class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, value in count.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq) -1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        