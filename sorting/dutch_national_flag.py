"""
 [G, B, G, G, R, B, R, G]



 [R, R, G, G, G, G, B, B]

"""

def group_nums(arr):
    red_ptr=0
    blue_ptr=len(arr) -1
    i=0
    while i<=blue_ptr:
        if arr[i] == "G":
            i+=1
        elif arr[i]=="B":
            arr[i],arr[blue_ptr]=arr[blue_ptr],arr[i]
            blue_ptr-=1
        elif arr[i]=="R":
            arr[i],arr[red_ptr]=arr[red_ptr],arr[i]
            red_ptr+=1
            i+=1
    return arr

strings=['G', 'B', 'G', 'G', 'R', 'B','R','G']
print(group_nums(strings))