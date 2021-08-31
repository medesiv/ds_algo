"""
# Problem2:
# 1. A ---50----> B
# 2. B ---30----> C
# 3. C ---50----> A


Output:

# B --20--> C

"""

def get_min(arr):
    return arr.index(min(arr))

def get_max(arr):
    return arr.index(max(arr))

def min_of_two(x, y):
    return x if x < y else y

def settle_expense_helper(amount):
    """
    This is a recursive call for settling the amounts
    :param amount:
    :return:
    """
    mx_credit_idx = get_max(amount)
    mx_debit_idx = get_min(amount)

    #Recursive termination : If these are 0 that means all the parties are settled
    if (amount[mx_credit_idx] == 0 and amount[mx_debit_idx] == 0):
        return 0

    # Otherwise we need to settle and settling indicates there is a positive and negative value
    # amount[mx_credit_idx] gives max amount to be credited to any person
    # amount[mx_debit_idx] indicates max amount to be debited from a person

    min = min_of_two(-amount[mx_debit_idx], amount[mx_credit_idx])

    #each time update these values only
    amount[mx_credit_idx] -= min
    amount[mx_debit_idx] += min

    print("Person ", mx_debit_idx, " pays ", min
          , " to ", "Person ", mx_credit_idx)

    settle_expense_helper(amount)


def settle_expense(expenses):
    N = len(expenses)
    #Initializing all the debts to be 0 as no one owes anyone
    amounts = [0 for i in range(N)]
    #The net debts array is calculated from the expense transactions made for each person p
    for p in range(N):
        for i in range(N):
            amounts[p] += (expenses[i][p] - expenses[p][i])
    #print(balances)
    settle_expense_helper(amounts)

"""
Initial balances of A B C are assumed to be 0
Indicating below transactions as a list to simplify
# 1. A ---50----> B -- represented as [0,50,0]
# 2. B ---30----> C -- represented as [0,0,30]
# 3. C ---50----> A -- represneted as [50,0,0]
"""
expenses = [[0, 50, 0],
         [0, 0, 30],
         [50, 0, 0]]

settle_expense(expenses)