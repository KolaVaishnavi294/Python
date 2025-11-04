import java.util.Scanner;
public class Strong
{   public static int factorial(int n)
    {   
        int result=1;
        for(int k=1;k<=n;k++)
        {
            result*=k;
        }
        return result;
    }
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        for(int i=0;i<n;i++)
        {
            int a=sc.nextInt();
            int original=a;
            int s=0;
            while(a!=0)
            {
                int r=a%10;
                s+=factorial(r);
                a=a/10;
            }
            if(original==s)
            {
                System.out.println("Strong");
            }
            else
            {
                System.out.println("Not Strong");
            }
        }
    }
}