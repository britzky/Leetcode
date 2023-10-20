# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # The list of NestedInteger elementes to be flattened
        self.nestedList = nestedList
        
        # The flattened list of integers
        self.flattenedList = []

        # Index to keep track of the current position in the flattenedList
        self.currentIndex = 0

        # Recurssive function that flattens nested lists and adds integers to the flattenedList  
        def flatten(current_list):
            for i in current_list:
                if i.isInteger():
                    self.flattenedList.append(i.getInteger())
                else:
                    flatten(i.getList())
        # Flatten the nestedList during initialization
        flatten(self.nestedList)

    # Returns the next integer in the flattened list
    def next(self):
        """
        :rtype: int
        """
        number = self.flattenedList[self.currentIndex]
        self.currentIndex += 1
        return number  

    # Checks if there are more integers in the flattened list
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.currentIndex < len(self.flattenedList)

        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())