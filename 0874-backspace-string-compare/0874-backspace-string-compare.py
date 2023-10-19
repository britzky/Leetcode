class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        #loop through s
        #if there is a # then remove it along with the value at the index prior to #
        
        #loop through t
        #if there is a # then remove it along with the value at the indiex prior to #

        #If new_s = new_t return true othereiwse return false

        s_list = []
        t_list = []
        for i in range(len(s)):
            if s[i] != "#":
                s_list.append(s[i])
            if s_list and s[i] == "#":
                s_list.pop()

        for j in range(len(t)):
            if t[j] != "#":
                t_list.append(t[j])
            if t_list and t[j] == "#":
                t_list.pop()

        if s_list == t_list:
            return True
        return False


        