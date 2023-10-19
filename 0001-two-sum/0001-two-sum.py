class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # initalize a result list
        # initialize a hashmap 
        # loop through nums
        # initialize a variable for the needed_value which would be target - current index value
        # check if the needed_value is in the hashmap
        # if it is the needed value then append the key of the number from the dictionary 
        # append the current index to the result list
        # if it isn't the needed value then add the index as the key and the number as the value
        # return the result list

        result = []
        hash_map = {}
        for i in range(len(nums)):
            needed_value = target - nums[i]    
            if needed_value in hash_map:
                result.append(hash_map[needed_value])
                result.append(i)
            else:
                hash_map[nums[i]] = i
        return result