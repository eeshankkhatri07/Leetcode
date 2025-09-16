import math
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            f, s = nums[i], nums[i + 1]
            g = math.gcd(f, s)
            if g > 1:
                nums[i] = math.lcm(f, s)  # merge into LCM
                nums.pop(i + 1)           # remove the next one
                if i > 0:                 # step back to check with previous
                    i -= 1
            else:
                i += 1
        return nums
