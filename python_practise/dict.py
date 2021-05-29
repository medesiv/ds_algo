# Dicts Key-Value Pairs, Unordered, Mutable

mydict = {"name":"Siva", "age":15, "city":"San Jose"}
mydict2 = dict(name = "Mary", city = "Boston")
print(mydict)

newdict = mydict.copy()

#newdict.pop("age")
newdict.popitem()
if "lastname" in mydict:
	print(newdict["name"])

try:
	 del newdict["name"]
except:
	print("no such key")

mydict.update(mydict2)
print("mydict:",mydict)
print("newdict:",newdict)


print("mydict2:",mydict2)

for key,val in newdict.items():
	print(key,val)



	

#print(newdict)