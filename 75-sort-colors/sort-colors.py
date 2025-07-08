class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        count0 = nums.count(0)
        count1 = nums.count(1)
        count2 = nums.count(2)

        # Clear original list and rebuild it
        nums[:] = [0] * count0 + [1] * count1 + [2] * count2

        