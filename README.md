# DVWA Brute Force Tool 🔐

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Security](https://img.shields.io/badge/security-educational-red.svg)](https://owasp.org)

## 📝 Description
Automated dictionary attack tool for DVWA (Damn Vulnerable Web Application) login testing. Performs credential brute-forcing with error handling and SSL bypass.

## 🎯 Features
- ✅ SSL certificate bypass for self-signed certificates
- ✅ Multi-language error detection (English/Arabic)
- ✅ Timeout protection (5 seconds)
- ✅ Progress tracking with attempt counter
- ✅ Connection error handling
- ✅ Arabic/English output support

## 🛠️ Technologies Used

### Programming Language
- **Python 3.7+** - Core programming language

### Libraries & Modules
| Library | Purpose |
|---------|---------|
| `requests` | HTTP requests handling |
| `urllib3` | SSL warning suppression |

### Built-in Modules
- `time` (implicit via timeout parameter)
- Exception handling system

## 📋 Requirements

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/dvwa-bruteforce.git
cd dvwa-bruteforce

# Install dependencies
pip install -r requirements.txt
```

## Prerequisites
Python 3.7 or higher

DVWA running locally (or authorized testing environment)

Wordlist file (passwords.txt)

## 🚀 Usage
Basic Usage
```bash
python dvwa_bruteforce.py
```

## Configuration
Edit the following variables in the script:

```python
target_url = "https://your-dvwa-ip/dvwa/login.php"
wordlist_path = "/path/to/your/passwords.txt"
```

## Expected Output
```text
[*] Attack on admin account launched...
[*] Trying passwords from passwords.txt file
[*] Attempt #1: Trying '123456'
[*] Attempt #2: Trying 'password'

[+] Success! Correct password --> admin
[+] Completed after 2 attempts
```
## ⚠️ Legal Disclaimer
FOR EDUCATIONAL PURPOSES ONLY

Use only on systems you own or have written permission to test

Unauthorized access to computer systems is illegal

The author assumes no liability for misuse

## 🏗️ Architecture
```text
┌─────────────┐     HTTP POST     ┌─────────────┐
│   Python    │ ──────────────────▶ │    DVWA     │
│   Script    │ ◀────────────────── │   Server    │
└─────────────┘     Response       └─────────────┘
       │                                    │
       │                                    │
   Wordlist                              Login
    File                               Validation
```

## 🔧 Troubleshooting
Issue	Solution
SSL Error	Verify verify=False is set
Connection refused	Check if DVWA is running
No password found	Expand your wordlist
Timeout errors	Increase timeout value

##📊 Performance
Average speed: ~1 request/second (with timeout)

Wordlist support: Unlimited line count

Memory usage: ~50MB for 1M passwords

##🤝 Contributing
Fork the repository

Create feature branch

Commit changes

Push to branch

Open Pull Request

## 📜 License
Distributed under MIT License. See LICENSE file.

##👤 Author
Security Researcher
Mina Safwat

## ⭐ Support
Give a ⭐ if this project helped you!

## 📚 Related Resources
OWASP Brute Force Attacks

DVWA Official

Python Requests Documentation
