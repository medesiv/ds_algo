
nums = [100,4,200,1,3,2]

def len_of_longest_seq(nums):
    max_len,len_of_seq = 0,0
    nums_set = set(nums)
    for n in nums:
        if n-1 not in nums_set:
            len_of_seq=0
            while n+len_of_seq in nums_set:
                len_of_seq+=1
            max_len = max(len_of_seq,max_len)
    return max_len


# # # a = 142
# # # r = 0
# # # while a>0:
# # #     r = r*10 + a%10
# # #     a=a//10
# # #
# # # print(r)
# #
# # # a to i
# # a=[]
# # for i in range(0,10):
# #     a.append(i)
# #
# # print(a)
# #
# # str ="42"
# #
# # for i in str:
# #     print(i.isalpha())
# """
#
# a = [50,3,2]
#
# if a[0]%4==0:
#     print("hello it's a multiple of 4 ")
# elif a[0]%2==0:
#     print("heya it's a multiple of 2")
#
#
# if a[0]%5==0:
#     print("yes")
#
# else:
#     print("not a multiple of 4 or 2")
#    """
#
# str = ['abc','def','ghi']
# res =[]
#
#
# def modify_arr(arr,i):
#
#     while i>0:
#         arr.append(i)
#         # if i ==1:
#         #     add_few_val(arr)
#         #     return
#         modify_arr(arr,i-1)
#         i-=1
#
#     return arr
#
# def add_few_val(temp):
#     temp = temp.copy()
#     temp.append(232)
#     print(temp)
#
#
# print(modify_arr([],5))


