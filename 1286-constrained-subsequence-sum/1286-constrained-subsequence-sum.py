class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = deque() # store indicies and their correspondiding total sums
        res = float('-inf') # set to negative infinity
        
        # loop through nums using enumerate
        for i, num in enumerate(nums):
            if q:
                total = num + q[0][1] # num + the first index in the deque
            else:
                total = num
            
            res = max(res, total) # keep track of the maximum total sum seen so far

            while q and total >= q[-1][1]: # if q exists and total is greater than or equal to the last element in the deque then pop it
                q.pop()
                
            if total > 0:
                q.append((i, total))
                
            if q and q[0][0] == i - k:
                q.popleft()
            
        return res
        