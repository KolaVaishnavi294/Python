import java.util.Scanner;
public class Pretty
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        for(int i=0;i<n;i++)
        {
            int start=sc.nextInt();
            int end=sc.nextInt();
            int c=0;
            for(int j=start;j<end+1;j++)
            {
                int ld=j%10;
                if(ld==2||ld==3||ld==9)
                {
                    c++;
                }
            }
            System.out.println(c);
        }
    }
}