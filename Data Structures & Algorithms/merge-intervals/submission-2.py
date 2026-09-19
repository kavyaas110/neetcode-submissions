class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        # print(intervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                # print("In If")
                # merge
                # print(ans[-1][0])
                ans[-1][0] = min(ans[-1][0],intervals[i][0])
                # print(ans[-1][0])
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans