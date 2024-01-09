class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, value in enumerate(nums):
            if index > 0 and nums[index - 1] == value:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([value, nums[l], nums[r]]) 
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
                
