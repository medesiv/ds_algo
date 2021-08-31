#Ordered, mutable, allows duplicate elements
import time

start_time = time.time()


mylist = ["banana","orange","ch","c"]


print(mylist)

new_list = sorted(mylist)
print(new_list)

new_list_cpy = mylist.copy()
new_list_another = mylist[:]
#Careful with 
new_list_another1 = mylist

new_list_cpy.append("lemon")

print("new_list_cpy",new_list_cpy)
print("new_list",new_list)
print("mylist",mylist)
print("new_list_another",new_list_another)
print("new_list_another1",new_list_another1)


all_caps = [w[0:2].capitalize() for w in mylist]
all_caps.pop()
all_caps.pop()
all_caps.pop()
print(all_caps)

print(mylist.index("c"))

print("--- %s seconds ---" % (time.time() - start_time))