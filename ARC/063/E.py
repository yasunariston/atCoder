def dicstra(fromNode, toNode):


class Node:
    def __init__(self):
        self.connection = []
        self.value = None

    def connect(self, node):
        self.connection.append(node)

    def getDist(self, toNode):
        return dicstra(self, toNode)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value


N = int(input())
nodeDict = {}
for _ in range(N):
    node1, node2 = [int(i) for i in input().split()]
    nodeDict[node1] = Node()
    nodeDict[node2] = Node()
    nodeDict[node1].connect(nodeDict[node2])
    nodeDict[node2].connect(nodeDict[node1])

K = int(input())
for _ in range(K):
    node, value = [int(i) for i in input().split()]
    nodeDict[node].setValue(value)

for key in range(1, N + 1):
    if nodeDict[key].getValue() == None:

