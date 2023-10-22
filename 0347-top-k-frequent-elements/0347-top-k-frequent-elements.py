class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # initialize a count hashmap 
        # make an empty list the length of nums
        # loop through nums and count each element
        n = len(nums)
        frequency = [[] for _ in range(n + 1)]
        count = {}
        result = []

        for num in nums:
            count[num] = count.get(num, 0) + 1 

        for key, value in count.items():
            frequency[value].append(key)

        for i in range(n, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result

    




        