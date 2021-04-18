from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import dectron2

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("<input type='file' id='avatar' name='avatar' accept='image/png, image/jpeg'>", 'utf-8'))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self, ...):
        img = self.post_data
        cls_ret = detectron2(img)
        if cls_ret[0] > 0.5:
            self.wfile.write(bytes("There is a windows in the build..."))
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
