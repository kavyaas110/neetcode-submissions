class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        for num in nums:
            if num not in ans:
                ans[num] = 1
            else:
                ans[num] += 1
        
        sorted_dict = dict(sorted(ans.items(), key = lambda item: item[1], reverse=True))
        return list(sorted_dict.keys())[:k]