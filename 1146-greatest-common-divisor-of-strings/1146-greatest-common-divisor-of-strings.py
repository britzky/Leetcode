class Solution(object):
    def gcd(self, a, b):
        if a % b == 0:
            return b
        return self.gcd(b, a % b)
    def gcdOfStrings(self, str1, str2):
        gcd = self.gcd(len(str1), len(str2))
        gcd_string = str1[0:gcd]
        
        for i in range(0, len(str1), gcd):
            sub = str1[i: i + gcd]
            print(sub)
            if sub != gcd_string:
                return ""
        for i in range(0, len(str2), gcd):
            sub = str2[i:i + gcd]
            if sub != gcd_string:
                return ""
        return gcd_string

    
        