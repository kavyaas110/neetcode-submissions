class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        overall_max = nums[0]
        curr_max = nums[0]
        for num in nums[1:]:
            curr_sum = curr_max + num
            curr_max = max(curr_sum,num)
            overall_max = max(overall_max,curr_max)
        
        return overall_max



        