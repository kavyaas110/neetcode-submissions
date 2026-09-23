class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        my_set = set(nums)

        for i in range(n+1):
            if i not in my_set:
                return i
        