class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber > 0:
            columnNumber -= 1   # adjust for 1-based indexing
            result = chr(ord('A') + (columnNumber % 26)) + result
            columnNumber //= 26
        return result
