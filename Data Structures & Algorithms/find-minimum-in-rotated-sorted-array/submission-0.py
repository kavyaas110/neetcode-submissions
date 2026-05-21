class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums)//2
        # print(len(nums),mid)
        min_val = nums[mid]
        # print(min_val)
        if mid+1<len(nums) and min_val<nums[mid+1] and min_val < nums[mid-1]:
            # print("In if")
            return min_val;
        else:
            # print("In else")
            right_min = self.findMin(nums[:mid]) if mid>0 else None
            left_min = self.findMin(nums[mid+1:]) if mid+1<len(nums) else None
            # print(right_min,left_min)
            if right_min == None and left_min == None:
                return min_val
            elif right_min == None:
                return min(min_val,left_min)
            elif left_min == None:
                return min(min_val,right_min)
            else:
                return min(min_val,left_min,right_min)