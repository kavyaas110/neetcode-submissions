class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0
        else:
            mid = len(nums)//2
            mid_value = nums[mid]

            if target == mid_value:
                return mid
            elif (nums[0]<nums[mid] and target > nums[0]) or (nums[0]>nums[mid] and target<nums[0]):
                if target<mid_value:
                    return self.search(nums[:mid],target)
                else:
                    if mid+1 == len(nums):
                        return -1
                    else:
                        val = self.search(nums[mid+1:],target)
                        if val == -1:
                            return -1
                        else:
                            return mid+1+val
            elif nums[0]<nums[mid] and target<nums[0]:
                if mid+1 == len(nums):
                    return -1
                else:
                    val = self.search(nums[mid+1:],target)
                    if val == -1:
                        return -1
                    else:
                        return mid+1+val
            elif nums[0] > nums[mid] and target > nums[0]:
                return self.search(nums[:mid],target)
            else:
                return 0