# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from collections import deque


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Binary Search Treeかどうかを判定する。
        BSTの定義として
        「左の部分木の要素は全てその木のroot.valの値よりも小さくなくてはいけない」
        「右の部分木の要素は全てその木のroot.valの値よりも大きくなくてはいけない」
        
        そのため単純にn.val > n.left.val などで比較してるだけではダメ。
        １つ上の階層のvalをupperやlowerとしてそれぞれ定義し、それと比較を行う。
        """
        if root is None:
            return True
        q = deque()
        q.append((root, float('-inf'), float('inf')))
        
        while q:
            n,lower,upper = q.popleft()
            if n is None:
                continue
            if not lower < n.val < upper:
                return False
            q.append((n.left, lower, n.val))
            q.append((n.right, n.val, upper))
        return True





# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=TreeNode(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=TreeNode(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=TreeNode(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == "__main__":
    # inp = "2 1 3"
    #inp = "5 1 4 N N 3 6"
    inp = "10 5 15 N N 6 20"
    root = buildTree(inp)
    s = Solution()
    print(s.isValidBST(root=root))