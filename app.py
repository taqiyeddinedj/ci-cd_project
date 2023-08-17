from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def print_hostname():
    hostname = subprocess.run(['hostname'], capture_output=True)
    return hostname.stdout.decode()

if __name__ == '__main__':
    app.run(host='0.0.0.0')