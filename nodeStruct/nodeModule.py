class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

    def setData(self, newData):
        self.data == newData

    def getData(self):
        return self.data

    def setPointer(self, newPoint):
        self.pointer = newPoint

    def getPointer(self):
        return self.pointer

class NodeList:
    def __init__(self):
        self.head = None
        self.count = 0