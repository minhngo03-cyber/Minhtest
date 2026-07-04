from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


HOST = "127.0.0.1"
PORT = 8000
INDEX_FILE = Path(__file__).with_name("index.html")


class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/index.html"):
            self.send_error(404, "Not Found")
            return

        content = INDEX_FILE.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), WebRequestHandler)
    print(f"Trang web dang chay tai http://{HOST}:{PORT}")
    print("Nhan Ctrl+C de dung server.")
    server.serve_forever()
