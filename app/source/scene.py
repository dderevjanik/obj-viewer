import tkinter
from .model import *
from .matrix import *


class Scene:

    """!
        Scene create enviroment for 3D models and manage
        main functions as rendering, placing models,
        updating and more
    """

    def __init__(self, mainroot, x, y, width, height):
        """!
            Initialize scene created from tkinter.Frame and tkinter.Canvas

            @param mainroot (tkinter.Tk): main root,
                on which will be scene created
            @param x (int): x position
            @param y (int): y position
            @param width (int): scene width (scene.width == canvas.width)
            @param height (int): scene height (scene.height == canvas.height)
        """
        x, y, width, height = int(x), int(y), int(width), int(height)
        self.mainroot = mainroot

        self.root = tkinter.Frame(mainroot)
        self.root.place()

        self.__canvas = tkinter.Canvas(
            self.mainroot, width=width - x, height=height - y, bg='white')
        self.__canvas.place(x=x, y=y)

        self.__models = list()
