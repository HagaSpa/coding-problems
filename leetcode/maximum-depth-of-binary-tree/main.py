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
    """
    FIXME: invalid data structure in TreeNode.
    """
    for i,t in enumerate(tree[1:]):
        tn = TreeNode(val=t)
        if i%2==0: # even
            p.left = tn
        else:
            p.right = tn
            if i%2==0:
                p = p.left
            else:
                p = p.right
    # debug TreeNode
    traverse(root)