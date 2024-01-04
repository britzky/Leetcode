class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            sorted_string = ''.join(sorted(string))
            anagrams[sorted_string].append(string)
        return anagrams.values()
