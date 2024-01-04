class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        values = {}
        for i in range(len(nums)):
            needed_value = target - nums[i]
            if nums[i] in values:
                result.append(i)
                result.append(values[nums[i]])
            else:
                values[needed_value] = i
        return result

        