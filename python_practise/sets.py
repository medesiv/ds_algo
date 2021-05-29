#Sets unordered , mutable , no duplicates

myset = {1,2,33,2,2,3}

myset.add(22)
myset.add(33)
myset.discard(22)
print(myset.pop()) 
print(myset)

odds = {1,3,4,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

print(u.intersection(odds))