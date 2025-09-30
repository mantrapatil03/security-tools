# security-tools

**Security Tool** is a collection of lightweight Python utilities for **cybersecurity learning, awareness, and ethical testing**.  

It brings together multiple essential scripts — from password utilities to basic network reconnaissance — **all in one place.**  


It is a small collection of educational cybersecurity utilities written in Python. It's designed for learning, lab-testing, and ethical security practice. This repo combines of tools:

>*⚠️ **Disclaimer:** Important — Legal & Ethical Notice: These tools are for **educational and authorized use only**.*
> *Do not run them against systems, networks, or users you don't own or explicitly have permission to test.*
> *The author is not responsible for misuse.*



## 📦 Included Tools

1. **🖥️ [Keylogger (POC)](keylogger/)**  
   - Captures keystrokes and logs them for analysis.  
   - Intended **only for educational demonstration** of keylogging techniques and defense.  

2. **🔑 [Password Strength Checker](password_strength_checker/)**  
   - Evaluates passwords based on length, complexity, and common patterns.  
   - Provides feedback and suggestions for stronger security.  

3. **🔒 [Password Generator](password_generator/)**  
   - Creates strong, random passwords.  
   - Supports custom length, symbols, numbers, and clipboard copy.  

4. **🌐 [Port Scanner](port_scanner/)**  
   - Scans ports on a given host to identify open services.  
   - Useful for basic **network reconnaissance** and awareness.  

---

## 🚀 Quick Start

**Installation**

Requirements:

``Python 3.8+``

``Git (optional)``

Clone the repo:
```
git clone https://github.com/mantrapatil03/security-tool.git
cd security_tool
```

Create and activate a virtual environment (recommended):
```
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Install optional dependencies:
```
pip install -r requirements.txt
```

requirements.txt is optional — see each tool for specific dependencies.

## Repo structure
```
security_tool/
├─ keylogger/
│  ├─ keylogger.py
│  └─ README.md
├─ password_strength_checker/
│  ├─ checker.py
│  └─ README.md
├─ password_generator/
│  ├─ generator.py
│  └─ README.md
├─ port_scanner/
│  ├─ scanner.py
│  └─ README.md
├─ .gitignore
├─ README.md        
├─ SECURITY.md
├─ requirements.txt

```

## 🔒 Security Policy

Please see `SECURITY.md`

for how to report vulnerabilities.
 
We follow responsible disclosure guidelines.

## 🤝 Contributing

If you want to contribute:

  -Fork the repo

  -Create a feature branch (`git checkout -b feat/my-feature`)

  -Add tests / docs

  -Submit a Pull Request with a clear description and testing steps

  -Be sure to follow the ethical guidelines: contributions that enable malicious behaviour without educational context may be rejected.






## 👨‍💻 Author

**Mantra Patil**

💼 LinkedIn: www.linkedin.com/in/mantrapatil25

✉ Email: techmantrapatil@gmail.com












---
**✨ Learn. Test. Secure. — with Security Tool.**
