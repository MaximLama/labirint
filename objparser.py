import numpy
import os


class ObjParser:
    class Material:
        def __init__(self, name):
            self.name = name
            self.specularExponent = False
            self.ambientColor = False
            self.diffuseColor = False
            self.specularColor = False
            self.indexOfRefraction = False
            self.opacity = False
            self.illuminationModel = False
            self.mapNames = list()
            self.diffuseMap = False

    class Object:
        def __init__(self, name):
            self.name = name
            self.Vertices = []
            self.TexCoords = []
            self.Normals = []
            self.Material = False
            self.useSmoothShading = False
            self.TextPolygons = []
            self.min = [numpy.inf, numpy.inf, numpy.inf]
            self.max = [-numpy.inf, -numpy.inf, -numpy.inf]

    def __init__(self, objPath, mtlPath):
        self.objPath = objPath
        self.mtlPath = mtlPath
        self.objTextLines = ''
        self.mtlTextLines = ''
        self.Objects = list()
        self.Materials = dict()

    def openFiles(self):

        fname, fextension = os.path.splitext(self.objPath)
        if fextension != '.obj':
            return False
        fname, fextension = os.path.splitext(self.mtlPath)
        if fextension != '.mtl':
            return False
        try:
            with open(self.objPath) as fObj:
                self.objTextLines = fObj.readlines()
            if self.objTextLines is not "":
                with open(self.mtlPath) as fMtl:
                    self.mtlTextLines = fMtl.readlines()
            if self.objTextLines == "" or self.mtlTextLines == "":
                return False
            return True
        except Exception:
            return False

    def parse(self):
        self.parseMtlText()
        self.parseObjText()
        for obj in self.Objects:
            max_el = abs(max(obj.max))
            min_el = abs(min(obj.min))
            scale = 1
            if max_el > min_el:
                scale = max_el
            else:
                scale = min_el
            obj.Vertices = obj.Vertices / scale
            obj.max = obj.max/scale
            obj.min = obj.min/scale

    def parseObjText(self):
        for line in self.objTextLines:
            line = line.strip()
            lineEls = line.split(" ")
            if lineEls[0] == "f":
                self.addPolygon(lineEls[1:])
            if lineEls[0] == "v":
                self.addVertex(lineEls[1:])
            if lineEls[0] == "vt":
                self.addTexCoords(lineEls[1:3])
            if lineEls[0] == "vn":
                self.addNormal(lineEls[1:])
            if lineEls[0] == "usemtl":
                self.setMaterial(lineEls[1])
            if lineEls[0] == "s":
                self.setShading(lineEls[1])
            if lineEls[0] == "o":
                self.createObject(lineEls[1])
            if lineEls[0] == "#" or lineEls == "\n":
                continue
            if lineEls[0] == "mtllib":
                self.materialFile = lineEls[1]
                continue

    def parseMtlText(self):
        for line in self.mtlTextLines:
            line = line.strip()
            lineEls = line.split(" ")
            if lineEls[0] == "Ns":
                self.setSpecularExponent(lineEls[1])
            if lineEls[0] == "Ka":
                self.setAmbientColor(lineEls[1:])
            if lineEls[0] == "Kd":
                self.setDiffuseColor(lineEls[1:])
            if lineEls[0] == "Ks":
                self.setSpecularColor(lineEls[1:])
            if lineEls[0] == "Ni":
                self.setIndexOfRefraction(lineEls[1])
            if lineEls[0] == "d":
                self.setOpacity(lineEls[1])
            if lineEls[0] == "illum":
                self.setIlluminationModel(lineEls[1])
            if lineEls[0] == "map_Kd":
                self.setDiffuseMap(lineEls[1])
            if lineEls[0] == "newmtl":
                self.createMaterial(lineEls[1])
            if lineEls[0] == "#" or lineEls == "\n":
                continue

    def createObject(self, objName):
        self.currentObj = self.Object(objName)
        self.Objects.append(self.currentObj)

    def addVertex(self, vertex):
        self.currentObj.Vertices.append(numpy.array(vertex, dtype="float32"))
        for i in range(len(self.currentObj.Vertices[-1])):
            el = self.currentObj.Vertices[-1][i]
            if el < self.currentObj.min[i]:
                self.currentObj.min[i] = el
            if el > self.currentObj.max[i]:
                self.currentObj.max[i] = el

    def addTexCoords(self, texCoords):
        self.currentObj.TexCoords.append(numpy.array(texCoords, dtype="float32"))

    def addNormal(self, normal):
        self.currentObj.Normals.append(numpy.array(normal, dtype="float32"))

    def addPolygon(self, polygon):
        self.currentObj.TextPolygons.append(polygon)

    def setMaterial(self, materialName):
        self.currentObj.Material = self.Materials[materialName]

    def setShading(self, shadingText):
        if shadingText == "1":
            self.currentObj.useSmoothShading = True

    def createMaterial(self, materialName):
        self.currentMat = self.Material(materialName)
        self.Materials[materialName] = self.currentMat

    def setSpecularExponent(self, specularExponent):
        self.currentMat.specularExponent = float(specularExponent)

    def setAmbientColor(self, ambientColor):
        self.currentMat.ambientColor = numpy.array(ambientColor, dtype="float32")

    def setDiffuseColor(self, diffuseColor):
        self.currentMat.diffuseColor = numpy.array(diffuseColor, dtype="float32")

    def setSpecularColor(self, specularColor):
        self.currentMat.specularColor = numpy.array(specularColor, dtype="float32")

    def setIndexOfRefraction(self, indexOfRefraction):
        self.currentMat.indexOfRefraction = float(indexOfRefraction)

    def setOpacity(self, opacity):
        self.currentMat.opacity = float(opacity)

    def setIlluminationModel(self, illuminationModel):
        if illuminationModel == "2":
            self.currentMat.illuminationModel = "ambient+diffuse+color"

    def setDiffuseMap(self, diffuseMap):
        self.currentMat.mapNames.append('diffuse')
        self.currentMat.diffuseMap = diffuseMap

