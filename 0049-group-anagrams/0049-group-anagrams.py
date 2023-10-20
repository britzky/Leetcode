class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list) # map charCount to list of anagrams
        print(result)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            result[tuple(count)].append(s)
        return result.values()



            
        