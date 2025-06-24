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
