class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_max = nums[0]
        overall_max = nums[0]
        curr_max = nums[0]
        for i, num in enumerate(nums[1:]):
            curr_sum = prev_max + num
            curr_max = max(curr_sum,num)
            if curr_max > overall_max:
                overall_max = curr_max
            prev_max = curr_max
        
        return overall_max



        