#! /bin/python3

import nmap

scanner = nmap.PortScanner()

print('Welcome to Scanner')
print('<---------------------------------------------------------------->')

ip_addr = input("Enter ip address to scan\n")

print("Correct IP?: " + ip_addr)

scanner.scan(ip_addr, '21-443', '-V -sU')
# print(scanner.scaninfo())
print('IP status', scanner[ip_addr].state())
print(scanner[ip_addr].all_protocols())
print('Open ports: ', scanner[ip_addr]['tcp'].keys())
