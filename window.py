import glfw
from OpenGL.GL import *
import mouse_input_controller as mic


class Window:
    def __init__(self, window_name: str):
        self.window = None
        glfw.init()
        self.mode = glfw.get_video_mode(glfw.get_primary_monitor())
        self.__width_scr = self.mode.size.width
        self.__height_scr = self.mode.size.height
        self.aspect_ratio = self.__width_scr/self.__height_scr
        self.__window_name = window_name
        self.mouse_input_controller_instance = mic.MouseInputController()
        self.create_window()

    def create_window(self):
        self.window = glfw.create_window(self.__width_scr, self.__height_scr, "My game", glfw.get_primary_monitor(), None)
        if not self.window:
            print("Don't work")
            glfw.terminate()

        glfw.make_context_current(self.window)
        glfw.set_framebuffer_size_callback(self.window, self.framebuffer_size_callback)
        glfw.set_cursor_pos_callback(self.window, self.mouse_input_controller_instance.mouse_callback)

        glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED)

    def framebuffer_size_callback(self, window, width, height):
        self.__width_scr = width
        self.__height_scr = height
        self.aspect_ratio = self.__width_scr/self.__height_scr
        glViewport(0, 0, width, height)

    def close_window(self):
        glfw.set_window_should_close(self.window, True)

    def __del__(self):
        glfw.terminate()
        return 0
