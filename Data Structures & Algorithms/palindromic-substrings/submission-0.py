class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        len_s = len(s)
        for len_sub in range(1,len_s+1):
            for start in range(len_s):
                end = start + len_sub
                if end <= len_s:
                    if self.is_palindrome(s[start:end]):
                        ans += 1
        return ans
    
    def is_palindrome(self,sub_s):
        rev_s = sub_s[::-1]
        if rev_s == sub_s:
            return True
        else:
            return False
        