class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        print(nums)
        for index, value in enumerate(nums):
            if index > 0 and nums[index - 1] == value:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                three_sum = value + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    print(three_sum, 'yes', [value, nums[l], nums[r]])
                    result.append([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result