class Model:
    class Object:
        def __init__(self):
            self.material = False
            self.nPolygons = 0
            self.verticesAttributes = list()
            self.indices = list()

    def __init__(self, objPath, mtlPath):
        objParser = ObjParser(objPath, mtlPath)
        if objParser.openFiles():
            objParser.parse()
            self.objects = list()
            for obj in objParser.Objects:
                modelObject = self.Object()
                modelObject.material = obj.Material
                modelObject.min = obj.min
                modelObject.max = obj.max
                modelObject.nPolygons = len(obj.TextPolygons[0])
                modelObject.verticesAttributes = self.getVerticesAttributes(obj)
                modelObject.indices = self.getIndices(obj)
                self.objects.append(modelObject)

    def getVerticesAttributes(self, obj):
        self.masPolygons = list(numpy.unique(numpy.array(obj.TextPolygons).flatten()))
        verticesAttribs = numpy.array([], dtype="float32")
        for el in self.masPolygons:
            indices = el.split("/")
            verticesAttribs = numpy.concatenate((verticesAttribs, obj.Vertices[int(indices[0])-1]))
            verticesAttribs = numpy.concatenate((verticesAttribs, obj.TexCoords[int(indices[1])-1]))
            verticesAttribs = numpy.concatenate((verticesAttribs, obj.Normals[int(indices[2])-1]))
        return verticesAttribs

    def getIndices(self, obj):
        indices = list()
        for i in obj.TextPolygons:
            for j in i:
                indices.append(self.masPolygons.index(j))
        return numpy.array(indices, dtype="uint32")

'''model = Model("resources/rock/rock.obj", "resources/rock/rock.mtl")
for el in model.objects:
    pprint.pprint(vars(el))'''