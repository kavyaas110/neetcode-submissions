class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = [nums[0]]
        for i, num in enumerate(nums[1:]):
            curr_sum = max_sum[i] + num
            final_max = max(curr_sum,num)
            max_sum.append(final_max)
        
        ans = max_sum[0]
        for num in max_sum:
            if num > ans:
                ans = num
        
        return ans



        