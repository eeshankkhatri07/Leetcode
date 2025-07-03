class Solution:
    def findMin(self, nums):
        s, e = 0, len(nums) - 1

        while s <= e:
            m = (s + e) // 2

            if s == e:
                return nums[s]

            if nums[m] >= nums[s] and nums[s] > nums[e]:
                s = m + 1
            else:
                e = m

        return -1
        