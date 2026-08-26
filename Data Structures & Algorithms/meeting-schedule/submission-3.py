"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    
        sorted_intervals = self.mergeSort(intervals)
        # for interval in sorted_intervals:
        #     print(interval.start,interval.end)
        for i,interval in enumerate(sorted_intervals[1:]):
            if interval.start < sorted_intervals[i].end:
                # print(interval.start,intervals[i].end)
                return False
        
        return True
    
    def mergeSort(self, intervals):
        if len(intervals) <= 1:
            return intervals
        mid = (len(intervals)//2)
        return self.merge(self.mergeSort(intervals[:mid]),self.mergeSort(intervals[mid:]))

    def merge(self, interval1, interval2):
        sorted_interval = []
        i = 0
        j = 0
        # print(interval1,interval2)
        while i < len(interval1) and j < len(interval2):
            if interval1[i].start <= interval2[j].start:
                sorted_interval.append(interval1[i])
                i+=1
            else:
                sorted_interval.append(interval2[j])
                j+=1
        if i < len(interval1):
            sorted_interval.extend(interval1[i:])
        
        if j < len(interval2):
            sorted_interval.extend(interval2[j:])
        
        return sorted_interval