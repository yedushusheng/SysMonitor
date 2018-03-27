import socket
import sys

class SockServer(object):

    def Client(self):
        s = socket.socket(
            socket.AF_INET,socket.SOCK_STREAM
        )
        host  = socket.gethostname()
        port = 8888
        s.connect((host,port))
        msg = s.rev(1024)
        s.close()
        print(msg.decode('utf-8'))


    def Server(self):
        serversocket = socket.socket(
            socket.AF_INET,socket.SOCK_STREAM
        )
        host = socket.gethostname()
        port = 8888
        serversocket.bind(host,port)
        serversocket.listen(5)

        while(True):
            clientsocket,addr = serversocket.accept()

            print("connected address:%s" % str(addr))

            msg = "Welcome to SysMonitor utils!" +"\r\n"
            clientsocket.send(msg.encode('utf-8'))
            clientsocket.close()