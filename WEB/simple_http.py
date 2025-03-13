from http.server import HTTPServer, SimpleHTTPRequestHandler

server_address = ('', 8000)  # Сервер запускається на локальному порту 8000
httpd = HTTPServer(server_address=('localhost', 8000), RequestHandlerClass=SimpleHTTPRequestHandler)

print("Сервер запущено на порту 8000...")
httpd.serve_forever()