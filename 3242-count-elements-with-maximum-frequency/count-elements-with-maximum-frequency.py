from collections import defaultdict

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)   # ✅ fix: defaultdict needs a default factory (int)
        for i in nums:
            d[i] += 1          # ✅ simplifies your if-else

        ans = []
        m = max(d.values())    # maximum frequency
        for i in d:
            if d[i] == m:      # ✅ check frequency, not element itself
                ans.append(i)

        # return total frequency of max occurring elements
        return m * len(ans)
        