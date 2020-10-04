from socket import*
from pandas import*
import time
import errno
import shutil
import sys

serverName = '192.168.1.100'
serverPort = 12000
BackUp_serverName = '192.168.1.100'
BackUp_serverPort = 11000
try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
except error as e:
    print("Error creating socket: %s" % e)
    sys.exit(1)
#clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
try:
    settimeout1 = clientSocket.settimeout(10)
    dummy = clientSocket.connect((serverName,serverPort))
    print(dummy)
except error as socket_error:
    print("An exception occured while connecting\nConnectin to backup server\n")
    try:
        clientSocket.close()
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((BackUp_serverName, BackUp_serverPort))
    except:
        print("An exception occured while connecting\nConnectin to backup server\n")
        sys.exit(1)
clientSocket.setblocking(1)
skipdata = 0
rangeskip = 0
while True:
    cntr = 0
    shutil.copy(r'/home/pi/Documents/AS2020/pi0203/mqtt/test01.xlsx',r'/home/pi/Documents/AS2020/pi0203/v2/Test08.xlsx')
    print("Copied")
    time.sleep(5)
    ip_data = pandas.read_excel(r'/home/pi/Documents/AS2020/pi0203/v2/Test08.xlsx', sheet_name='Import', skiprows = rangeskip)
    shapedata = ip_data.shape
    print(shapedata)
    rowsdata = shapedata[0]
    print(rowsdata)
    if rowsdata == 0:
        skipdata = skipdata
    else:
        skipdata = skipdata + rowsdata
    rangeskip = list(range(1,skipdata))
    print(skipdata)
    print(rangeskip)
    timestamp = ip_data['Param1'].tolist()
    power1 = ip_data['Param2'].tolist()
    param3 = ip_data['Param3'].tolist()
    if rowsdata == 0 :
        try:
            clientSocket.send(str('NP').encode())
        except error as e:
            if e.errno == errno.ECONNRESET:
                print("Error Sending Data {}".format(e))
                #clientSocket.shutdown(SHUT_RDWR)
                clientSocket.close()
                clientSocket = socket(AF_INET, SOCK_STREAM)
                #clientSocket.
                create_connection((BackUp_serverName, BackUp_serverPort))

                try:
                    clientSocket.send(str('NP').encode())
                except error as e:
                    print("backup prob2")
                    #sys.exit(1)
    for i in timestamp:
        power2 = power1[cntr]
        param32 = param3[cntr]
        timestamp2 = timestamp[cntr]
        clientData = [timestamp2,power2,param32]
        print(str(clientData))
        try:
            clientSocket.send(str(clientData).encode())
        except error as e:
            if e.errno == errno.ECONNRESET:
                #clientSocket.shutdown(SHUT_RDWR)
                clientSocket.close()
                clientSocket = socket(AF_INET, SOCK_STREAM)
                #clientSocket.
                create_connection((BackUp_serverName, BackUp_serverPort))
                time.sleep(5)
                try:
                    clientSocket.send(str(clientData).encode())
                except error as e:
                    print("backup prob3")
                    #clientSocket.send(str(clientData).encode())
                    #sys.exit(1)
            #print("Error Sending Data {}".format(e))
            #clientSocket.close()
            #clientSocket.connect((BackUp_serverName, BackUp_serverPort))
            try:
                clientSocket.send(str(clientData).encode())
            except error as e:
                print("backup prob4")
                #sys.exit(1)
        cntr = cntr + 1
    time.sleep(5)
#clientSocket.close()
