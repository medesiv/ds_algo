#Ordered, immutable, allows duplicate elements

mytuple = (11,2,2,3)



x=[31, 231, 3, 56, 63, 23]

try:
	print(x.index(311))
except:
	print("No such value")
print(x)

for i in mytuple:
	print(i)

print(mytuple)