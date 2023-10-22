class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left_boundary = [-1] * n
        right_boundary = [n] * n
        left_stack = []
        right_stack = []

        for i in range(n - 1, - 1, -1):
            while left_stack and nums[left_stack[-1]] > nums[i]:
                left_boundary[left_stack[-1]] = i
                left_stack.pop()
            left_stack.append(i)

        for i in range(n):
            while right_stack and nums[right_stack[-1]] > nums[i]:
                right_boundary[right_stack[-1]] = i
                right_stack.pop()
            right_stack.append(i)
        
        max_score = 0

        for i in range(n):
            if left_boundary[i] < k and right_boundary[i] > k:
                sub_array_score = nums[i] * (right_boundary[i] - left_boundary[i] - 1)
                max_score = max(max_score, sub_array_score)
        return max_score                
        