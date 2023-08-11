import socket
def client_program():
    print("type bye to terminate ")
    host=socket.gethostname()
    port=5000
    client_socket=socket.socket()
    client_socket.connect((host,port))
    message=input("->")
    while str(message)!="bye":
        client_socket.send(message.encode())
        data=client_socket.recv(1024).decode()
        print("recevied from server:"+data)
        message=input("->")
    client_socket.close()

client_program()        
        

    

