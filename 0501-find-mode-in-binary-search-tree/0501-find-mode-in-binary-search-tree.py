# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        #initlaize a counter hashmap that takes int
        counter = defaultdict(int)
        # initialize a function that takes a node and the counter hashmap
        def dfs(node, counter):
            # if the node is empty exit the function
            if not node:
                return

            # otherwise count the value in the the node in our hashmap
            counter[node.val] += 1
            # call dfs on both children
            dfs(node.left, counter)
            dfs(node.right, counter)
        # call dfs on the root and counter
        dfs(root, counter)
        #initialize a variable for the maximum appearances of a number
        max_freq = max(counter.values())

        # initalize a variable for an empty list that we can return
        result = []
        # loop through the keys in the hashmap and check if their value is equal to the max_freq
        for key in counter:
            if counter[key] == max_freq:
                result.append(key)
        return result
        


        