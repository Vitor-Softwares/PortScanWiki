import socket

ip = raw_input("Write the IP our Address: \n")
cport = raw_input("Do you want to scan all ports for, specific port or group of ports? \n1 = all \n2 = specific \n3 = group \n")

if cport == "1":
    ports = range(65535)
    timeout = float(raw_input("Write the timeout for requests: \n 0.01 = 10 miliseconds \n"))
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        code = client.connect_ex((ip, port))
        if code == 0:
            print str(port) + " -> Port Open"
elif cport == "2":
    port1 = int(raw_input("Write the number of port: \n"))
    if port1 > 65536:
        print "This number of port is invalid!"
    else:
        timeout = float(raw_input("Write the timeout for requests: \n 0.01 = 10 miliseconds \n"))
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        code = client.connect_ex((ip, port1))
        if code == 0:
            print str(port1) + " -> Port Open"
        else:
            print str(port1) + " -> Port Closed"
elif cport == "3":
    timeout = float(raw_input("Write the timeout for requests: \n 0.01 = 10 miliseconds \n"))
    nport = int(raw_input("how many ports will you scan? \n"))
    ports2 = []
    count = 0
    while count < nport:
        ports2.append(int(raw_input("Write the ports: \n")))
        count += 1
    for port2 in ports2:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((ip, port2))
        if code == 0:
            print str(port2) + " -> Port Open"
        else:
            print str(port2) + " -> Port Closed"
else:
    print "This option is invalid!!"











