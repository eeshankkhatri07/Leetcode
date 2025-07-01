class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_count=0
        freq={}
        left=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            max_count=max(max_count,freq[s[right]])
            if right-left+1 - max_count >k:
                freq[s[left]]-=1
                left+=1
        return len(s)-left