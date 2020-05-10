class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for i in intervals:
            if len(result) == 0:
                result.append(i)
            else:
                if i[0] <= result[-1][1]:
                    # can merge
                    result[-1] = [result[-1][0], max(result[-1][1], i[1])]
                else:
                    result.append(i)
        return result
