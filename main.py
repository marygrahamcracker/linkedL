from typing_extensions import Self

class node():
    def __init__(self, id: int, Name: str) -> None:
        self._id:int = id
        self._Name:str = Name
        self._next:node = None
    
    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, value:int):
        self.id = value

    @property
    def id(self) -> str:
        return self._name
    @Name.setter
    def id(self, value:str):
        self._name = value

    @property
    def next(self) -> Self:
        return self._next
    @next.setter
    def next(self, value:Self):
        self._next = value

class LinkedList():
    def __init__(self) -> None:
        self._nodeList: dict[int, node] = {}
        self.nodepos: dict[int, int] = {}

    def addNode(self, node:node) -> None:
        #we have to dedupe the node being passed in...gotta be unique
        if node is not None:
            found: bool = node.id in self._nodeList
            if not found:
                pos = len(self._nodeList) + 1
                self._nodepos[pos] = node.id
                self._addList[node.id] = node
            
            if pos > 1:
                prevnodepos = pos - 1 
                prevnodeid = self.nodepos[prevnodepos]
                prevnode = self._nodeList[prevnodeid]
                prevnode.next = node

        #add node to internal list
        #ensure last node in lost has its next property pointed to this node being added

node1 = node(1,'mike')
node2 = node(2,'mary')
node3 = node(3,'felicity')
node4 = node(4,'dad')
node11 = node(1, 'mikey')

myLL = LinkedList()
myLL.addNode(node1)
myLL.addNode(node2)
myLL.addNode(node3)
myLL.addNode(node4)
myLL.addNode(node11)

# mylist = [node1, node2, node3, node4]
# mylist[0].name = 'mike2'
# print(f'node1.name euals: {node1.name}')