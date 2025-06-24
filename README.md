# 🦊 RedFox - Offensive Security Toolkit

RedFox is a modular and extensible Python-based offensive security tool designed to assist in red teaming, ethical hacking, and penetration testing operations. It automates core stages of the attack lifecycle: reconnaissance, vulnerability scanning, exploitation, and basic reporting.

---

## 📁 Project Structure

```
RedFox/
├── main.py                     # Entry point of the tool
├── core/                       # Core functionality
│   ├── recon.py                # DNS and IP recon
│   ├── scanner.py              # Nmap-based port scanner
│   ├── exploit.py              # XSS vulnerability tester
│   └── report.py               # Report generator
├── utils/
│   └── helpers.py              # UI and formatting utilities
├── data/
│   └── payloads.json           # XSS and SQLi payloads
└── README.md                   # Documentation
```

---

## 🚀 Features

- 🌐 **Reconnaissance**
  - DNS resolution (IP lookup)
  - Easily extendable to subdomain and WHOIS queries

- 🔍 **Port Scanning**
  - Fast scanning using `nmap` for detecting open ports and services

- 💥 **Exploitation**
  - Tests for basic reflected XSS using GET requests
  - Uses customizable payloads from `payloads.json`

- 📝 **Reporting**
  - Outputs a plain-text report of the recon and scan results

---

## 📦 Requirements

### 🐍 Python Libraries

Install required Python modules:

```bash
pip install requests
```

### 🔧 External Tools

Ensure `nmap` is installed:

```bash
sudo apt install nmap   # for Debian/Ubuntu
```

---

## 🧪 Usage

### 1. Run the Tool

```bash
python main.py
```

### 2. Enter Target

You'll be prompted to input a target domain or IP:

```
Enter target URL or IP: example.com
```

### 3. Sample Output

```
[+] Running recon on example.com
[+] Resolved IP: 93.184.216.34
[+] Scanning target: example.com
...
[+] Testing for basic XSS on example.com
[!] XSS vulnerability detected!
[+] Generating report for example.com
```

A report file will be saved in the current directory as:

```
example_com_report.txt
```

---

## 📚 Payload Configuration

The tool uses a JSON file for storing payloads:

```json
{
  "xss": ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"],
  "sqli": ["' OR '1'='1", "'; DROP TABLE users; --"]
}
```

You can customize this file at `data/payloads.json` to include additional XSS or SQLi payloads.

---

## 🔮 Planned Enhancements

- Subdomain enumeration
- CMS and technology fingerprinting
- SQLi testing using SQLMap integration
- HTML/PDF report generation
- Shodan/Censys passive recon support

---

## ⚠️ Disclaimer

This tool is provided for **educational and authorized testing purposes only**. Do not use RedFox on systems you do not own or have explicit permission to test.

---

## 📂 Metadata

**Repository:** `windro-exe/redfox`  
**Files analyzed:** `8`  
**Directory:** `windro-exe-redfox`  
**Report Digest Link:**  
[https://gitdocs1.s3.amazonaws.com/digests/windro-exe-redfox/fb87cc8b-81b8-4499-b75c-ab486156ad28.txt](https://gitdocs1.s3.amazonaws.com/digests/windro-exe-redfox/fb87cc8b-81b8-4499-b75c-ab486156ad28.txt)
