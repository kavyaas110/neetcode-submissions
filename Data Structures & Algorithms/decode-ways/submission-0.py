class Solution:
    def numDecodings(self, s: str) -> int:
        my_dict = {len(s):1}
        return self.count_recursive(0,s,my_dict)
    
    def count_recursive(self,i,s,my_dict):
        if i in my_dict:
            return my_dict[i]
        
        if s[i] == '0':
            my_dict[i] = 0
            return 0
        
        ans = self.count_recursive(i+1,s,my_dict)
        if i < len(s)-1 and (s[i] == '1' or (s[i] =='2' and s[i+1] in '0123456')):
            ans += self.count_recursive(i+2,s,my_dict)
        
        my_dict[i] = ans
        return ans



        