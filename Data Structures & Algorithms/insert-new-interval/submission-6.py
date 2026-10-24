class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        if not len(intervals): 
            return [newInterval]
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            i+=1
        mergeBefore = -1
        if newInterval[0] < intervals[i-1][1]:
            #merge before
            mergeBefore = i-1
        mergeAfter = -1
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            i+=1
            mergeAfter = i-1
        if mergeBefore == -1 and mergeAfter == -1:
            intervals.insert(i, newInterval)
        elif mergeBefore != -1 and mergeAfter == -1:
            intervals[mergeBefore] = [intervals[mergeBefore][0], max(newInterval[1], intervals[mergeBefore][1])]
        elif mergeBefore == -1 and mergeAfter != -1:
            intervals.insert(i, [newInterval[0], max(intervals[mergeAfter][1], newInterval[1])])
            del intervals[i+1:i]
        else:
            intervals[mergeBefore] = [intervals[mergeBefore][0], intervals[mergeAfter][1]]
            del intervals[mergeBefore+1:i]
        return intervals
