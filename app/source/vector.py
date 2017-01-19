import math


class Vector:

    def __init__(self, x, y, z):
        """Initialize Vector

        Args:
            x (int): x position
            y (int): y position
            z (int): z position
        """
        self.__x = x
        self.__y = y
        self.__z = z
        self.__size = math.sqrt(x*x + y*y + z*z)

    # Section: Magic Methods

    def __repr__(self):
        name = "Vector\n"
        cord = """\t
        X:{} Y:{} Z:{}""".format(self.getX(), self.getY(), self.getY())
        return name + cord

    def __eq__(self, other):
        if self.__x != other.getX():
            return False
        if self.__y != other.getY():
            return False
        if self.__z != other.getZ():
            return False
        return True

    def __sub__(self, other):
        x1, y1, z1 = self.getX(), self.getY(), self.getZ()
        x2, y2, z2 = other.getX(), other.getY(), other.getZ()
        return Vector(x1 - x2, y1 - y2, z1 - z2)

    def __mul__(self, other):
        x1, y1, z1 = self.getX(), self.getY(), self.getZ()
        x2, y2, z2 = other.getX(), other.getY(), other.getZ()
        vector = Vector(y1*z2 - y2*z1, z1*x2 - z2*x1, x1*y2 - x2*y1)
        return vector

    # Section: Getters

    def getX(self):
        """Get X position"""
        return self.__x

    def getY(self):
        """Get Y position"""
        return self.__y

    def getZ(self):
        """Get Z position"""
        return self.__z

    def getSize(self):
        """Return size of current vector"""
        return self.__size

    # Section: changable Methods

    def normalize(self):
        """Normalize current vector"""
        size = self.size()
        self.__x /= size
        self.__y /= size
        self.__z /= size

    def multiply(self, other):
        """Multiply currrent vector by other

        Args:
            other (Vector): other vector
        """
        x1, y1, z1 = self.__x, self.__y, self.__z
        x2, y2, z2 = other.getX(), other.getY(), other.getZ()
        self.__x = y1*z2 - y2*z1
        self.__y = z1*x2 - z2*x1
        self.__z = x1*y2 - x2*y1

    def subtraction(self, other):
        """Subtraction current vector

        Args:
            other (Vector): other vector
        """
        self.__x -= other.getX()
        self.__y -= other.getY()
        self.__z -= other.getZ()

    # Section: returning Methods

    def createNormalVector(self):
        """Return normalized normalized vector

        Return:
            Vector Object
        """
        size = self.size()
        x, y, z = self.getX(), self.getY(), self.getZ()
        return Vector(x/size, y/size, z/size)

    def scalarVector(self, other):
        """Return scalar

        Return:
            Int scalar
        """
        x1, y1, z1 = self.getX(), self.getY(), self.getZ()
        x2, y2, z2 = other.getX(), other.getY(), other.getZ()
        return (x1*x2) + (y1*y2) + (z1*z2)
