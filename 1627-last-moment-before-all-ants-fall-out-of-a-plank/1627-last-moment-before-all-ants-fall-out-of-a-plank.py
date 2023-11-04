class Solution(object):
    def getLastMoment(self, n, left, right):
        result = 0

        for num in left:
                result = max(result, num)
        for num in right:
                result = max(result, n - num)

        return result
        