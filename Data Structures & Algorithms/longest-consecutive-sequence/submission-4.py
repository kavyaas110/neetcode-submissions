class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        my_len = len(nums)
        longest_overall = 0
        starts = []
        for num in nums:
            if num-1 not in my_set:
                starts.append(num)
        
        for num in set(starts):
            j = 1
            longest_so_far = 1
            while(j<=(my_len-len(starts))):
                if num+j in my_set:
                    longest_so_far += 1
                    j+=1
                else:
                    break
            
            if longest_so_far > longest_overall:
                longest_overall = longest_so_far


        return longest_overall




        
            

        



        
        