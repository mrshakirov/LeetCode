#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3290/

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

# Complexity O(N), where N is number of Nodes in Linked List