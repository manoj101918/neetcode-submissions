class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        mapp={1:intervals[0].end}
        room=1
        for i in range(1,len(intervals)):
            found=False
            for room in mapp:
                if intervals[i].start>=mapp[room]:
                    mapp[room]=intervals[i].end
                    found=True
                    break
            if not found:
                room+=1
                mapp[room]=intervals[i].end
        return len(mapp)

        