class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.dfs(nums, [], [], target, 0, 0)
    
    def dfs(self,nums,curr_list,numcomb_list,target,curr_sum, index):
        if index >= len(nums) or curr_sum > target:
            return numcomb_list
        elif curr_sum == target:
            numcomb_list.append(curr_list.copy())
            return numcomb_list
        else:
            curr_list.append(nums[index])
            sum_new_list = curr_sum + nums[index]
            numcomb_list = self.dfs(nums, curr_list, numcomb_list, target, sum_new_list, index)
            curr_list.pop()
            numcomb_list = self.dfs(nums,curr_list,numcomb_list, target, curr_sum, index+1)
            return numcomb_list   