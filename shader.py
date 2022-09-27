import game
from OpenGL.GL import *
import OpenGL.GL.shaders


class Shader:
    def __init__(self, vertexPath, fragmentPath, shader_name):
        game.Game.shaders[shader_name] = self
        vShaderFile = open(vertexPath)
        fShaderFile = open(fragmentPath)
        try:
            vertexCode = "".join(vShaderFile.readlines())
            fragmentCode = "".join(fShaderFile.readlines())
        finally:
            vShaderFile.close()
            fShaderFile.close()
        self.ID = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertexCode, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragmentCode, GL_FRAGMENT_SHADER))

    def use(self):
        glUseProgram(self.ID)

    def set_bool(self, name, value):
        glUniform1i(glGetUniformLocation(self.ID, name), value)

    def set_int(self, name, value):
        glUniform1i(glGetUniformLocation(self.ID, name), value)
        
    def set_float(self, name, value):
        glUniform1f(glGetUniformLocation(self.ID, name), value)

    def set_mat3(self, name, value):
        glUniformMatrix3fv(glGetUniformLocation(self.ID, name), 1, GL_FALSE, value)

    def set_mat4(self, name, value):
        glUniformMatrix4fv(glGetUniformLocation(self.ID, name), 1, GL_FALSE, value)

    def setVec3(self, name, value):
        glUniform3fv(glGetUniformLocation(self.ID, name), 1, value)

    def setVec2(self, name, value):
        glUniform2fv(glGetUniformLocation(self.ID, name), 1, value)