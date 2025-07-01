class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        current = []

        for char in s:
            if char in current:
                index = current.index(char)
                current = current[index + 1:]
            current.append(char)
            longest = max(longest, len(current))
        
        return longest


        
        