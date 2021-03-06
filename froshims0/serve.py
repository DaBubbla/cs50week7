# Implements a web server

from http.server import BaseHTTPRequestHandler, HTTPServer


# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    #GET
    def do_GET(self):

        # send response status code
        self.send_response(200)

        # send handlers
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # write message
        self.wfile.write(bytes("Hello, world", "utf8"))


# Configure server
port = 8080
server_address = ("0.0.0.0", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

# run server
httpd.serve_forever()