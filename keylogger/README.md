# 📝 simple_keylogger.py

![Project: Educational](https://img.shields.io/badge/purpose-educational-blue.svg)
![Language: Python](https://img.shields.io/badge/language-Python-green.svg)

> **Simple, minimal proof-of-concept (POC)** keylogger written in Python using `pynput`.  
> Designed for learning and defensive research — **not** for covert or malicious use.

---

## 🔎 What this script does

`simple_keylogger.py` listens to keyboard events and appends keystrokes to a log file (`keylog.txt`).  
It handles printable characters, space and enter keys, and records special keys in square brackets (e.g. `[shift]`). Press **ESC** to stop the listener.

This script is intentionally minimal to demonstrate how keystroke capture works and to help defenders understand detection and mitigation.

---

## ⚠️ Legal & Ethical Notice (READ FIRST)

**DO NOT** use this script on devices, accounts, or networks that you do not own or have explicit, written permission to test.  
Unauthorized keylogging is often illegal and a serious invasion of privacy.

By using this code you agree to follow all local laws and organizational policies. The author accepts **no responsibility** for misuse.

---

## ✅ Quickstart

### Prerequisites
- Python **3.8+**
- `pynput` library

Install dependency:
```bash
python -m pip install --user pynput
```

Run the keylogger
```
python simple_keylogger.py
```

You will see:
```vbnet
Starting keylogger. Press ESC to stop.
```

Keystrokes will be appended to `keylog.txt` in the same directory. Press ESC to stop the logger.

## 🗂️ Log format examples

- Typing `Hello World` → file content:

```nginx
Hello World
```

- Pressing Enter → a newline is recorded.

- Special keys recorded like:

```css
[shift]a[shift] [enter] [tab]
```

## 🔧 Notes & Best Practices (for educational use)

- Run the script in an isolated environment (VM or lab machine) when testing.

- Use a virtual environment:
  
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
pip install pynput
```

- Keep logs secure and delete them after analysis. Never store logs in a public repository.

- Consider modifying the script to run only for a limited duration or to require explicit confirmation before recording.

## 🛡️ Defensive suggestions (learners & defenders)

If you are studying this to improve defenses, consider exploring:

- Endpoint detection rules for pynput usage or unexpected persistent listeners.

- File integrity monitoring for unauthorized log files (e.g., keylog.txt).

- Process and autorun detection for suspicious Python scripts.

- Application whitelisting and strict user privilege separation.

## 🧾 Frequently Asked Questions (FAQ)

Q: Can this capture passwords?<br>
A: Yes — if run while a user types passwords, the keystrokes will be recorded. That’s why strict ethical constraints apply.

Q: Is pynput cross-platform?<br>
A: pynput supports Windows, macOS and many Linux distributions, but behavior/permissions can vary by OS.

Q: How do I stop the script?<br>
A: Press ESC in the environment where the script is running.

## 🛠️ Possible improvements (ideas)

- Add CLI flags for `--output`path, `--duration` (seconds), and `--verbose`.

- Add optional timestamping and process/window context (for defensive analysis).

- Encrypt or safely handle log files (if used for legitimate research).

- Add a consent prompt and explicit logging of consent.

> These are suggestions for educational/defensive enhancements only.


## 🤝 Contributing & Contact

If you want to improve this POC for defensive/educational purposes, please open a PR with a clear description and emphasize ethical use. For security reports or questions, see `SECURITY.md`.


## 👨‍💻 Author

**Mantra Patil**

💼 LinkedIn: www.linkedin.com/in/mantrapatil25

✉ Email: techmantrapatil@gmail.com

---

***✨ Thanks for visiting my profile! ✨***






