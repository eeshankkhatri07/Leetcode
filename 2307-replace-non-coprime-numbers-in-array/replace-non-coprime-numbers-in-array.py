import math
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            # keep merging while the last two numbers are not coprime
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = math.gcd(a, b)
                if g > 1:
                    stack.pop()                 # remove last
                    stack[-1] = math.lcm(a, b)  # merge into LCM
                else:
                    break
        return stack
