class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Initialize a variable to track if the values of k and the first element are the same
        equal_values = True

        # Calculate the total number of elements in the nth row - 2^(n -1)
        n= 2**(n - 1)

        # Initialize a loop that starts at the end and continues until we reach the first row
        while n != 1:
            # half the number of elements in the row
                n //= 2

                # if k is in the second half of the row, adjust k and toggle the flag
                if k > n:
                    k -= n
                    equal_values = not equal_values
        # Return 0 if the values are the same and 1 otherwise
        return 0 if equal_values else 1


            
            