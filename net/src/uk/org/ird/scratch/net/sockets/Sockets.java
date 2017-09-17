package uk.org.ird.scratch.net.sockets;

import java.io.IOException;

public class Sockets {
    public static void main(String[] args) {
        OTWClient v = new OTWClient("vortex.labs.overthewire.org", 5842);
        try {
            System.out.println(v.vortex0());
        }
        catch(IOException e){
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }
}
