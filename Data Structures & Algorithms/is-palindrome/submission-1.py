class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join([ch.lower() for ch in s if ch.isalnum()])

        start = 0
        end = -1

        print(clean_str)

        for pos in range(len(clean_str)//2):
            if clean_str[start] == clean_str[end]:
                start+=1
                end-=1
            else:
                return False
        
        return True