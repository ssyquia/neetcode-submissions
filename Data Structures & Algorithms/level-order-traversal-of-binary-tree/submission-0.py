# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # create a queue for bfs
        queue = deque()
        queue.append(root)
        # output list 
        res = []
        # while there is a queue
        while len(queue) > 0:
            # iterate through the lnegth of the queue
            level = []
            for i in range(len(queue)):
                # add children of the nodes
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(level)
       
        # return output 
        return res
