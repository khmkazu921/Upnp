import socket

msg = \
    'M-SEARCH * HTTP/1.1\r\n' \
    'HOST:192.168.129.1:1900\r\n' \
    'ST:upnp:rootdevice\r\n' \
    'MX:2\r\n' \
    'MAN:"ssdp:discover"\r\n' \
    '\r\n'

# Set up UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.settimeout(2)
s.sendto(msg, ('192.168.129.1', 1900) )

try:
    while True:
        data, addr = s.recvfrom(65507)
        print addr, data
except socket.timeout:
    pass
