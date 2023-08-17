import subprocess

def run_command(command):
    return subprocess.getoutput(command)

if __name__ == '__main__':
    run_command("echo 'Hello, this pod is working.'")
    run_command("echo $(hostname)")
