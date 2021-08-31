
"""
We are working on a security system for a badged-access room in our company's building.

We want to find employees who badged into our secured room unusually often. We have an unordered list of names and entry times over a single day. Access times are given as numbers up to four digits in length using 24-hour time, such as "800" or "2250".

Write a function that finds anyone who badged into the room three or more times in a one-hour period. Your function should return each of the employees who fit that criteria, plus the times that they badged in during the one-hour period. If there are multiple one-hour periods where this was true for an employee, just return the first one.

badge_times = [
["Paul", "1355"],
["Jennifer", "1910"],
["John", "835"],
["John", "830"],
["Paul", "1315"],
["John", "1615"],
["John", "1640"],
["Paul", "1405"],
["John", "855"],
["John", "930"],
["John", "915"],
["John", "730"],
["John", "940"],
["Jennifer", "1335"],
["Jennifer", "730"],
["John", "1630"],
["Jennifer", "5"]
]

Expected output (in any order)
John: 830 835 855 915 930
Paul: 1315 1355 1405

n: length of the badge records array
"""


badge_times = [
["Paul", "1355"],
["Jennifer", "1910"],
["John", "835"],
["John", "830"],
["Paul", "1315"],
["John", "1615"],
["John", "1640"],
["Paul", "1405"],
["John", "855"],
["John", "930"],
["John", "915"],
["John", "730"],
["John", "940"],
["Jennifer", "1335"],
["Jennifer", "730"],
["John", "1630"],
["Jennifer", "5"]
]

import collections
import bisect
def badgeAccess(badgeTimes): # Q1
    hours = [i * 100 for i in range(24)]
    #hours.insert(bisect.bisect(hours,1355), 1355)
    print(hours)
    records = collections.defaultdict(lambda: [[] for _ in range(24)])
    for employee, time in badgeTimes:
        records[employee][bisect.bisect(hours, int(time)) - 1].append(time)
    return {
        employee: hour
        for employee, hours in records.items()
        for hour in hours[::-1]
        if len(hour) >= 3
    }

print(badgeAccess(badge_times))



