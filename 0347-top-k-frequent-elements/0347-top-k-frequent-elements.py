class Solution(object):
    def topKFrequent(self, nums, k):
        m = {}
        r = []
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1

        for j in range(k):
            max_freq = 0
            max_freq_num = 0
            for key, value in m.items():
                if value > max_freq:
                    max_freq = value
                    max_freq_num = key
            r.append(max_freq_num)
            m.pop(max_freq_num)

        return r
    




        