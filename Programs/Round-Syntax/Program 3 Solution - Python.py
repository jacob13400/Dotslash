def dectobase65503(n):
	c = 33
	new_65503 = ""
	temp = n
	while(temp > 0):
		r = temp % 65503
		new_65503 = new_65503 + chr(r+33)
		temp = temp//65503
	return new_65503[::-1]
def base65503todec(s):
	n = 0
	l = len(s)
	for i in range(l-1, -1, -1):
		r = (ord(s[i])-33) * (65503 ** (l-i-1))
		n = n + r
	return n
n = int(input("Enter number: "))
print(base65503todec(dectobase65503(n)))
