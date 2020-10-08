# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from collections import deque
from itertools import groupby


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # empty pattern
        if root is None:
            return []

        # mapping value to level
        q = deque()
        q.append((root, 0))
        li = []
        while q:
            n,l = q.popleft()
            if n.left is not None:
                q.append((n.left, l+1))
            if n.right is not None:
                q.append((n.right, l+1))
            # {val: x, level: y}
            li.append({"val":n.val, "level":l})
        
        # group by level
        gp = groupby(li, lambda x: x["level"])
        ans = []
        for key, group in gp:
            vl = [d['val'] for d in list(group)]
            if key%2==1:
                vl.reverse()
            ans.append(vl)
        return ans


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
    #inp = "3 9 20 N N 15 7"
    inp = "0 2 4 1 N 3 -1 5 1 N 6 N 8"
    root = buildTree(inp)
    s = Solution()
    print(s.zigzagLevelOrder(root=root))