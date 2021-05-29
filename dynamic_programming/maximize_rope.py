def max_product_from_cut_pieces(n):
    #
    # Write your code here.
    #
    if (n == 0):
        return 0
    res = []

    def helper(n, slate, start):
        temp_slate = slate[:]
        product = 1
        if (sum(temp_slate) == n):
            for i in temp_slate:
                product *= i
            res.append(product)

        for i in range(start, n):
            slate.append(i)
            helper(n, slate, i + 1)
            slate.pop()

    helper(n, [], 1)
    return max(res)


print(max_product_from_cut_pieces(5))

"""
                5
        /              / \ \ \ 
        0               1  2 3 4

        / \         /\ \
                    2 3 4 
    1 2 3 4
    
    
    max(table[i],
"""