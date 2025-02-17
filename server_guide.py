
"""
COMPREHENSIVE PYTHON SERVER GUIDE
================================
This guide covers different server implementations in Python.
Each section demonstrates various server types and configurations.
"""

import socket
import http.server
import socketserver
from typing import Tuple, Any
import json
import threading
from urllib.parse import parse_qs

# ===========================
# SECTION 1: BASIC TCP SERVER
# ===========================
"""
Simple TCP server implementation.
"""
print("\n=== Basic TCP Server ===")

class TCPServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 8000):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        
        while True:
            client, address = self.socket.accept()
            print(f"Connection from {address}")
            self.handle_client(client)
    
    def handle_client(self, client_socket: socket.socket):
        data = client_socket.recv(1024).decode()
        print(f"Received: {data}")
        
        response = f"Server received: {data}"
        client_socket.send(response.encode())
        client_socket.close()

# ===========================
# SECTION 2: HTTP SERVER
# ===========================
"""
Basic HTTP server implementation.
"""
print("\n=== HTTP Server ===")

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <html>
            <body>
                <h1>Hello from Python HTTP Server!</h1>
            </body>
        </html>
        """
        self.wfile.write(html.encode())

def run_http_server(port: int = 8080):
    with socketserver.TCPServer(("0.0.0.0", port), HTTPRequestHandler) as httpd:
        print(f"HTTP Server running on port {port}")
        httpd.serve_forever()

# ===========================
# SECTION 3: WEBSOCKET SERVER
# ===========================
"""
Simple WebSocket server implementation.
"""
print("\n=== WebSocket Server ===")

class WebSocketServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 8765):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.clients = []
    
    def start(self):
        self.server.listen(5)
        print(f"WebSocket server started on port {self.server.getsockname()[1]}")
        
        while True:
            client, address = self.server.accept()
            self.clients.append(client)
            client_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_thread.start()
    
    def handle_client(self, client: socket.socket):
        while True:
            try:
                message = client.recv(1024).decode()
                if not message:
                    break
                self.broadcast(message, client)
            except:
                break
        
        self.clients.remove(client)
        client.close()
    
    def broadcast(self, message: str, sender: socket.socket):
        for client in self.clients:
            if client != sender:
                try:
                    client.send(message.encode())
                except:
                    self.clients.remove(client)
                    client.close()

# ===========================
# SECTION 4: JSON API SERVER
# ===========================
"""
Simple JSON API server implementation.
"""
print("\n=== JSON API Server ===")

class JSONAPIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "message": "Hello from JSON API",
            "status": "success",
            "data": {
                "endpoints": ["/api/data", "/api/users"],
                "version": "1.0"
            }
        }
        
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode())
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "message": "Data received",
            "received_data": data
        }
        
        self.wfile.write(json.dumps(response).encode())

def run_json_api(port: int = 8090):
    with socketserver.TCPServer(("0.0.0.0", port), JSONAPIHandler) as httpd:
        print(f"JSON API Server running on port {port}")
        httpd.serve_forever()

# ===========================
# SECTION 5: ASYNC SERVER
# ===========================
"""
Asynchronous server implementation using asyncio.
"""
print("\n=== Async Server ===")

import asyncio

class AsyncServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 8888):
        self.host = host
        self.port = port
    
    async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        addr = writer.get_extra_info('peername')
        print(f"New connection from {addr}")
        
        while True:
            data = await reader.read(100)
            if not data:
                break
                
            message = data.decode()
            print(f"Received {message} from {addr}")
            
            response = f"Echo: {message}"
            writer.write(response.encode())
            await writer.drain()
        
        print(f"Closing connection with {addr}")
        writer.close()
        await writer.wait_closed()
    
    async def start(self):
        server = await asyncio.start_server(
            self.handle_client, self.host, self.port
        )
        
        print(f"Async server running on {self.host}:{self.port}")
        async with server:
            await server.serve_forever()

# Example usage of different servers
if __name__ == "__main__":
    # Choose one server to run
    
    # TCP Server
    # tcp_server = TCPServer()
    # tcp_server.start()
    
    # HTTP Server
    # run_http_server()
    
    # WebSocket Server
    # ws_server = WebSocketServer()
    # ws_server.start()
    
    # JSON API Server
    # run_json_api()
    
    # Async Server
    # asyncio.run(AsyncServer().start())
    
    print("Uncomment the server you want to run")
