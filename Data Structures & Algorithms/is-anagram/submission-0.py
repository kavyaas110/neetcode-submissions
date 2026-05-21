class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}

        for val in s:
            if val in freq_s:
                freq_s[val] += 1
            else:
                freq_s[val] = 1
        
        for val in t:
            if val in freq_t:
                freq_t[val] += 1
            else:
                freq_t[val] = 1

        for key in freq_s:
            if (key in freq_t) and (freq_t[key] == freq_s[key]):
                continue
            else:
                return False
        
        for key in freq_t:
            if (key in freq_s) and (freq_t[key] == freq_s[key]):
                continue
            else:
                return False

        return True
        

        