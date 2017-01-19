import tkRAD
from source.model import *
from source.matrix import *
from source.scene import *
from source.loader import *
from tkinter.filedialog import askopenfilename

MATRIX_VIEW = Matrix(4, 4, [
        [100, 0, 0, 0],
        [0, 100, 0, 0],
        [0, 0, 100, 0],
        [300, 200, 0, 1]
    ])
MATRIX_START = Matrix(4, 4, [
        [0.01, 0, 0, 0],
        [0, 0.01, 0, 0],
        [0, 0, 0.01, 0],
        [-3, -2, 0, 1]
    ])


class Application(tkRAD.RADXMLMainWindow):

    APP = {
        "name": _("Obj Viewer"),
        "version": _("0.3a"),
        "description": _("Viewing and editing obj models"),
        "title": _("Obj Viewer"),
        "author": _("Daniel Derevjanik <daniel.derevjanik@gmail.com>"),
        "copyright": _("(c) 2015 Daniel Derevjanik."),
        "license": _("""
            This program is free software: you can redistribute
            it and/or modify it under the terms of the GNU
            General Public License as published by the Free
            Software Foundation, either version 3 of the
            License, or (at your option) any later version.
            This program is distributed in the hope that it will
            be useful, but WITHOUT ANY WARRANTY; without even the
            implied warranty of MERCHANTABILITY or FITNESS FOR A
            PARTICULAR PURPOSE. See the GNU General Public
            License for more details.

            You should have received a copy of the GNU General
            Public License along with this program.

            If not, see: http://www.gnu.org/licenses/
        """),
        "license_url": _("http://www.gnu.org/licenses/"),
    }  # end of APP

    def cmd_new_scene(self, **kwargs):
        """!
            Create new scene

            @desc delete all models from current scene
        """
        self.canvas.delete("all")
        self.models = list()

    def cmd_model_move(self, x, y, z, **kwargs):
        """!
            Move all models in current scene

            @param x (int): dx
            @param y (int): dy
            @param z (int): dz
        """
        for model in self.models:
            model.calculate(MoveMatrix(x, y, z))
            model.render()

    def cmd_model_toggle_texture(self, **kwargs):
        """!
            Toggle model texture

            @desc when is off, it'll shows wireframe model
        """
        for model in self.models:
            model.texture(show=not model.isTextured())

    def cmd_model_scale(self, scale, **kwargs):
        """!
            Scale model
        """
        self.cmd_model_calculate(ScaleMatrix(scale, scale, scale))

    def cmd_model_rotate_x(self, **kwargs):
        """!
            Rotate model by X coord
        """
        self.cmd_model_calculate(RotateMatrixX(0.1))

    def cmd_model_rotate_y(self, **kwargs):
        """!
            Rotate model by Y coord
        """
        self.cmd_model_calculate(RotateMatrixY(5))

    def cmd_model_rotate_z(self, **kwargs):
        """!
            Rotate model by Z coord
        """
        self.cmd_model_calculate(RotateMatrixZ(5))

    def cmd_model_calculate(self, matrix):
        """!
            It'll calculate all models with inserted matrix

            @desc function multiply all models with inserted matrix, but first
            it'll use Start matrix, then inserted matrix and last for center View Matrix.
            This order is used, when you want to have model on specific position.
        """
        for model in self.models:
            model.calculate(MATRIX_START)
            model.calculate(matrix)
            model.calculate(MATRIX_VIEW)
            model.render()

    def dlg_open_file(self, **kwargs):
        """!
            Show dialog for open file

            @desc now accepting only .obj file types

            @return (str): path to selected file
        """
        path = askopenfilename(filetypes=(("Obj Model", "*.obj"),
                                           ("All files", "*.*")))
        self.cmd_load_model(path)

    def cmd_load_model(self, path):
        """!
            Load model from path and it'll render it

            @desc method add loaded model to models Collection

            @param path (str): path to model
        """
        l = ObjLoader()

        model = l.loadModel(path)
        model.setCanvas(self.canvas)
        model.calculate(MATRIX_VIEW)
        model.render()

        self.models.append(model)

    def __init__(self):
        self.mainwindow = tkRAD.RADXMLMainWindow(title="Obj Viewer")

        xml = open('gui/window_main.xml', 'r').read()

        self.mainwindow.xml_build(xml)
        self.mainwindow.events.connect("new_scene", self.cmd_new_scene)
        self.mainwindow.events.connect("model_scale_up",   lambda **kwargs: self.cmd_model_scale(1.01))
        self.mainwindow.events.connect("model_scale_down", lambda **kwargs: self.cmd_model_scale(0.99))
        self.mainwindow.events.connect("model_rotate_x", self.cmd_model_rotate_x)
        self.mainwindow.events.connect("model_rotate_y", self.cmd_model_rotate_y)
        self.mainwindow.events.connect("model_rotate_z", self.cmd_model_rotate_z)

        self.mainwindow.events.connect("model_move_up",    lambda **kwargs: self.cmd_model_move(0,  -10, 0, **kwargs))
        self.mainwindow.events.connect("model_move_down",  lambda **kwargs: self.cmd_model_move(0,  10, 0, **kwargs))
        self.mainwindow.events.connect("model_move_left",  lambda **kwargs: self.cmd_model_move(-10, 0, 0, **kwargs))
        self.mainwindow.events.connect("model_move_right", lambda **kwargs: self.cmd_model_move(10,  0, 0, **kwargs))
        self.mainwindow.events.connect("model_texture_toggle", lambda **kwargs: self.cmd_model_toggle_texture())
        
        self.canvas = self.mainwindow.mainframe.canvas
        self.models = list()

        self.mainwindow.events.connect("model_add", self.dlg_open_file)

        self.testModel('../resources/objs/Buzz.obj')

        self.mainwindow.run()

    def testModel(self, path):
        """!
            Only for test purpose

            @desc method load obj model from selected path, then it render it
        """
        l = ObjLoader()
        self.model = l.loadModel(path)
        self.model.setCanvas(self.mainwindow.mainframe.canvas)
        self.model.calculate(MATRIX_VIEW)
        self.model.render()
        self.models.append(self.model)

app = Application()