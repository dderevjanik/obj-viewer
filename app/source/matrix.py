import math
"""!
    @todo Scaling matrix with only 1 argument
    @todo Rotatotion matrix use function for calculate sinus and
        cosinus (also math.radians(angle))
"""


class Matrix:

    """!
        Math matrix. It contains translations, rotations and
        multiply scaling methods.

        @param rows (int): number of rows in matrix
        @param cols (int): number of collumns in matrix
        @param array (list(list(int))): 2D array of cols*rows size with values

    """

    def __init__(self, rows, cols, array):
        """!
            Initialize matrix

            @param rows (int): number of rows
            @param cols (int): number of cols
            @param array (list(list(int))): array
        """
        self.rows = rows
        self.cols = cols
        self.array = array

    def __getitem__(self, row):
        return self.array[row]

    def __mul__(self, another):
        """!
            Multiply another matrix with current.
            It doesn't change this or another matrix.

            @param another (class.Matrix): Another matrix

            @return (class.Matrix): return new matrix,
                which is computed by multiply this and another
        """
        array = []

        for i in range(self.rows):
            array.append([0] * another.cols)

        result = Matrix(self.rows, another.cols, array)

        for i in range(self.rows):
            for j in range(another.cols):
                for k in range(self.cols):
                    result.array[i][j] += self.array[i][k] * \
                        another.array[k][j]

        return result

    def __repr__(self):
        name = "Matrix: \n"
        size = "\tROWS: {}\n\tCOLS: {}\n".format(self.rows, self.cols)
        array = "\t\t"

        for i in range(self.rows):
            for j in range(self.cols):
                array += "{} ".format(self.array[i][j])
            array += "\n\t\t"

        return name + size + array


class MoveMatrix(Matrix):

    def __init__(self, x, y, z):
        """!
            Initialize move matrix

            @param x (float): x
            @param y (float): y
            @param z (float): z
        """
        super().__init__(4, 4, [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [x, y, z, 1]
        ])


class RotateMatrixX(Matrix):

    def __init__(self, x):
        """!
            Initialize rotate matrix

            @param x (float): x rotation
        """
        self.__x = x
        angle = math.radians(x)
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)
        super().__init__(4, 4, [
            [1, 0,  0,  0],
            [0,  math.cos(x), -math.sin(x),  0],
            [0,  math.sin(x),  math.cos(x), 0],
            [0,  0,  0,  1]
        ])


class RotateMatrixY(Matrix):

    def __init__(self, y):
        """!
            Initialize rotate matrix

            @param y (float): y rotation
        """
        self.__y = y
        angle = math.radians(y)
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)
        super().__init__(4, 4, [
            [cos_a, 0,  sin_a,  0],
            [0, 1, 0,  0],
            [-sin_a,  0,  cos_a, 0],
            [0,  0,  0,  1]
        ])


class RotateMatrixZ(Matrix):

    def __init__(self, z):
        """!
            Initialize rotate matrix

            @param z (float): z rotation
        """
        self.__z = z
        z = math.radians(z)
        super().__init__(4, 4, [
            [math.cos(z), math.sin(z),  0, 0],
            [-math.sin(z), math.cos(z), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])


class TranslationMatrix(Matrix):

    def __init__(self, tx, ty, tz):
        """!
            Initialize rotate matrix

            @param z (float): z rotation
        """
        self.__z = z
        z = math.radians(z)
        super().__init__(4, 4, [
            [1, 0,  0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [tx, ty, tz, 1]
        ])


class ScaleMatrix(Matrix):

    def __init__(self, sx, sy, sz):
        """!
            Initialize scaling matrix

            @param sx (float): x scaling
            @param sy (float): y scaling
            @param sz (float): z scaling
        """
        self.__sx = sx
        self.__sy = sy
        self.__sz = sz
        super().__init__(4, 4, [
            [sx, 0,  0,  0],
            [0,  sy, 0,  0],
            [0,  0,  sz, 0],
            [0,  0,  0,  1]
        ])

    def __repr__(self):
        name = "Scaling Matrix: \n"
        size = "\tROWS: {}\n\tCOLS: {}\n".format(self.rows, self.cols)
        array = "\t\t"

        for i in range(self.rows):
            for j in range(self.cols):
                array += "{} ".format(self.array[i][j])
            array += "\n\t\t"

        return name + size + array

    def setScaling(self, sx, sy, sz):
        """!
            Set scaling values

            @param sx (float): x scaling
            @param sy (float): y scaling
            @param sz (float): z scaling
        """
        self.array[0][0] = sx
        self.array[1][1] = sy
        self.array[2][2] = sz
