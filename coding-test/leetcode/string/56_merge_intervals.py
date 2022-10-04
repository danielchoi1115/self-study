# https://leetcode.com/problems/merge-intervals/
# 56. Merge Intervals
import itertools
from typing import List


# 1,3,2,6,8,10,15,18,inf,inf
3, 2


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start, end = -1, -1
        merged = []
        intervals.append([float('inf'), float('inf')])

        def sort_key(interval):
            return interval[0]
        intervals.sort(key=sort_key)
        for (i_start, i_end) in intervals:
            if start == -1:
                start = i_start
                end = i_end
            elif i_start <= end:
                if i_end > end:
                    end = i_end
                if i_start < start:
                    start = i_start
            else:
                merged.append([start, end])
                start, end = i_start, i_end
        return merged


intervals = [[1, 4], [2, 6], [0, 0], [8, 10], [15, 18]]

s = Solution()
print(s.merge(intervals))
