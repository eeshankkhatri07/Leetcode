class Solution(object):
    def countSubstrings(self, s):
        def expandAroundCenter(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total = 0
        for center in range(len(s)):
            total += expandAroundCenter(center, center)
            total += expandAroundCenter(center, center + 1)
        return total


        