class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # initalize a result hashmap as a default dict that holds lists as the value
        # loop through strs
        # initlialize a count array filled with 26 0's
        # loop through the chars of strs
        # insert the order of the current char - the order of 'a' into the count array
        result_map = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            result_map[tuple(count)].append(string)
        return result_map.values()
        