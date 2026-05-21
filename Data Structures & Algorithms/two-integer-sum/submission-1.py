class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hashmap = {val:index for index,val in enumerate(nums)}
        for i,val in enumerate(nums):
            find_val = target - val
            print(find_val)
            if find_val in my_hashmap:
                j = my_hashmap[find_val]
                if i != j:
                    return [i,j] if i<j else [j,i]

        