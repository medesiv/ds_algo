"""
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

"""

def letter_combs(str):

    digits_to_str = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }

    if not str:
        return []

    # abcdef
    res = []
    def helper(bag, next_digits):
        if len(next_digits) == 0:
            res.append(bag)
        else:
            for c in digits_to_str[next_digits[0]]:
                helper(bag+c,next_digits[1:])

    helper("",str)
    return res


print(letter_combs('23'))