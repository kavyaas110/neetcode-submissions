class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        len_s = len(s)
        for center in range(len_s):
            #odd length
            j = 1
            ans +=1
            start = center - j
            end = center + j
            if start >=0 and end < len_s:
                while s[start] == s[end]:
                    ans += 1
                    j += 1
                    start = center - j
                    end = center + j
                    if start < 0 or end >= len_s:
                        break
            
            # even length
            j = 1
            start = center
            end = center + j
            if start >=0 and end < len_s:
                while s[start] == s[end]:
                    ans += 1
                    j += 1
                    start = center - j + 1
                    end = center + j
                    if start < 0 or end >= len_s:
                        break

        return ans
    
    
        