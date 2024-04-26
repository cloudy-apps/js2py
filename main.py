from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from js2py import eval_js

class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header('Content-type', 'text/x-python; charset=utf-8')
        self.end_headers()

        input = post_body.decode('utf-8')
        response = eval_js(input)
        self.wfile.write(response.encode('utf-8'))

def run(port=0):
    server_address = ('', port)
    httpd = HTTPServer(server_address, Server)
    print(f"Starting httpd server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run(port=int(os.getenv('PORT')))
