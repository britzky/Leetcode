class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        values = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if nums[i] in values:
                res.append(i)
                res.append(values[nums[i]])
            else:
                values[compliment] = i
        return res

        