Repository: windro-exe/redfox
Files analyzed: 8

Estimated tokens: 696

Directory structure:
└── windro-exe-redfox/
    ├── README.md
    ├── main.py
    ├── core/
    │   ├── exploit.py
    │   ├── recon.py
    │   ├── report.py
    │   └── scanner.py
    ├── data/
    │   └── payloads.json
    └── utils/
        └── helpers.py


================================================
FILE: README.md
================================================
# RedFox - Offensive Security Toolkit

RedFox is a modular Python tool for automating recon, scanning, and basic exploitation tasks during offensive security engagements.

## Features
- Subdomain and DNS recon
- Nmap port scanning
- Basic XSS testing
- Report generation

## Usage
```bash
python main.py
```

Ensure `nmap` is installed on your system.



================================================
FILE: main.py
================================================
from core import recon, scanner, exploit, report

def main():
    print("Welcome to RedFox - Offensive Security Toolkit")
    target = input("Enter target URL or IP: ")
    recon.run_recon(target)
    scanner.run_scan(target)
    exploit.run_exploit(target)
    report.generate_report(target)

if __name__ == "__main__":
    main()



================================================
FILE: core/exploit.py
================================================
import requests

def run_exploit(target):
    print(f"[+] Testing for basic XSS on {target}")
    try:
        xss_test = "<script>alert(1)</script>"
        response = requests.get(target, params={"q": xss_test})
        if xss_test in response.text:
            print("[!] XSS vulnerability detected!")
        else:
            print("[-] No basic XSS detected.")
    except Exception as e:
        print(f"[-] Exploit test failed: {e}")



================================================
FILE: core/recon.py
================================================
import socket
import requests

def run_recon(target):
    print(f"[+] Running recon on {target}")
    try:
        ip = socket.gethostbyname(target)
        print(f"[+] Resolved IP: {ip}")
    except Exception as e:
        print(f"[-] Failed to resolve IP: {e}")



================================================
FILE: core/report.py
================================================
def generate_report(target):
    print(f"[+] Generating report for {target}")
    with open(f"{target.replace('.', '_')}_report.txt", "w") as f:
        f.write("RedFox Security Report\n")
        f.write(f"Target: {target}\n")
        f.write("Scan completed. See terminal output for details.\n")



================================================
FILE: core/scanner.py
================================================
import subprocess

def run_scan(target):
    print(f"[+] Scanning target: {target}")
    try:
        subprocess.run(["nmap", "-T4", "-F", target])
    except Exception as e:
        print(f"[-] Scan failed: {e}")



================================================
FILE: data/payloads.json
================================================
{
    "xss": ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"],
    "sqli": ["' OR '1'='1", "'; DROP TABLE users; --"]
}



================================================
FILE: utils/helpers.py
================================================
def print_banner():
    print("""
    ==============================
    RedFox Offensive Toolkit
    ==============================
    """)


