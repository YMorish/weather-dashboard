#!/usr/bin/env python3
"""
Simple HTTP server to serve the weather app frontend
Run this script to serve your HTML files properly (avoiding file:// protocol issues)
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow requests to Flask backend
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def serve_frontend():
    """Start the frontend server"""
    # Change to directory containing HTML files
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"✅ Frontend server running at http://localhost:{PORT}/")
        print(f"📂 Serving files from: {os.getcwd()}")
        print(f"🌐 Open: http://localhost:{PORT}/index.html")
        print(f"🔙 Make sure your Flask backend is running on http://localhost:5000")
        print("\n📝 Instructions:")
        print("1. Keep this server running")
        print("2. Run your Flask app.py in another terminal")
        print("3. Open http://localhost:8000/index.html in browser")
        print("\nPress Ctrl+C to stop the server")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

if __name__ == "__main__":
    serve_frontend()