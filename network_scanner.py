import nmap

scanner = nmap.PortScanner()

target = input("Enter IP address: ")

print("Scanning...", target)

scanner.scan(target, '1-1024')

for host in scanner.all_hosts():
    print("Host:", host)
    print("State:", scanner[host].state())

    for proto in scanner[host].all_protocols():
        print("Protocol:", proto)

        for port in scanner[host][proto]:
            state = scanner[host][proto][port]['state']
            print("Port:", port, "State:", state)