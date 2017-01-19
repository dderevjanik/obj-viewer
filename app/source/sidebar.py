import tkinter


class Sidebar:

    """!
        GUI Addon. Sidebar store list of current models in scene,
        it also provide basic functions.
    """

    def __init__(self, root, x, y, width, height):
        x, y, width, height = int(x), int(y), int(width), int(height)
        self.root = root

        self.frame = tkinter.Frame(root, background="red")
        self.frame.place(x=x, y=y, width=width, relheight=height)

        self.header = tkinter.Label(self.frame, text="Models")
        self.header.place(x=x, y=y, width=width, height=24)

        self.init_list()

    def init_list(self):
        self.itemCnt = 0
        self.items = list()
        self.selected = None

        self.listbox = tkinter.Listbox(self.frame)
        self.listbox.place(x=0, y=24, relheight=1, width=120)

    def append(self, key, item):
        self.listbox.insert(self.itemCnt, key)
        self.items.append(item)
        self.itemCnt += 1

        return self.itemCnt

    def clearList(self):
        self.items = list()
        self.listbox.delete(0, self.itemCnt)
        self.itemCnt = 0
        self.selected = None
