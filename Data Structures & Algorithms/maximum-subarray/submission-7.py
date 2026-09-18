class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        overall_max = curr_max = nums[0]
        for num in nums[1:]:
            curr_max = max(curr_max + num,num)
            overall_max = max(overall_max,curr_max)
        
        return overall_max



        