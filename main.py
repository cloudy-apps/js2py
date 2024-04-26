from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from js2py import translate_js6

class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        input = post_body.decode('utf-8')

        try:
            response = translate_js6(input)
            self.send_response(200)
            self.send_header('Content-type', 'text/x-python; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(response).encode('utf-8'))
        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(str(e).encode('utf-8'))

def run(port=0):
    server_address = ('', port)
    httpd = HTTPServer(server_address, Server)
    print(f"Starting httpd server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run(port=int(os.getenv('PORT')))
