"""

Eg: 
    C1 --> [3,3]
    C3 --> [1,3]
    C4 --> [6,3]
    Formula - Distance from C1 
        1. To C3 is -> |C1.x - C3.x| + |C1.y - C3.y| -> |3-1| + |3-3| = 2
        2. To C4 is -> |C1.x - C4.x| + |C1.y - C4.y| -> |3-6| + |3-3| = 3
        3. So C3 is nearest city from C1. 

Input:
cityNames: ["c1","c2","c3","c4"]
x: [3,2,1,6]
y: [3,2,3,3]
queriedCities: ["c1","c2","c3"]

Output:
returnList: ["C3","NONE", "C1"]

"""
import collections
import math

names = ["c1","c2","c3","c4"]
xs =  [3,2,1,6]
ys = [3,2,3,3]
queriedCities = ["c1","c2","c3"]

def nearest(names, xs, ys, queries): # sort O(N*logN)
    Near = collections.namedtuple("Near", ["dist", "name"], defaults=[math.inf, ""])
    cities = {name: Near() for name in names}
    #print(cities)
    xy, yx = [collections.defaultdict(dict) for _ in range(2)]

    for name, x, y in zip(names, xs, ys):
        xy[x][y] = yx[y][x] = name
    print(xy)
    print(yx)
    for values in xy.values(), yx.values():
        for axes in values:
            print(axes)
            items = [(-math.inf, "")] + sorted(axes.items()) + [(math.inf, "")]
            for (prevAxis, prevName), (currAxis, currName), (nextAxis, nextName) in zip(items, items[1:], items[2:]):
                cities[currName] = min(cities[currName], Near(currAxis - prevAxis, prevName), Near(nextAxis - currAxis, nextName))
    return [cities[query].name for query in queries]


print(nearest(names,xs,ys,queriedCities))