from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>" 

@app.route('/hostname')
def print_hostname():
    hostname = subprocess.run(['hostname'], capture_output=True)
    return "<pre>" + hostname.stdout.decode() + "</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')