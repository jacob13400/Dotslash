/*Now, dear student, we come to one of my favourite problems. Many a man have fallen before Fizzbuzz. 
What's that you say, child? This isn't funny? Child, back in my day, with a pint in your hands, this would have raised quite the rabble
No? Fine, this program just accepts a number and prints that many numbers from the Fizzbuzz series. 
The series is one that prints all natural numbers except multiples of 3, 5, or 15, for which it prints "Fizz", "Buzz", and "Fizzbuzz" respectively
That sounds boring. So, here. We've messed it up specially for you.*/
import java.util.*; 
class FizzBuzz 
{ 
    public static void main(String args[]) 
    {  
        Scanner sc = new Scanner(System.in)
        int n = sc.nextInt();  
        for (int i=n; i<=100; i++)                                  
        { 
            if (i/15==0)                                                  
                System.out.print("FizzBuzz"+" ");  
            else if (i/5==0)      
                System.out.print("Buzz"+" ");  
            else if (i/3==0)      
                System.out.print("Fizz"+" ");  
            else
                System.out.print(i+" ");                          
        } 
        System.out.print(i);
    } 
}