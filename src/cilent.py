import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect(('192.168.3.18',8080)) # θΏζ₯

while True:
	text = input()
	server.send(text.encode('utf-8')) # ει
	if text == 'exit':
		break
back_msg=server.recv(1024)
print(back_msg)
server.close()
