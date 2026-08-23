class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        curr_palindrome_size_highest = 0
        curr_palindrome_highest = ""

        for center in range(length-1,-1,-1):
            # for odd length palindromes
            p_len = 1
            if p_len > curr_palindrome_size_highest:
                curr_palindrome_highest = s[center]
                curr_palindrome_size_highest = p_len
            j=1
            if (center-j) >= 0 and (center + j) < length:
                while s[center-j] == s[center+j]:
                    p_len +=2
                    if p_len > curr_palindrome_size_highest:
                        curr_palindrome_highest = s[center-j:center+j+1]
                        curr_palindrome_size_highest = p_len
                    j+=1
                    if (center-j) < 0 or (center + j) >= length:
                        break

            # for even length palindromes
            p_len = 0
            j=1
            if (center-j)>=0 and (center+j-1)<length:
                while s[center-j] == s[center+j-1]:
                    p_len +=2
                    if p_len > curr_palindrome_size_highest:
                        curr_palindrome_highest = s[center-j:center+j]
                        curr_palindrome_size_highest = p_len
                    j+=1
                    if center-j < 0 or center + j -1 >= length:
                        break
            
            



        # for len_size in range(1,length+1):
        #     for i in range(0,length-len_size+1):
        #         sub_s = s[i:i+len_size]
        #         if self.isPalindrome(sub_s):
        #             if len(sub_s) > curr_palindrome_size_highest:
        #                 curr_palindrome_size_highest = len(sub_s)
        #                 curr_palindrome_highest = sub_s
        
        return curr_palindrome_highest

    

    def isPalindrome(self,s):
        s_rev = s[::-1]
        if s == s_rev:
            return True
        else:
            return False
        