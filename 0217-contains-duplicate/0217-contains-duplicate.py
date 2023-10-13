class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # initialize a dict to count the occurances of each number in nums
        # loop through nums
        # check if the current num is in the dict
        # if it is add 1 to the value
        # if not add the num to the dict
        # compare the length of the dict with the length of nums list
        # if they are different lengths return True

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 0
        if len(count) != len(nums):
            return True
        return False