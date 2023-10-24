# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #initlialize a result array
        result = []

        # check if the tree is empty
        if not root:
            return result
        
        #intialize an empty deque
        my_deque = deque()
        # add the root to the deque
        my_deque.append(root)

        # loop through the deque while there are nodes in it
        while my_deque:
            #initialize a max_value at negative inifinity
            max_value = float("-inf")
            #initialize a second loop that traverses the rows of the tree
            for _ in range(len(my_deque)):
                # initialize a variable for the left most node 
                node = my_deque.popleft()
                # update the max_value by comparing the current max_value with the popped node value
                max_value = max(max_value, node.val)

                #check if the current node has children.
                # if it does append the nodes to the deque
                if node.left:
                    my_deque.append(node.left)
                if node.right:
                    my_deque.append(node.right)
            #after each row iteration append the max value
            result.append(max_value)
        #when the whole deque is empty return the result array
        return result



        print(self.root[0])

        