class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res=[]
        prev_start=intervals[0][0]
        prev_end=intervals[0][1]
        for i in range(1,len(intervals)):
            if prev_end>=intervals[i][0]:
                prev_end=max(prev_end,intervals[i][1])
            else:
                res.append([prev_start,prev_end])
                prev_start=intervals[i][0]
                prev_end=intervals[i][1]
        res.append([prev_start,prev_end])

        return res
        
        
        
        