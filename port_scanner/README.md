# 🌐 Port Scanner

[![Language: Python](https://img.shields.io/badge/language-Python-3776AB.svg)](https://www.python.org/)  

A lightweight, educational TCP **port scanner** implemented in pure Python.  
Use it to quickly check a range of ports on a host to determine which services may be reachable. Designed for learning, lab testing, and basic reconnaissance in authorized environments.

---

## 🚀 Features
- Simple and self-contained — uses only Python's standard `socket` library.
- Scans a user-specified port range and reports **OPEN** / **closed** ports.
- Configurable timeout to avoid long waits on unresponsive ports.
- Clear, human-readable console output for quick inspection.

---

## ⚠️ Legal & Ethical Notice — READ FIRST
Scanning systems you do **not** own or do not have **explicit permission** to test can be illegal and unethical.  
**Do not** run this tool against third-party servers or networks without written authorization.

By using this script you confirm you have permission to scan the target. The author is not responsible for misuse.

---

## ✅ Quickstart

### Prerequisites
- Python 3.6+ (no external dependencies)

### Run the scanner
```bash
git clone https://github.com/<your-username>/security-tool.git
cd security-tool/port_scanner
python port_scanner.py
```

The script will prompt for:

- Target host (IP address or domain)

- Start port

- End port

### Example:
```yaml
Enter target host (IP or domain): example.com
Enter start port number: 7500
Enter end port number: 7510
```

### Output:
```vbnet
Scanning example.com from port 7500 to 7510...

Port 7500 is closed
Port 7501 is closed
Port 7502 is OPEN
...
```

## 🧰 Script Overview

File: `port_scanner.py`<Br>
Core function:
```python
def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # seconds
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0
```


Behavior:

- Attempts a TCP connect to each port in the specified range.

- Uses `connect_ex` which returns `0` on success (port open).

- Uses a short timeout to limit waiting on filtered/unresponsive ports.

### ⚙️ Configuration & Tips

- Increase `sock.settimeout(...)` if scanning slow or remote hosts.

- For faster scans across many ports, consider adding concurrency (threads or async IO) — see Improvements below.

- For production-grade scanning, professional tools (e.g., `nmap`) are recommended.

### 🔧 Suggested Improvements (for learning)

- Add CLI flags using `argparse` (e.g. `--host`, `--start`, `--end`, `--timeout)`.

- Implement worker threads (`concurrent.futures.ThreadPoolExecutor`) for concurrent scanning.

- Add port service name lookup using `socket.getservbyport`.

- Output results to a CSV or JSON report for automated analysis.

- Add rate limiting and polite scanning delays to avoid overwhelming targets.

## 🛡️ Defensive / Safety Notes

- Always whitelist the scanner in your own firewall rules when testing locally.

- Keep scan logs private and delete them after research.

- Avoid scanning production systems during business hours.



## 🤝 Contributing

Contributions are welcome — especially improvements that retain the script’s educational purpose and keep safety warnings prominent. Please:

- Fork the repo

- Create a feature branch (`git checkout -b feat/fast-scan`)

- Submit a pull request with tests and usage notes

## 📬 Contact / Security

For security issues or responsible disclosure, see `SECURITY.md` in the repository root.

## 👨‍💻 Author

**Mantra Patil**

💼 LinkedIn: www.linkedin.com/in/mantrapatil25

✉ Email: techmantrapatil@gmail.com

***“Security begins with curiosity and responsibility.” 🔍🧠***
