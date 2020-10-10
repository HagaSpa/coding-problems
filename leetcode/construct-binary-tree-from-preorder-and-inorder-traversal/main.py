# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List
from collections import deque


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0 or len(inorder)==0:
            return
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root


if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    s = Solution()
    root = s.buildTree(preorder=preorder, inorder=inorder)
    print(root)