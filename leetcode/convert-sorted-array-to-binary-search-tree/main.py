# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        ソート済みのlistからBinary Search Treeを作る問題。
        BSTの定義におけるrootノードの値はどうでも良くて、単純にrootよりも小さければleftへ大きければrightへ配置。
        すでにソート済みのためこのロジックは不要で、BSTの高さを合わせるために要素数を2で割ってrootのノードを選定するだけいい。
        """
        if len(nums) == 0:
            return
        # index for root. truncate division. 
        i = len(nums)//2
        root = TreeNode(val=nums[i])
        root.left = self.sortedArrayToBST(nums=nums[:i])
        root.right = self.sortedArrayToBST(nums=nums[i+1:])
        return root