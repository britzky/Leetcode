class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_list = []
        vowel_positions = []

        for index, char in enumerate(s):
            if char.lower() in {'a', 'e', 'i', 'o', 'u'}:                
                vowels_list.append(char)
                vowel_positions.append(index)
        
        vowels_list.sort()
        result_list = list(s)
        
        for position, vowel in zip(vowel_positions, vowels_list):
            result_list[position] = vowel

        return ''.join(result_list)