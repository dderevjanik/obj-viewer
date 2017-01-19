from .model import *
from .vertex import *
from .face import *


class ObjLoader:

    """!
        Load model from a .obj file format
    """

    def loadModel(self, path):
        """!
            Load model from path

            @param path (str): path to model

            @return (class.Model): model
        """
        model = Model(0, 0)

        f = open(path, 'r')

        for line in f.readlines():
            line = line.split(' ')
            if len(line) == 0:
                # blank line, skip
                pass
            elif line[0] == 'v':
                # vertex
                vertex = Vertex(line[1], line[2], line[3])
                model.addVertex(vertex)
            elif line[0] == 'f':
                # face
                face = Face()
                for vIndex in line[1:]:
                    face.addVertex(model.getVertex(int(vIndex) - 1))
                model.addFace(face)
            elif line[0] == 'o':
                # model name
                pass
            else:
                # other
                pass

        f.close()

        return model

    def saveModel(self, model, path):
        """!
            Save model

            @param path (str): path where to save

            @todo finish save Model
        """
        pass
