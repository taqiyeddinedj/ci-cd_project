import subprocess

def get_hostname():
    return subprocess.getoutput('hostname')

if __name__ == '__main__':
    print(get_hostname())
