class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        curr_palindrome_size_highest = 0
        curr_palindrome_highest = ""
        for len_size in range(1,length+1):
            for i in range(0,length-len_size+1):
                sub_s = s[i:i+len_size]
                if self.isPalindrome(sub_s):
                    if len(sub_s) > curr_palindrome_size_highest:
                        curr_palindrome_size_highest = len(sub_s)
                        curr_palindrome_highest = sub_s
        
        return curr_palindrome_highest

    

    def isPalindrome(self,s):
        s_rev = s[::-1]
        if s == s_rev:
            return True
        else:
            return False
        