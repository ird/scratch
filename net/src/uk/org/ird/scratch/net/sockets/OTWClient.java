/* OTW Vortex 1 */
package uk.org.ird.scratch.net.sockets;

import java.io.*;
import java.net.InetSocketAddress;
import java.nio.BufferUnderflowException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.channels.SocketChannel;

public class OTWClient {
    String url;
    int port;
    public OTWClient(String url, int port) {
        this.url = url;
        this.port = port;
    }

    public String vortex0() throws IOException{

        StringBuilder sb = new StringBuilder();
        try (
                SocketChannel socket = SocketChannel.open();
        ) {
            socket.connect(new InetSocketAddress(url,port));
            ByteBuffer buf = ByteBuffer.allocateDirect(64).order(ByteOrder.LITTLE_ENDIAN);

            /** CHALLENGE **/
            /* writing to buf <- socket */
            socket.read(buf);

            /*reading from buf -> total */
            buf.flip();
            long total = accum(buf); //4x 32-bit unsigned ints

            /** RESPONSE **/
            /* writing to buf <- total */
            buf.flip();
            buf.clear();
            buf.putLong(total);

            /* reading from buf -> socket */
            buf.flip();
            socket.write(buf);

            /** REPLY **/
            /* writing to buf <- socket */
            buf.flip();
            buf.clear();
            socket.read(buf);

            /* reading from buf -> string */
            buf.flip();
            while(buf.remaining() > 0){
                sb.append((char)buf.get());
            }

            socket.close();
        }
        catch (BufferUnderflowException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }

        return sb.toString();
    }

    private long accum(ByteBuffer buf){
        long total = 0;
        for(int i=0;i<4;i++){
            byte[] dst = new byte[4];
            buf.get(dst, 0,4);
            total += ByteBuffer.wrap(dst).order(ByteOrder.LITTLE_ENDIAN).getInt();
        }
        return total;
    }

}
