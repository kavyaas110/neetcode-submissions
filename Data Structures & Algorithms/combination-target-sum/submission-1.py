class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.dfs(nums, [], [], target, 0)
    
    def dfs(self,nums,curr_list,numcomb_list,target,curr_sum):
        if curr_sum > target:
            return numcomb_list
        elif curr_sum == target:
            numcomb_list.append(curr_list)
            return numcomb_list
        else:
            for i in range(len(nums)):
                new_list = curr_list.copy()
                new_list.append(nums[i])
                sum_new_list = curr_sum + nums[i]
                numcomb_list = self.dfs(nums[i:], new_list, numcomb_list, target, sum_new_list)
            return numcomb_list   