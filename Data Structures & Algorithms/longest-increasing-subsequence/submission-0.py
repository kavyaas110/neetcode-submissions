class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s = [1 for _ in nums]
        
        for index, num in enumerate(nums):
            for j in range(index):
                if nums[j] < num:
                    s[index] = max(s[j]+1,s[index])
        
        max_val = max(s)
        return max_val



        