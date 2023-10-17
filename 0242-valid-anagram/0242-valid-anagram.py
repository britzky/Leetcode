class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # check if the strings are the same length
        if len(s) != len(t):
            return False
        
        # initialize a hashmap to count the letters
        # loop through s and count each letter in the hashmap
        char_count = {}
        for i in range(len(s)):
            if s[i] not in char_count:
                char_count[s[i]] = 1
            else:
                char_count[s[i]] += 1
            # if the index of t is in char_count subtract 1 
            if t[i] not in char_count:
                char_count[t[i]] = -1
            else:
                char_count[t[i]] -= 1
        #return True if the values of char_count = 0 and False otherwise
        for value in char_count.values():
            if value != 0:
                return False
        return True      

        