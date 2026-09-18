class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0
        intervals.sort()
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0]<end:
                end = min(interval[1],end)
                remove += 1
            else:
                end = interval[1]
        return remove        