#Given a non-empty, singly linked list with head node head, return a middle node of linked list.

#If there are two middle nodes, return the second middle node.

from typing import List

class LinkedList:
    def __init__(self, nodes=None):
            self.head = None
            if nodes is not None:
                node = Node(data=nodes.pop(0))
                self.head = node
                for elem in nodes:
                    node.next = Node(data=elem)
                    node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LeetCode:
    def middleNode(self, head: Node) -> Node:
        fast = slow = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow.data

l = LeetCode()

llist = LinkedList(["1","2","3","4","5"])


print(l.middleNode(llist.head))

# Complexity O(n)