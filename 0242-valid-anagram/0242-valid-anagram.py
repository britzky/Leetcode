class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        char_map = {}
        
        for i in range(len(s)):
            if s[i] in char_map:
                char_map[s[i]] += 1
            else:
                char_map[s[i]] = 1
            if t[i] in char_map:
                char_map[t[i]] -= 1
            else:
                char_map[t[i]] = -1 
        
        for value in char_map.values():
            if value != 0:
                return False
        return True