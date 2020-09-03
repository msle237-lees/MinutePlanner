import java.io.*;
import java.net.*;
import java.util.Scanner;
public class main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        try
        {
            String message = scan.nextLine();
            Socket soc=new Socket("localhost",2004);
            DataOutputStream dout=new DataOutputStream(soc.getOutputStream());
            dout.writeUTF(message);
            System.out.println("Sending " + message);
            dout.flush();
            dout.close();
            soc.close();
        }
        catch(Exception e)
        {
            e.printStackTrace();}
        }
}
