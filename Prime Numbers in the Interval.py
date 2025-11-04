import java.util.Scanner;
public class Prime
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        for(int i=a;i<=b;i++)
        {
            if(prime(i))
            {
                System.out.println(i);
            }
        }
    }
        public static boolean prime(int n)
        {   if(n<=1)
           {
               return false;
           }
            for(int j=2;j<=Math.sqrt(n);j++)
            {
                if(n%j==0)
                {
                    return false;
                }
            }
            return true;
        }
}