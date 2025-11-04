import java.util.Scanner;
public class Home
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int y=sc.nextInt();
        if((x*5)>=y)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }
    }
}