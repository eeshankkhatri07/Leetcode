from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts=Counter(nums)
        if any(count>1 for count in counts.values()):
            return True
        else:
            return False
        