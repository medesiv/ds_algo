"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

def merge(intervals):
    if not intervals:
        return []
    arr = sorted(intervals,key= lambda x: x[0])
    for i in range(len(arr)-1):
        j = i+1
        while j<=len(arr)-1 and (arr[i][1]>=arr[j][0]):
            arr[i][1] = max(arr[j][1],arr[i][1])
            arr.pop(j)
    return arr

arr = [[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))