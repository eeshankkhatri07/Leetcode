class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        str1 = ['a']
        while len(str1) < k:
            new_str = []
            for i in str1:
                if i == 'z':
                    new_str.append('a')
                else:
                    new_str.append(chr(ord(i) + 1))
            str1.extend(new_str)
        return str1[k - 1]

