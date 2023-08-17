from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Hello I am taqiyeddine</h1>
    <p>This app is running on node: {}</p> 
    """.format(socket.gethostname())

if __name__ == '__main__':
    app.run(host='0.0.0.0')