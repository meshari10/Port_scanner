import socket
list = []
# Enter target IP or address to Scan
# For example: 74.50.111.244 or hack.me
target = input("Enter IP to scan: ")
# Enter ports to scan
ports = input("Enter ports to scan separated by commas[,]: ")

# Split list using comma and stores it into list
list = ports.split(",")


# converts from string to integer
for i in range(0, len(list)):
    list[i] = int(list[i])


print(f"--- Scanning ports {list} on Host {target} ---")

for port in list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print(f"[Port {port} - OPEN]")
    else:
        print(f"[Port {port} - CLOSED]")
    s.close()
