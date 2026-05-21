class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        triplets_set = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        curr_set = set([nums[i],nums[j],nums[k]])
                        if curr_set not in triplets_set:
                            triplets.append([nums[i],nums[j],nums[k]])
                            triplets_set.append(curr_set)
        
        return triplets