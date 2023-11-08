class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        width = abs(sx - fx)
        height = abs(sy - fy)
        if width == 0 and height == 0 and t == 1:
            return False
        return t >= max(width, height)
        