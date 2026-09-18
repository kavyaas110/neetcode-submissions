class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]
        print(sorted_intervals)
        for interval in sorted_intervals[1:]:
            if interval[0]<end:
                end = min(interval[1],end)
                remove += 1
            else:
                end = interval[1]
        
        return remove


        