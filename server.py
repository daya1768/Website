#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class HotelRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        requested_path = self.path.split("?", 1)[0]
        if requested_path in {"", "/", "/index", "/home"}:
            self.path = "/index.html"
        return super().do_GET()


def run() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", 8000), HotelRequestHandler)
    print("Serving Golden Horizon Hotel at http://0.0.0.0:8000")
    server.serve_forever()


if __name__ == "__main__":
    run()
