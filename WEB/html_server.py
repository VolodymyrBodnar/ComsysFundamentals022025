from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

server_address = ('localhost', 8000)
httpd = HTTPServer(server_address, MyHandler)

print("Сервер запущено на http://localhost:8000")
httpd.serve_forever()