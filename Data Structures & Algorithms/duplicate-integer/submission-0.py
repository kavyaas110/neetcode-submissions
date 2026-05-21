class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_duplicate = {}
        for num in nums:
            check_duplicate[num] = False
        for num in nums:
            if check_duplicate[num] == False:
                check_duplicate[num] = True
            else:
                return True
        return False
        