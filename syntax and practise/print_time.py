"""
input - ("mon 10:00 am", mon 11:00 am)
Output - [11005, 11010, 11015...11100]
Output starts with 1 if the day is monday, 2 if tuesday and so on till 7 for sunday
Append 5 min interval times to that till the end time
So here it is 10:05 as first case, so its written as 11005
2nd is 10:10 so its written as 11010
...
...
Stop at 11100
"""


import datetime
from datetime import datetime as dt

def get_intervals(order=['mon 10:00 am', 'mon 11:00 am']):
    delta = datetime.timedelta(minutes=5)
    start = dt.strptime(order[0], '%a %I:%M %p')
    end = dt.strptime(order[1], '%a %I:%M %p')
    output = []
    while start < end:
        start += delta
        output.append(start.strftime('%w%H%M'))
    return output

"""
I wasn't sure how you'd want to handle the pm in an output, should it really go [11255,10100]? 
If so change output.append(start.strftime('%w%H%M')) to output.append(start.strftime('%w%I%M')),
but I think switching over to 24 hours is better for this "compressed" string.
"""
print(get_intervals())