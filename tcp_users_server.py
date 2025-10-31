import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)

    messages: list[str] = []
    while True:
        client_socket, client_adress = server_socket.accept()
        print(f'Пользователь с адрессом: {client_adress} подключился к серверу')
        message = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_adress} отправил сообщение: {message}")

        messages.append(message)
        
        client_socket.send('\n'.join(messages).encode())
        client_socket.close()
        
if __name__ == '__main__':
    server()
