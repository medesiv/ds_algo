

#XXXII

def roman_to_int(s):
	mp = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
	num,i = 0,0
	if s in mp:
		return mp[s]
	else:
		while i < len(s):
			if i+1 <len(s) and mp[s[i]]<mp[s[i+1]]:
				num+=mp[s[i+1]] - mp[s[i]]
				i+=2
			else:
				num+=mp[s[i]]
				i+=1
		return num


print(roman_to_int("XXXIV"))