class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = len(set([ch for ch in s]))
        found = False
        while(unique_chars>1):
            for i in range(0,len(s)):
                if len(set(s[i:i+unique_chars])) == unique_chars:
                    found = True
                    break
            if found:
                break
            else:
                unique_chars -= 1
        
        return unique_chars
                

        