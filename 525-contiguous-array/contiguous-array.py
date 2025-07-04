class Solution(object):
    def findMaxLength(self, nums):
        zcount = 0
        ocount = 0
        counts = {}
        max_len = 0
        counts[0] = -1 

        for i in range(len(nums)):
            if nums[i] == 0:
                zcount += 1
            else:
                ocount += 1

            diff = ocount - zcount

            if diff in counts:
                max_len = max(max_len, i - counts[diff])
            else:
                counts[diff] = i

        return max_len

            
