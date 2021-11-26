from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1>top five programming languages</h1>

<h1>1.python</h1>
<p>Improved Productivity.
Interpreted Language. ...
Dynamically Typed. ...
Free and Open-Source.
Vast Libraries Support</p>

<h1>2.C++</h1>
<p>Mid-level programming language. ...
Object-Oriented. ...
Multi-paradigm programming language. ...
Memory Management. ...
Fast and Powerful.</p>

<h1>3.javascript</h1>
<p>Speed. Client-side JavaScript is very fast because it can be run immediately within the client-side browser. ...
Simplicity. JavaScript is relatively simple to learn and implement.
Popularity. ...
Interoperability. ...
Server Load.</p>

<h1>4.kotlin</h1>
<p>Speed. Client-side JavaScript is very fast because it can be run immediately within the client-side browser. ...
Simplicity. JavaScript is relatively simple to learn and implement.
Popularity. ...
Interoperability. ...
Server Load.</p>

<h1>5.swift</h1>
<p>It's safe. ...
Interoperable with Objective-C. ...
Low maintenance. ...
Better user experience. ...
Effective memory management</p>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8080)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

