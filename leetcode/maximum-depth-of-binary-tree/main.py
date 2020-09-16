from math import floor


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node.val) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        current_level = next_level


if __name__ == "__main__":
    tree = [3,9,20,None,None,15,7]
    
    # convert TreeNode
    root = TreeNode(val=tree[0])
    p = root
    prev = root
    tmp_i = 0
    for i,v in enumerate(tree[1:], 1):
        t = TreeNode(val=v)
        # f is index of node
        f = floor((i-1)/2)
        # same node
        if f == tmp_i:
            if i%2==0:
                p.right = t
            else:
                p.left = t
        else:
            # change node
            if i%2==0:
                p = prev.left
                p.right = t
                prev = p
            else:
                p = prev.right
                p.left = t
            tmp_i = f
    
    s = Solution()
    ans = s.maxDepth(root=root)
    print(ans)