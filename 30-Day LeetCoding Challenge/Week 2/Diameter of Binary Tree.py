#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3293/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class LeetCode:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def getDiameter(node):
            if not node: return 0

            l, r = getDiameter(node.left), getDiameter(node.right)
            self.ans = max(self.ans, l+r)
            return max(l, r) + 1 #adding node itself

        if not root: return 0
        self.ans = float('-inf')
        getDiameter(root)
        return self.ans

# Complexity is o(N), where N is number of nodes