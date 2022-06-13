class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        
        intervals.sort()
        
        for interval in range(len(intervals) - 1):
            if intervals[interval][1] > intervals[interval+1][0]:
                return False
        
        return True