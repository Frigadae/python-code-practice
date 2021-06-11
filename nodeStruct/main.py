from nodeModule import *

def main(num):
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.setPointer(node2)
    node2.setPointer(node3)
    node3.setPointer(node4)

    nodeList = node1

    while nodeList:
        print(nodeList.getData())
        nodeList = nodeList.getPointer()
        
num = 4
main(num)

