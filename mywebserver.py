from http.server import HTTPServer, BaseHTTPRequestHandler
content  = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1>Welcome</h1>
</body>
</html>
"""
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html;charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8080)
httpd = HTTPServer(server_address,myHandler)
print("my webserver is running...")
httpd.serve_forever()








        