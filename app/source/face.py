class Face:

    """!
        Face is polygon representet by Vertex points.
        It can render whole face by vertex points.
    """

    def __init__(self, vertexes=[]):
        """!
            Initialize Face

            @param vertexes (iterable(Vertex)): reference on used vertexes
        """
        self.__vertexes = list()  # store reference to vertexes
        self.__face = None   # create_polygon()
        self.__rendered = False  # ? rendered
        self.__textured = True   # ? textured

        self.__addVertexes(vertexes)

    def __repr__(self):
        name = "Face"
        return "{}:\n\tVertexes: {}".format(name, self.__vertexes)

    def __addVertexes(self, vertexes):
        """!
            Add vertexes reference to face

            @param vertexes (iterable(Vertex)): reference on used vertexes
        """
        for vertex in vertexes:
            self.__vertexes.append(vertex)

    def setCanvas(self, canvas):
        """!
            Set canvas to Face

            @param canvas (ICanvas): canvas on which render
        """
        self.__canvas = canvas

    def addVertex(self, vertex):
        """!
            Add vertex to Face

            @param vertex(Class.vertex): vertex to add

            @todo make shall copy
        """
        self.__vertexes.append(vertex)

    def vertexCount(self):
        """!
            Vertexes count

            @return (int): number of vertexes in face
        """
        return len(self.__vertexes)

    def isRendered(self):
        """!
            Check if face is rendered

            @return (bool): True if face is render, otherwise False
        """
        return self.__rendered

    def isTextured(self):
        """!
            Check if face has texture

            @return (bool): True if face has texture, otherwise False
        """
        return self.__textured

    def __render(self, coords):
        """!
            Real face render

            @param coords (list(float)): face vertex positions
        """
        self.__face = self.__canvas.create_polygon(
            *coords, fill='white', outline='black')

    def __update(self, coords):
        """!
            Update rendered face

            @param coords (list(float)): new face vertex positions
        """
        self.__canvas.coords(self.__face, *coords)

    def fill(self, fill=True):
        """!
            Fill face with 'white' color

            @param fill (bool, True): when set to True,
                face will be filled with color

            @todo more options (colors/textures)
        """
        if fill:
            if self.isTextured():
                pass
            else:
                self.__canvas.itemconfig(self.__face, fill='white')
                self.__textured = True
        else:
            if self.isTextured():
                self.__canvas.itemconfig(self.__face, fill='')
                self.__textured = False
            else:
                pass

    def render(self):
        """!
            Render face from vertexes
        """
        coords = list()
        for vertex in self.__vertexes:
            coords.append(vertex.getX())
            coords.append(400 - vertex.getY())

        # check if face is rendered before
        if self.isRendered():
            self.__update(coords)
        else:
            self.__render(coords)
            self.__rendered = True
