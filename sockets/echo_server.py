import socket

HOST = '127.0.0.1'  # Локальний хост
PORT = 12345        # Порт, на якому працює сервер

# Створюємо сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  # Прив'язуємо до адреси та порту
server_socket.listen()  # Починаємо слухати підключення

print(f"Сервер слухає на {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()  # Приймаємо підключення
    print(f"Підключено: {client_address}")

    while True:
        data = client_socket.recv(1024)  # Отримуємо дані
        if not data:
            break  # Якщо отримали пусте повідомлення – завершуємо обмін
        client_socket.sendall(data)  # Відправляємо ті ж дані назад

    client_socket.close()  # Закриваємо з'єднання