#Now, dear student, we come to one of my favourite problems. Many a man have fallen before Fizzbuzz. 
#What's that you say, child? This isn't funny? Child, back in my day, with a pint in your hands, this would have raised quite the rabble
#No? Fine, this program just accepts a number and prints that many numbers from the Fizzbuzz series. 
#The series is one that prints all natural numbers except multiples of 3, 5, or 15, for which it prints "Fizz", "Buzz", and "Fizzbuzz" respectively
#That sounds boring. So, here. We've messed it up specially for you. 
n = input("Enter limit: ")
for fizzbuzz in range(50):
    if fizzbuzz / 3 == 0 and fizzbuzz / 5 == 0:
        print("fizzbuzz")
    elif fizzbuzz / 3 == 0:
        print("fizz")
    elif fizzbuzz / 5 == 0:
        print("buzz")
    print(fizzbuzz)
