class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # initialize a result array
        # intialize a variable to store max_candies
        # loop through candies
        # check if the current index + extraCandies is greater than max_candies
        # if the current index is >= max_candies
        # append True to the result list
        # if it is < max_candies 
        # append False to the result list
        # return the result list

        result = []
        max_candies = max(candies)
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
        