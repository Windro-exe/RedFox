import socket
import requests

def run_recon(target):
    print(f"[+] Running recon on {target}")
    try:
        ip = socket.gethostbyname(target)
        print(f"[+] Resolved IP: {ip}")
    except Exception as e:
        print(f"[-] Failed to resolve IP: {e}")
