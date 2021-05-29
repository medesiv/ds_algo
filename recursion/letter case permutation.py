"""
Input : S = "a1b2"

Output: [a1b2, a1B2, A1b2, A1B2]


 
   a1b2

a1b2  A1b2


a1b2

"""


def space_eff_permute(s):
    temp = []
    return capitalize_helper(s, 0, temp)


def capitalize_helper(s, i, slate):
    if i == len(s):
        str = ""
        for el in slate:
            str += el
        print(str)
        return
    if s[i].isdigit():
        slate.append(s[i])
        capitalize_helper(s, i + 1, slate)
        slate.pop()
    else:
        slate.append(s[i].upper())
        capitalize_helper(s, i + 1, slate)
        slate.pop()
        slate.append(s[i].lower())
        capitalize_helper(s, i + 1, slate)
        slate.pop()

# Space complexity with immutable strings is 2^n + O(n^2) with mutable is 2^n + O(n)

def permute_with_strings(s):
    return capitalize_helper2(s, 0, "")


def capitalize_helper2(s, i, slate_str):
    if i == len(s):
        print(slate_str)
        return
    if s[i].isdigit():
        capitalize_helper2(s, i + 1, slate_str + s[i])
    else:
        capitalize_helper2(s, i + 1, slate_str + s[i])
        capitalize_helper2(s, i + 1, slate_str + s[i].upper())


S = "a1b2"
print("\nStrings based sol:\n")
print(permute_with_strings(S))

S = "a1b2C"
print("\nSpace efficient list based sol:\n")
print(space_eff_permute(S))
