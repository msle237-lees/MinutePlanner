import java.io.*;
import java.net.*;
public class main {
    public static void main(String[] args) {

        try
        {
            Socket soc=new Socket("localhost",2004);
            DataOutputStream dout=new DataOutputStream(soc.getOutputStream());
            dout.writeUTF("Hello Server");
            dout.flush();
            dout.close();
            soc.close();
        }
        catch(Exception e)
        {
            e.printStackTrace();}
        }
}
