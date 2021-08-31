class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_str =  ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalized_str.split()
        mp = {}
        #print(words)
        for w in words:
            if w not in banned:
                mp[w] = mp.get(w,0) + 1

        return max(mp.items(), key=operator.itemgetter(1))[0]
                    
        