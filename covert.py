def ip_to_bin(ip):
    return '.'.join(f"{int(octet):08b}" for octet in ip.split('.'))

# Ask user for input
ip = input("Enter an IP address (e.g. 192.168.1.1): ")

binary_ip = ip_to_bin(ip)
print(f"Binary representation: {binary_ip}")
