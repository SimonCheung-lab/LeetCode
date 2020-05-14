import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]

        first = [x[0] for x in intervals]
        second = [x[1] for x in intervals]

        i = bisect.bisect_left(first, newInterval[0])
        j = bisect.bisect_left(second, newInterval[1])

        left, mid, right = [], [], []
        if i - 1 > 0:
            left = intervals[:i - 1]
        if j + 1 < n:
            right = intervals[j + 1:]

        if i > 0:
            if newInterval[0] <= intervals[i - 1][1]:
                newInterval[0] = intervals[i - 1][0]
            else:
                mid += [intervals[i - 1]]
        
        if j < n:
            if newInterval[1] < intervals[j][0]:
                right = [intervals[j]] + right
            else:
                newInterval[1] = intervals[j][1]
        
        mid += [newInterval]

        ans = []
        if len(left):
            ans += left
        
        ans = ans + mid

        if len(right):
            ans += right

        return ans
