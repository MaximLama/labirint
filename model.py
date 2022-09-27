import pyrr
import objparser
import mesh
import shader as sh
import numpy
from OpenGL.GL import *
from PIL import Image
import os
import game
import collision as col


class Model:
    def __init__(self, objPath, mtlPath, is_dynamic = False):
        self.meshes = []
        self.directory = ""
        self.textures_loaded = []
        self.shader = None
        self.min_point = [numpy.inf, numpy.inf, numpy.inf]
        self.max_point = [-numpy.inf, -numpy.inf, -numpy.inf]
        self.collision = None
        self.is_dynamic = is_dynamic
        self.loadModel(objPath, mtlPath)
        self.create_collision()

    def Draw(self, shader_inst):
        for i in range(0, len(self.meshes)):
            self.meshes[i].Draw(shader_inst)

    def loadModel(self, objPath, mtlPath):
        model = objparser.Model(objPath, mtlPath)
        self.directory = objPath[0:objPath.rfind('/')]
        print(self.directory)
        self.processNode(model)

    def processNode(self, model):
        for mesh_inst in model.objects:
            self.meshes.append(self.processMesh(mesh_inst))

    def processMesh(self, mesh_inst):
        for i in range(3):
            if self.min_point[i] > mesh_inst.min[i]:
                self.min_point[i] = mesh_inst.min[i]
            if self.max_point[i] < mesh_inst.max[i]:
                self.max_point[i] = mesh_inst.max[i]
        textures = []
        vertices = mesh_inst.verticesAttributes
        indices = mesh_inst.indices
        material = mesh_inst.material
        diffuseMaps = self.loadMaterialTextures(material, "texture_diffuse")
        if diffuseMaps:
            textures.extend(diffuseMaps)

        #specularMaps = self.loadMaterialTextures(material, "texture_specular")
        #textures.extend(specularMaps)

        #normalMaps = self.loadMaterialTextures(material, "texture_normal")
        #textures.extend(normalMaps)

        print(textures)

        return mesh.Mesh(vertices, textures, indices)
    def loadMaterialTextures(self, mat, typename):
        print("loadMaterialTextures")
        textures = []
        str = ''
        if typename == "texture_diffuse":
            if "diffuse" in mat.mapNames:
                str = mat.diffuseMap
            else:
                return
        if typename == "texture_specular":
            str = mat.texture_specular_color.name
        if typename == "texture_normal":
            str = mat.texture_bump.name
        skip = False
        for texts in self.textures_loaded:
            if str == texts.path:
                textures.append(texts)
                skip = True
                break
        if not skip:
            texture = mesh.Texture(self.TextureFromFile(str, self.directory), typename, str)
            textures.append(texture)
            self.textures_loaded.append(texture)
        return textures

    def TextureFromFile(self, path, directory):
        print("TextureFromFile")
        filename = directory + '/' + path
        cacheFilename = directory + '/cache/' + path
        print(filename)
        print(cacheFilename)
        textureId = glGenTextures(1)
        image = Image.open(filename)
        image.transpose(Image.FLIP_TOP_BOTTOM)
        format = ''
        if image.mode == "L":
            format = GL_RED
        if image.mode == "P":
            image = image.convert("RGBA")
            format = GL_RGBA
        if image.mode == "RGB":
            format = GL_RGB
        if image.mode == "RGBA":
            format = GL_RGBA
        if os.path.exists(cacheFilename+".npy"):
            data = numpy.load(cacheFilename+'.npy')
        else:
            if not os.path.isdir(directory+'/cache'):
                os.mkdir(directory+'/cache')
            data = numpy.array(list(image.getdata()), numpy.uint8)
            numpy.save(cacheFilename, data)
        print(image.mode)
        glBindTexture(GL_TEXTURE_2D, textureId)
        glTexImage2D(GL_TEXTURE_2D, 0, format, image.size[0], image.size[1], 0, format, GL_UNSIGNED_BYTE, data)
        glGenerateMipmap(GL_TEXTURE_2D)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        if format == GL_RGBA:
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        image.close()

        return textureId

    def prepare_instanced_draw(self, model_matrices):
        for i in range(len(self.meshes)):
            self.meshes[i].prepare_instanced_draw(model_matrices)

    def set_shader(self, shader):
        self.shader = shader

    def draw_instanced(self, amount):
        for i in range(len(self.meshes)):
            self.meshes[i].draw_instanced(self.shader, amount)

    def create_collision(self):
        self.collision = col.Collision(self.min_point, self.max_point)
