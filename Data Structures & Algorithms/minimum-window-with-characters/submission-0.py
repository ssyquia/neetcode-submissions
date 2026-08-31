class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "" or len(t) > len(s):
            return ""
        
        
        # hash table to store the frequencies of t
        freqT = {}
        freqS = {}
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1
        
        have = 0
        need = len(freqT) #unique characters in frq
        min_window = [-1,-1]
        min_len = float("infinity")
        
        l = 0
        # the output always starts with some letter from 
        for r, c in enumerate(s):
            freqS[c] = freqS.get(c, 0) + 1
            if c in freqT and freqT[c] == freqS[c]:
                have += 1

            while have == need:
                if(r - l + 1) < min_len:
                    min_window = [l, r]
                    min_len = r - l + 1
                
                freqS[s[l]] -= 1
                if s[l] in freqT and freqS[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1
        l, r = min_window
        return s[l:r+1] if min_len != float("infinity") else ""



