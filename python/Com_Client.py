from socket import*
from pandas import*

cntr = 0
serverName = '192.168.1.14'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.setblocking(1)
ip_data = pandas.read_excel(r'C:\Users\Anirudh\Documents\SIC\Sem2\Seminar\IOT\Test01.xlsx', sheet_name='Export')
timestamp = ip_data['Time'].tolist()
power1 = ip_data['Power'].tolist()

for i in timestamp:
    power2 = power1[cntr]
    timestamp2 = timestamp[cntr]
    clientData = [timestamp2,power2]
    print(str(clientData))
    clientSocket.send(str(clientData).encode())
    cntr = cntr + 1

clientSocket.close()
