class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        # initialize a variable to prevent integer overflow issues
        mod = int(1e9 + 7)
        #sort the array in ascending order
        arr.sort()
        #initialize a variable to hold the number of binart trees
        total = 0
        # initialize a hashmap to store the ways to form a binary tree for each element
        # the key is the element and the value is the number
        tree_map = {}

        # loop through the sorted array
        for num in arr:
            # initialize a ways variable to 1
            ways = 1
            # intialize a max value variable
            max_value = int(num ** 0.5)

            # intialize a counter vairable
            count = 0
            # intialize a variable for left node
            left = arr[0]
            while left <= max_value:
                if num % left != 0:
                    count += 1
                    left = arr[count]
                    continue
                right = num // left
                if right in tree_map:
                    ways = (ways + tree_map[left] * tree_map[right] * (1 if left == right else 2)) % mod
                count += 1
                left = arr[count]
            tree_map[num] = ways
            total = (total + ways) % mod
        return total




