import socket 
s=socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(10)
print(host)
print("waiting for connection....")
conn,addr=s.accept()
print(addr,"connected to server ")
filename