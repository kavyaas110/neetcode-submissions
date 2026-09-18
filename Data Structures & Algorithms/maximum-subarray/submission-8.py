class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        overall_max = curr_max = nums[0]
        for i in range(1,len(nums)):
            curr_max = max(curr_max + nums[i],nums[i])
            overall_max = max(overall_max,curr_max)
        
        return overall_max



        