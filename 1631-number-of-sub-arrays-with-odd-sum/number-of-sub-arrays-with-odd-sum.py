class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        odd = 0
        even = 1  # prefix sum of 0 is even
        prefix = 0
        count = 0

        for num in arr:
            prefix += num
            if prefix % 2 == 0:
                count += odd
                even += 1
            else:
                count += even
                odd += 1

        return count % MOD


