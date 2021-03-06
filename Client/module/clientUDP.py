import socket

class ClientUDP():
    def __init__(self, response, target, ipType, address, port):
        self.target = target
        self.address = address
        self.port = port
        self.address = (self.address, self.port)

        if ipType == 4:
            self.cnx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.cnx = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        #Then we run
        self.__run(response)

    def __run(self, response):
        print('UDP - Connecting to : ' + str(self.address))
        buffer = bytearray('-Yolo-\n', 'ascii')
        self.cnx.sendto(buffer, self.address)
        try:
            self.cnx.settimeout(10) #Timeout of 10s
            (res,addr) = self.cnx.recvfrom(1024)
        except socket.timeout:
            success = 'X'
            print('time out')
        else:
            success = 'OK'
            print('UDP - It Worked - ' + res.decode('ascii').strip("\n"))
        response[self.target].append(('UDP', self.address, self.port, success))
