class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_min = nums[0]
        curr_max = nums[0]

        for num in nums[1:]:
            old_min = curr_min
            old_max = curr_max

            curr_max = max(num, num*old_max, num*old_min)
            curr_min = min(num, num*old_max, num*old_min)

            ans = max(ans,curr_max)
        
        return ans

