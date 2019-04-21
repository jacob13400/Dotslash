import java.util.*;
public class Program3
{
	public static String dectobase65503(int n)
	{
		int c = 33;
		String new_65503 = "";
		int temp = n;
		while(temp > 0)
		{
			int r = temp % 65503;
			new_65503 = new_65503 + (char)(r+33);
			temp = temp/65503;
		}
		String str = new_65503;
		String reverse = "";
        for(int i = str.length() - 1; i >= 0; i--)
        {
            reverse = reverse + str.charAt(i);
        }
		return reverse;
	}
	public static double base65503todec(String s)
	{
		double n = 0;
		int l = s.length();
		for(int i = l-1; i > -1; i = i - 1)
		{
			double r = ((int)(s.charAt(i))-33) * (Math.pow(65503,(l-i-1)));
			n = n + r;
		}
		return n;
	}
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println((int)(base65503todec(dectobase65503(n))));
	}
}