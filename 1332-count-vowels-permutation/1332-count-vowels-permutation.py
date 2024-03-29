class Solution(object):
    def countVowelPermutation(self, n):
        mod = (10**9) + 7
        
        # initialize counts for the all vowels for n = 1
        a, e, i, o, u = 1, 1, 1, 1, 1

        #Update counts based on transitions
        for _ in range(1, n):
            a_next = e
            e_next = (a + i) % mod
            i_next = (a + e + o + u) % mod
            o_next = (i + u) % mod
            u_next = a
        
            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next

        return (a + e + i + o + u ) % mod