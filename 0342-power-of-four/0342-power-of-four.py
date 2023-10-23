class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(16):
            power_of_four = 4 ** i
            if power_of_four == n:
                return True
            if power_of_four > n:
                return False
        return False



            
        
        
        