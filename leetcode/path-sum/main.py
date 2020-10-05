# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    BSTに与えられたsumを含むかどうか。ただしBSTの最後の層まで遡って含むか判断する。
    つまり木構造の途中でsumを満たしていてもそれはfalseとする。
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        sum = sum - root.val
        # check has path sum
        if sum == 0 and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root=root.left, sum=sum) \
            or self.hasPathSum(root=root.right, sum=sum)


from collections import deque
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
    inp = "1 2"
    sum = 1
    root = buildTree(inp)
    s = Solution()
    print(s.hasPathSum(root=root, sum=sum))