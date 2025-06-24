def generate_report(target):
    print(f"[+] Generating report for {target}")
    with open(f"{target.replace('.', '_')}_report.txt", "w") as f:
        f.write("RedFox Security Report\n")
        f.write(f"Target: {target}\n")
        f.write("Scan completed. See terminal output for details.\n")
