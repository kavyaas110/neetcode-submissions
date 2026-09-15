class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) > 0:
            return self.helper(wordDict,s, 0, {})
        else:
            if "" in wordDict:
                return True
            else:
                return False
    
    def helper(self, wordDict, s, index, dp):
        if index in dp:
            return dp[index]
        print(wordDict)
        result = False
        if index == len(s):
            return True
        else:
            for word in wordDict:
                if s[index:len(word)+index] == word:
                    dp[index] = self.helper(wordDict,s,index+len(word),dp)
                    if dp[index]:
                        return dp[index]      
            return result