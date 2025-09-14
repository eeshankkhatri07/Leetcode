class Solution:
    def spellchecker(self, wordList: List[str], queries: List[str]) -> List[str]:
        vowels=set("aeiou")
        def devowel(word:str)->str:
            return "".join('*'if c in vowels else c for c in word )
        word_set=set(wordList)
        case_map={}
        vowel_map={}
        for word in wordList:
            lower=word.lower()
            dev=devowel(lower)
            if lower not in case_map:
                case_map[lower]=word
            if dev not in vowel_map:
                vowel_map[dev]=word
        res=[]
        for q in queries :
            if q in word_set:
                res.append(q)
            elif q.lower() in case_map:
                res.append(case_map[q.lower()])
            elif devowel(q.lower()) in vowel_map:
                res.append(vowel_map[devowel(q.lower())])
            else:
                res.append("")
        return res