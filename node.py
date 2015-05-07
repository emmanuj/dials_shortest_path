'''
Emmanuel John (emmanuj)
Encapsulates node data

'''
class Node:
    def __init__(self, id):
        self.id = id
        self.distance = float("inf")
        self.parent = self

    def __repr__(self):
        return "nodeId "+str(self.id)+" label "+ str(self.distance) + " parent "+ str(self.parent.id)
