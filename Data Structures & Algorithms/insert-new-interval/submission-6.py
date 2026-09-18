class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        if len(intervals) == 0:
            return [newInterval]
        is_inserted = False
        insert_index = 0
        less_index = -1
        more_index = -1
        for i,interval in enumerate(intervals):
            if interval[0] <= newInterval[0]:
                less_index = i
        
        if less_index >= 0:
            prev_start = intervals[less_index][0]
            prev_end = intervals[less_index][1]
        
        for i in range(max(less_index,0),len(intervals)):
            if newInterval[1] <= intervals[i][1]:
                more_index = i
                break

        merge_both = False
        merge_less = False
        merge_out = False
        merge_start = 0
        merge_end = 0

        if less_index >= 0 and prev_end >= newInterval[0]:
            merge_less = True
            merge_start = min(prev_start,newInterval[0])
            merge_end = max(prev_end,newInterval[1])
        
        if (merge_less and merge_end >= intervals[more_index][0]):
            merge_both = True
            merge_start = min(merge_start, intervals[more_index][0])
            merge_end = max(merge_end,intervals[more_index][1])
        
        if more_index >= 0 and not merge_less and (less_index != more_index) and newInterval[1] >= intervals[more_index][0]:
            merge_out = True
            merge_start = min(newInterval[0],intervals[more_index][0])
            merge_end = max(newInterval[1],intervals[more_index][1])
        
        if merge_both:
            ans = intervals[:less_index] + [[merge_start,merge_end]]
            if more_index >= 0:
                ans += intervals[more_index+1:]
        elif merge_less:
            ans = intervals[:less_index] + [[merge_start,merge_end]]
            if more_index >=0:
                if less_index == more_index:
                    ans += intervals[more_index+1:]
                else:
                    ans += intervals[more_index:]
        elif merge_out:
            ans = intervals[:less_index+1] + [[merge_start,merge_end]] + intervals[more_index+1:]
        else:
            ans = intervals[:less_index+1] + [newInterval]
            if more_index >= 0:
                if less_index == more_index:
                    ans += intervals[more_index+1:]
                else:
                    ans += intervals[more_index:]
        
        return ans