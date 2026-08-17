class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Options: Take it, you cannot take the next one
        Not take it , explore both possibilities of taking and not taking the next one
        """
        amnt = []
        amnt.append(0)
        amnt.append(nums[0])
        for i in range(1,len(nums)):
            amnt.append(max(amnt[(i+1)-1], amnt[(i+1)-2] + nums[i]))
        
        # print(amnt)
        ans = amnt[0]
        for i in range(1,len(amnt)):
            if amnt[i] > ans:
                ans = amnt[i]
        
        return ans
