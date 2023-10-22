class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_map = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in char_map:
                char_map[s[i]] += 1
            else: 
                char_map[s[i]] = 1
            if t[i] in char_map:
                char_map[t[i]] -= 1
            else: 
                char_map[t[i]] = -1
        values = char_map.values()

        for i in range(len(values)):
            if values[i] != 0:
                return False
        return True