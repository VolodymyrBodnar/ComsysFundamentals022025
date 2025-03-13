import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []  # Список активних клієнтів

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break  # Вихід при втраті з'єднання
            broadcast(message, client_socket)
        except:
            break  # Вихід при помилці

    client_socket.close()
    clients.remove(client_socket)  # Видаляємо клієнта зі списку

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message)
            except:
                client.close()
                clients.remove(client)

print(f"Сервер запущений на {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Підключився новий клієнт: {client_address}")
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
