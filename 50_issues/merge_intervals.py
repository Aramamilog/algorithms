from typing import List


# https://leetcode.com/problems/merge-intervals/description/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = result[-1][1]
            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])

        return result


sol = Solution()
assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert sol.merge([[1,4],[4,5]]) == [[1,5]]
assert sol.merge([[4,7],[1,4]]) == [[1,7]]
# time complexity O(logn) for the sort and O(n) for the algo
# memory complexity O(len(intervals))
