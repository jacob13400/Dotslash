num = int(input("Enter number of digits you want in series (minimum 3): "))
first = 0
second = 1 
print("\nFibonacci series is:")
print("{0}, {1}".format(first, second), end = ", ")
for i in range(2, num):
	next = first + second
	if i != num-1:
		print(next, end=", ")
	else:
		print(next)
	first = second
	second = next