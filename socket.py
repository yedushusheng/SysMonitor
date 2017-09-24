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

            print("连接地址:%s" % str(addr))

            msg = "欢迎使用系统监控平台！" +"\r\n"
            clientsocket.send(msg.encode('utf-8'))
            clientsocket.close()