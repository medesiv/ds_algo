import heapq
from collections import defaultdict
strs = ['alpha','alpha','gamma','gamma','gamma','bin','bin','bin', 'delta', 'delta', 'delta']

cnt_mp = {}

for w in strs:
	cnt_mp[w] = cnt_mp.get(w,0) + 1

print(cnt_mp)


final_mp = {}
for k,v in cnt_mp.items():
	hp = final_mp.get(v, [])
	heapq.heappush(hp, k)
	final_mp[v] = hp

s_cnt_mp = sorted(final_mp.items(), key = lambda x: x[0], reverse=True)


for k, v in s_cnt_mp:
	while len(v) != 0:
		print(k, heapq.heappop(v))


