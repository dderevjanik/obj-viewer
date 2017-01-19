from .matrix import *
"""!
    View Matrix

    @todo add CONST_MAIN to config files
    @todo clean description
"""

MATRIX_VIEW = Matrix(4, 4, [
    [100, 0, 0, 0],
    [0, -100, 0, 0],
    [0, 0, 0, 0],
    [300, 200, 0, 1]
])


class Vertex:

    """!
        Vertex represents point in 3D,
        store default info about his coordinations
        also store math Matrix,
        where all operations are computed
    """

    def __init__(self, x, y, z, e=1):
        """!
            Initialize vertex

            Args:
                x (float): X
                y (float): Y
                z (float): Z
                e (float): extra
        """
        # set original coords
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)
        self.__e = float(e)

        # initialize matrix
        self.__initMatrix(x, y, z, e)

    # Section: Magic Methods

    def __repr__(self):
        name = "Vertex:\n"
        orig = """\toriginal:
        X:{} Y:{} Z:{}\n""".format(self.__x, self.__y, self.__z)
        curr = """\tcurrent:
        X:{} Y:{} Z:{}""".format(self.getX(), self.getY(), self.getZ())
        return name + orig + curr

    # Section: Private Methods

    def __initMatrix(self, x, y, z, e):
        """!
            Initialize a matrix

            Args:
                x (float): X coordination
                y (float): Y coordination
                z (float): Z coordination
                e (float): extra
        """
        self.__matrix = Matrix(
            1, 4, [[float(x), float(y), float(z), float(e)]])

    # Section: Changable Methods

    def calculate(self, matrix):
        """!
            Multiplication vertex matrix with inserted matrix

            Args:
                matrix (class.Matrix): multiplication matrix

            Todo:
                optimize this with adding
                method class.Matrix.multiplication(matrix)
        """
        self.__matrix = self.__matrix * matrix

    # Section: Getters - Original Coordinations

    def getOrgX(self):
        """get original (initialized) X coordination"""
        return self.__x

    def getOrgY(self):
        """get original (initialized) Y coordination"""
        return self.__y

    def getOrgZ(self):
        """get original (initialized) Z coordination"""
        return self.__z

    def getOrgE(self):
        """get original (initialized) E coordination"""
        return self.__e

    # Section: Getters

    def getX(self):
        """get current X coordination"""
        return self.__matrix[0][0]

    def getY(self):
        """get current Y coordination"""
        return self.__matrix[0][1]

    def getZ(self):
        """get current Z coordination"""
        return self.__matrix[0][2]

    def getE(self):
        """get current E coordination"""
        return self.__matrix[0][3]
