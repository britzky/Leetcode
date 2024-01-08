class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1
            if t[i] not in count:
                count[t[i]] = -1
            else:
                count[t[i]] -= 1
        for value in count.values():
            print(value)
            if value != 0:
                return False
        return True

