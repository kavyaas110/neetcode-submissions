class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest_overall = 0

        for num in my_set:
            if num-1 not in my_set:
                longest_so_far = 1
                while num+1 in my_set:
                    longest_so_far += 1
                    num += 1
                longest_overall = max(longest_overall, longest_so_far)
        return longest_overall




        
            

        



        
        