class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)
        return self.binary_search(nums,target,0,right)

    def binary_search(self, nums, target, left, right):
        if (right-left) == 1:
            if nums[left] != target:
                return -1
            else:
                return left
        else:
            mid = left + (right-left)//2
            mid_value = nums[mid]

            if target == mid_value:
                return mid
            elif (nums[0]<nums[mid] and target > nums[0]) or (nums[0]>nums[mid] and target<nums[0]):
                if target<mid_value:
                    return self.binary_search(nums,target,left,mid)
                else:
                    if mid+1 >= right:
                        return -1
                    else:
                        return self.binary_search(nums,target,mid+1,right)
                        # if val == -1:
                        #     return -1
                        # else:
                        #     return mid+1+val
            elif nums[0]<nums[mid] and target<nums[0]:
                if mid+1 >= right:
                    return -1
                else:
                    return self.binary_search(nums,target,mid+1,right)
                    # if val == -1:
                    #     return -1
                    # else:
                    #     return mid+1+val
            elif nums[0] > nums[mid] and target > nums[0]:
                return self.binary_search(nums, target, left, mid)
            elif target == nums[0]:
                return 0
            else:
                return -1
