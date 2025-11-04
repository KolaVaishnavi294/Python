import java.util.Scanner;
public class Bill
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int units=sc.nextInt();
        double cp;
        if(units<=199)
        {
            cp=1.20;
        }
        else if(units>=200 && units<400)
        {
            cp=1.40;
        }
        else if(units>=400 && units<600)
        {
            cp=1.60;
        }
        else if(units>=600 && units<800)
        {
            cp=1.80;
        }
        else
        {
            cp=2.00;
        }
        double bill=units*cp;
        double surcharge=0;
        if(bill>400)
        {
            surcharge=bill*0.15;
        }
        double total=bill+surcharge;
        System.out.printf("Units Consumed: %d\n",units);
        System.out.printf("Cost per Unit: %.2f\n",cp);
        System.out.printf("Bill: %.2f\n",bill);
        System.out.printf("Surcharge: %.2f\n",surcharge);
        System.out.printf("Total Amount: %.2f\n",total);
    }
}