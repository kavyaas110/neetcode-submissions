"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) > 0:
            start_times = [interval.start for interval in intervals]
            end_times = [interval.end for interval in intervals]
            sorted_start = self.mergeSort(start_times)
            sorted_end = self.mergeSort(end_times)

            left = 0
            right = 0
            size = len(sorted_start)
            curr = 0
            number_of_rooms = 0
            while(left < size):
                if sorted_start[left] < sorted_end[right]:
                    curr += 1
                    if number_of_rooms < curr:
                        number_of_rooms = curr
                    left += 1
                else:
                    curr -= 1
                    right += 1

        else:
            number_of_rooms = 0
        
        return number_of_rooms

    
    def mergeSort(self, intervals):
        if len(intervals) == 1 or len(intervals) == 0:
            return intervals
        else:
            mid = len(intervals)//2
            return self.merge(self.mergeSort(intervals[:mid]),self.mergeSort(intervals[mid:]))
    
    def merge(self,list1, list2):
        i = 0
        j = 0
        len_l1 = len(list1)
        len_l2 = len(list2)

        combined = []

        while(i<len_l1 and j < len_l2):
            if list1[i] <= list2[j]:
                combined.append(list1[i])
                i += 1
            else:
                combined.append(list2[j])
                j += 1
        
        if i >= len_l1:
            combined.extend(list2[j:])
        else:
            combined.extend(list1[i:])
        
        return combined

        