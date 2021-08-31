"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""
import math
def longest_substr_without_rep(s):
    seen = set() # keep track of seen values
    i = 0 # start of the window
    max_len = -math.inf
    for j in range(len(s)): #j is end of the window
        if(s[j] not in seen):
            seen.add(s[j])
            j+=1
            max_len = max(max_len,len(seen))
        else:
            seen.remove(s[i])
            i+=1
    return max_len,seen


print(longest_substr_without_rep("pwwkew"))


def longest_substr_without_rep2(s):
    seen = set() # keep track of seen values
    i = 0 # start of the window
    max_len = -math.inf
    for j in range(len(s)): #j is end of the window
        while s[j] in seen:
            seen.remove(s[i])
            i+=1
        seen.add(s[j])
        max_len = max(max_len,j-i+1)

    return max_len,seen

print(longest_substr_without_rep2("pwwkew"))