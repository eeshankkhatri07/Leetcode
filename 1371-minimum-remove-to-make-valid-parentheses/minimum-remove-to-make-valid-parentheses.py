class Solution(object):
    def minRemoveToMakeValid(self, s):
        
        s = list(s)
        st = []
        for i, e in enumerate(s):
            if e == '(':
                st.append(i)
            elif e == ')':
                if st:
                    st.pop()
                else:
                    s[i] = ''

        while st:
            s[st.pop()] = ''
        
        return ''.join(s)

    
            
        