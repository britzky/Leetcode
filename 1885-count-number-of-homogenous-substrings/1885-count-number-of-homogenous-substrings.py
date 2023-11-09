class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = (10 ** 9) + 7
        result = 0
        streak = 0

        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                streak += 1
            else:
                streak = 1
            result = (result + streak) % mod
        return result