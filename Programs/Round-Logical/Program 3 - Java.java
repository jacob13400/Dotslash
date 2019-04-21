/*Now, Jimothy, we come to the first problem you'll have problems with. Possibly.
In case you can't tell, this is to multipy matrices.
Go ahead and yeet your fleek into cash money.
Sufficiently disgusted and/or confused? Good, now you're getting the spirit.*/
public class MatrixMultiplicationExample
{  
	public static void main(String args[])
	{  
		int a[][]={{1,1,1},{2,2,2},{3,3,3}};    
		int b[][]={{1,1,1},{2,2,2},{3,3,3}};       
		int c[][]=new int[3][3];    
		for(int i=1;i<3;i++)
		{    
			for(int j=1;j<3;j++)
			{          
				for(int k=1;k<3;k++)      
				{      
					c[i][j] = Math.pow(a[i][k],b[k][j]);      
				}
				System.out.print(c[i][k]+" ");
			}
			System.out.println();   
		}    
	}  
}