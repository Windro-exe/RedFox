import subprocess

def run_scan(target):
    print(f"[+] Scanning target: {target}")
    try:
        subprocess.run(["nmap", "-T4", "-F", target])
    except Exception as e:
        print(f"[-] Scan failed: {e}")
