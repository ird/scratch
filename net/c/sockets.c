#include <sys/socket.h>
#include <sys/types.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

#define MAXDATASIZE 16

int getsockfd(const char* url, const char* port);

int main(int argc, char** argv) {
    int sock = getsockfd("vortex.labs.overthewire.org", "5842");
    char buf[MAXDATASIZE];
    int numbytes;
    if((numbytes = recv(sock, buf, MAXDATASIZE-1, 0)) == -1){
        fprintf(stderr, "recv() error\n");
    }
    buf[MAXDATASIZE] = 0;
    printf("Recv: %s\n", buf);
    close(sock);
    return 0;
}
int getsockfd(const char* url, const char* port) {
    struct addrinfo hints;
    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_flags = AI_PASSIVE;
    int status;
    struct addrinfo *servinfo;
    if ((status = getaddrinfo(url, port, &hints, &servinfo)) != 0) {
        fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(status));
        exit(1);
    }
    struct addrinfo* p;
    int sock;
    for(p = servinfo; p != NULL; p = p->ai_next){
        void* addr = &((struct sockaddr_in *)p->ai_addr)->sin_addr;
        char ipstr[INET_ADDRSTRLEN];
        inet_ntop(p->ai_family,addr, ipstr, sizeof ipstr);
        printf("Connecting to: %s\n", ipstr);
        sock = socket(p->ai_family, p->ai_socktype, p->ai_protocol);
        if(sock == -1) {
            continue;
        }
        if(connect(sock, p->ai_addr, p->ai_addrlen) == -1) {
            close(sock);
            continue;
        }
        break;
    }
    if(p == NULL) {
        fprintf(stderr, "socket()/connect() error, couldn't connect\n");
        exit(1);
    }
    freeaddrinfo(servinfo);
    return sock;
}
