"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"


Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.


Follow up: Could you find an algorithm that runs in O(n) time?

"""
"""
Below is Optimum space wise 
"""

def min_window_substr(s,t):
    # create a map for character count
    INT_MAX = 10 ** 5
    char_map = {}
    for c in t:
        char_map[c] = char_map.get(c, 0) + 1  # get or setdefault
    i = 0  # start
    formed_len = 0
    min_window_size = INT_MAX
    min_left = 0
    if s == "" or t == "":
        return ""

    for j in range(len(s)):
        # if we found s[end]
        if s[j] in char_map:
            char_map[s[j]] -= 1
            if (char_map[s[j]] >= 0):
                formed_len += 1

        while formed_len == len(t):
            if (len(t) == formed_len == 1):
                return s[j]
            if min_window_size > j - i + 1:
                min_window_size = j - i + 1
                min_left = i
            if (s[i] in char_map):
                char_map[s[i]] += 1
                if (char_map[s[i]]) > 0:
                    formed_len -= 1
            i += 1

    if (min_window_size > len(s)): return ""
    return s[min_left:min_left + min_window_size]


s = "ADOBECADEBANC"
t = "ABC"
#print(min_window_substr("ABC","A"))
print(min_window_substr(s,t))

from collections import Counter
import math
def min_window(s,t):
    #need = {c:t.count(c) for c in set(t)}
    #need = Counter(t)
    need, missing = Counter(t),len(t)
    i,mw_start,mw_end=0,0,0
    for j,c in enumerate(s,1):
        if need[c]>0:
            missing-=1
        need[c]-=1
        if missing ==0:
            while i<j and need[s[i]]<0:
                need[s[i]]+=1
                i+=1
            if not mw_end or j-i <= mw_end - mw_start:
                mw_start = i
                mw_end = j
        j+=1
    return s[mw_start:mw_end]

s = "ADOBECODEBANC"
#print(min_window(s,"ABC"))