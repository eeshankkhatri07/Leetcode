from functools import reduce

class Solution(object):
    def productExceptSelf(self, nums):
        zero_count = nums.count(0)
        product = []

        if zero_count > 1:
            return [0] * len(nums)
        
        elif zero_count == 1:
            total_product = reduce(lambda x, y: x * y, [num for num in nums if num != 0])
            for num in nums:
                if num == 0:
                    product.append(total_product)
                else:
                    product.append(0)
        else:
            total_product = reduce(lambda x, y: x * y, nums)
            for num in nums:
                product.append(total_product // num)

        return product

        