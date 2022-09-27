from OpenGL.GL import *
import numpy


class Texture:
    def __init__(self, id, type, path):
        self.id = id
        self.type = type
        self.path = path


class Mesh:
    def __init__(self, vertices, textures, indices):
        self.vertices = vertices
        self.textures = textures
        self.indices = indices
        self.VAO = 0
        self.VBO = 0
        self.EBO = 0
        self.setup_mesh()

    def Draw(self, shader):
        diffuseNr = 1
        #specularNr = 1
        for i in range(0, len(self.textures)):
            glActiveTexture(GL_TEXTURE0 + i)
            number = 0
            name = self.textures[i].type
            if name == "texture_diffuse":
                number = diffuseNr
                diffuseNr+=1
            '''elif name == "texture_specular":
                number = specularNr
                specularNr+=1'''

            shader.setFloat("material."+name+str(number), i)
            glBindTexture(GL_TEXTURE_2D, self.textures[i].id)

        glActiveTexture(GL_TEXTURE0)

        glBindVertexArray(self.VAO)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
        glBindVertexArray(0)

    def setup_mesh(self):

        self.VAO = numpy.array(glGenVertexArrays(1), dtype=numpy.uint32)
        self.VBO = numpy.array(glGenBuffers(1), dtype=numpy.uint32)
        self.EBO = numpy.array(glGenBuffers(1), dtype=numpy.uint32)

        glBindVertexArray(self.VAO)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)

        glBufferData(GL_ARRAY_BUFFER, len(self.vertices)*4, self.vertices, GL_STATIC_DRAW)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(self.indices)*4, self.indices, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)

        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(20))
        glEnableVertexAttribArray(2)

        glBindVertexArray(0)

    def prepare_instanced_draw(self, model_matrices):
        self.instanced_buffer = glGenBuffers(1)
        print(self.instanced_buffer)
        glBindBuffer(GL_ARRAY_BUFFER, self.instanced_buffer)
        glBufferData(GL_ARRAY_BUFFER, len(model_matrices) * 16 * 4, model_matrices, GL_STATIC_DRAW)
        glBindVertexArray(self.VAO)
        vec4Size = 16
        glEnableVertexAttribArray(3)
        glVertexAttribPointer(3, 4, GL_FLOAT, GL_FALSE, 4 * vec4Size, ctypes.c_void_p(0))
        glEnableVertexAttribArray(4)
        glVertexAttribPointer(4, 4, GL_FLOAT, GL_FALSE, 4 * vec4Size, ctypes.c_void_p(1 * vec4Size))
        glEnableVertexAttribArray(5)
        glVertexAttribPointer(5, 4, GL_FLOAT, GL_FALSE, 4 * vec4Size, ctypes.c_void_p(2 * vec4Size))
        glEnableVertexAttribArray(6)
        glVertexAttribPointer(6, 4, GL_FLOAT, GL_FALSE, 4 * vec4Size, ctypes.c_void_p(3 * vec4Size))

        glVertexAttribDivisor(3, 1)
        glVertexAttribDivisor(4, 1)
        glVertexAttribDivisor(5, 1)
        glVertexAttribDivisor(6, 1)

        glBindVertexArray(0)

    def draw_instanced(self, shader, amount):
        diffuse_nr = 1
        for i in range(len(self.textures)):
            glActiveTexture(GL_TEXTURE0 + i)
            number = 0
            name_texture = self.textures[i].type
            if name_texture == "texture_diffuse":
                number = diffuse_nr
                diffuse_nr += 1
            shader.set_float(name_texture + str(number), i)
            glBindTexture(GL_TEXTURE_2D, self.textures[i].id)
        #shader.set_vec3("material.ambient_color", self.material.ambient_color)
        #shader.set_vec3("material.diffuse_color", self.material.diffuse_color)
        if len(self.textures):
            glActiveTexture(GL_TEXTURE0)
        glBindVertexArray(self.VAO)
        glDrawElementsInstanced(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None, amount)
        glBindVertexArray(0)
