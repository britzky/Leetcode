# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.matchingSubtreeCount = 0 # intialize the count of subtrees with matchin averages

    # Initialize a DFS function that returns a tuple of two values
    # - The sum of the values within the current subtree
    # - the number of nodes within the current subtree
    def calculateSubtreeValues(self, currentNode):
        # Initialize a base case:
        # Return 0 for both sum and number of nodes if the node is None
        if currentNode is None:
            return 0, 0 

        # Recursively calculate values foor the left and right subtrees
        leftSubtree = self.calculateSubtreeValues(currentNode.left)
        rightSubtree = self.calculateSubtreeValues(currentNode.right)

        # Calculate the sum of values and the number of nodes in the current subtree
        sumOfValues = leftSubtree [0] + rightSubtree[0] + currentNode.val
        numberOfNodes = leftSubtree [1] + rightSubtree[1] + 1

        # Check if the current node's value matches the average of its subtree.
        if numberOfNodes != 0 and sumOfValues // numberOfNodes == currentNode.val:
            self.matchingSubtreeCount += 1
        
        # return the calculated values for the current subtree
        return sumOfValues, numberOfNodes

    def averageOfSubtree(self, root):
        # Start the DFS from the root node
        self.calculateSubtreeValues(root)
        return self.matchingSubtreeCount

        