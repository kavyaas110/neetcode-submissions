class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]
        suffix_prod = [1]
        running_prod_pre = 1
        running_prod_suf = 1

        for i in range(len(nums)-1):
            running_prod_pre *= nums[i]
            prefix_prod.append(running_prod_pre)
        
        for i in range(len(nums)-1,0,-1):
            running_prod_suf *= nums[i]
            suffix_prod.insert(0,running_prod_suf)

        print(prefix_prod)
        print(suffix_prod)
        
        output = []
        for i in range(len(nums)):
            output.append(prefix_prod[i]*suffix_prod[i])

        return output

        


