class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numz = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numz:
                length = 0
                while num + length in numz:
                    length += 1
                longest = max(longest, length)
        return longest

        
        