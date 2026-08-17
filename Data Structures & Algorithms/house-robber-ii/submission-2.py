class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        else:
            val1 = self.helper_rob(nums[:len(nums)-1])
            val2 = self.helper_rob(nums[1:])
            return max(val1,val2)
    
    def helper_rob(self, nums):
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
        
        
        