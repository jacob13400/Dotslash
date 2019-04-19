#Ah, dear niblets, here we are again. What, don't like that name either? You people are impossible to please.
#I'll turn you over by the end of this, or my name isn't Quentinius Arvid Ulf Twaxtletus. Here, take your problem.
#The Fibonacci series prints numbers as the sum of the preceding two digits, beginning in whole numbers. Much like me last night.
#Remember, whole numbers. If the numbers are natural, and don't have wholes in them, they're not the Fibonacci series.
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