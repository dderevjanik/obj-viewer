from .vertex import *
from .vector import *
from .face import *
from .matrix import *


class Model:

    """!
        Model describe obj object. Store information about 3D model.
        It also menages vertexes and faces in models.
    """

    def __init__(self, x, y, z):
        """!
            Create a blank model

            Args:
                x (float): model X coordination
                y (float): model Y coordination
                z (float): model Z coordination
        """
        self.__vertexes = list()
        self.__faces = list()

        self.__position = (x, y, z)

        self.__rendered = False

    # Section: Getters/Setters

    def getVertex(self, index):
        """!
            Get vertex with specifed index

            Args:
                index (int): index of vertex
        """
        return self.__vertexes[index]

    def getX(self):
        """Return X coordination of model"""
        return self.__position[0]

    def getY(self):
        """Return Y coordination of model"""
        return self.__position[1]

    def getZ(self):
        """Return Z coordination of model"""
        return self.__position[2]

    def isRendered(self):
        """Check if model is rendered

            Return:
                (bool): True if model is rendered
        """
        if self.__rendered:
            return True
        return False

    # Section: Methods

    def addFace(self, face):
        """!
            Add face to model

            Args:
                face (class.Face): face
        """
        self.__faces.append(face)

    def addVertex(self, vertex):
        """Add vertex to model

            vertex (class.Vertex): vertex
        """
        self.__vertexes.append(vertex)

    def calculateVertexes(self, matrix):
        """Recalculate all vertexes with matrix

            Args:
                matrix (class.Matrix): multicaption matrix

            Todo:
                correct method description
        """
        for vertex in self.__vertexes:
            vertex.calculate(matrix)

    def render(self):
        """Render model"""
        for face in self.__faces:
            face.render()
