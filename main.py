from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
from urllib.error import URLError

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello, World!")

        elif self.path == "/health":
            self.send_response(200)
            self.end_headers()

        elif self.path == "/weather":
            try:
                response = urlopen("https://wttr.in")
                data = response.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(data)
            except URLError as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode())

        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHandler):
    server_address = ('', 3000)
    httpd = server_class(server_address, handler_class)
    print("Serving on port 3000...")
    httpd.serve_forever()

run()
