/*Ah, dear niblets, here we are again. What, don't like that name either? You people are impossible to please.
I'll turn you over by the end of this, or my name isn't Quentinius Arvid Ulf Twaxtletus. Here, take your problem.
The Fibonacci series prints numbers as the sum of the preceding two digits, beginning in whole numbers. Much like me last night.
Remember, whole numbers. If the numbers are natural, and don't have wholes in them, they're not the Fibonacci series.*/
public class Fibonacci {
    public static void main(String[] args) {
        int n = 10, t1 = 1, t2 = 2;
        System.out.print("First " + n + " terms: ");
        for (int i = 1; i <= n; ++i)
        {
            if(i != n)
            	System.out.print(t2 + " + ");
            else
            	System.out.print(t2);
            int sum = t1 + t2 - 1;
            t1 = t2;
            t2 = sum;
        }
    }
}