class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        dp = self.dfs(nums,dp,0,len(nums)-1)
        return dp[0]
    
    def dfs(self,nums,dp,index,end):
        curr_jump = nums[index]
        if index in dp:
            return dp
        if curr_jump == 0 and index != end:
            dp[index] = False
            return dp
        if index == end:
            dp[index] = True
            return dp
        result = False
        for i in range(1,min(curr_jump+1,end-index+1)):
            dp = self.dfs(nums,dp,index+i,end)
            result = result or dp[index+i]
        dp[index] = result
        return dp

        