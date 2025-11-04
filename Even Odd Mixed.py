import java.util.Scanner;
public class Number
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int c1=0;
        int c2=0;
        int c3=0;
        while(a!=0)
        {
            int r=a%10;
            if(r%2==0) c1++;
            else if(r%2!=0) c2++;
            a=a/10;
        }
        if(c1>0&&c2==0){
            System.out.println("Even");
        }
        else if(c1==0&&c2>0)
        {
            System.out.println("Odd");
        }
        else if(c1>0&&c2>0)
        {
            System.out.println("Mixed");
        }
    }
}