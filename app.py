from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Hello from Flask!</h1>
    <p>This app is running on node: {}</p>
    <p>All nodes:</p>
    <ul>{}</ul>
    """.format(os.uname()[1], '\n'.join('<li>{}</li>'.format(n) for n in os.environ['NODES'].split(',')))

if __name__ == '__main__':
    app.run(host='0.0.0.0')