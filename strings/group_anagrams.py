"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""


"""
Below is O(NK)
"""
import collections
def group_anagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()
"""
Below is O(NKlogK)
"""

def group_anagrams(strs):
    if not strs:
        return [[""]]
    else:
        hmap={}
        for str in strs:
            key =  "".join(sorted(str))
            if key not in hmap:
                hmap[key]=[str]
            else:
                hmap[key].append(str)
        return list(hmap.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))