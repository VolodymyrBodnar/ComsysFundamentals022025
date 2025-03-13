import socket

HOST = '127.0.0.1'  # Адреса сервера
PORT = 12345        # Порт сервера

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))  # Підключаємося до сервера

while True:
    message = input("Введіть повідомлення (або 'exit' для виходу): ")
    if message.lower() == 'exit':
        break
    client_socket.sendall(message.encode())  # Відправляємо повідомлення
    data = client_socket.recv(1024)  # Отримуємо відповідь
    print(f"Сервер відповів: {data.decode()}")

client_socket.close()  # Закриваємо з'єднання