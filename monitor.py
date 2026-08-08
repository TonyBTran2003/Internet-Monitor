import socket
import subprocess
import time
import httpx

host = "1.1.1.1"

def ping_host(host):
    result = subprocess.run(
    ["ping", "-c", "2", host],
    capture_output=True,
    text=True)

    if result.returncode == 0:# ping succeeded
        print(result.stdout)
    
    else:# ping failed
        print(f"Ping failed @ {host}")
    



def check_dns(domain):
    pass


def check_http(url):
    pass


def main():
    ping_host(host)


if __name__ == "__main__":
    main()