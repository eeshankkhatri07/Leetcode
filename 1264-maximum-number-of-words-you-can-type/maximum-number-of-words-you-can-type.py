class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        lst = text.split(' ')
        l = len(lst)
        for word in lst:
            for ch in word:
                if ch in brokenLetters:
                    l -= 1
                    break   
        return l
