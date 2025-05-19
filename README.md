# 🎯 Phishing Attack Simulator

This project is a **phishing simulation web application** built using Flask. It is designed for **internal security testing and training**, allowing ethical red teamers or security analysts to test user susceptibility to phishing attacks in a controlled environment.

> ⚠️ **Legal Notice**: This tool is for authorized use only. You must have explicit permission from your organization or client to use this tool in a testing environment.

---

## 🧰 Features

- Simple fake login form with email and password fields.
- Backend captures and logs credentials along with IP and User-Agent.
- Redirects to a decoy website after submission.
- Styled frontend with realistic-looking login interface.

---

## 📁 Project Structure

phishing_sim/
├── app.py
├── cred.txt # Captured credentials log
├── templates/
│ └── login.html # Login form
├── static/
│ ├── style.css # Styling for the form
│ └── script.js # Optional frontend logic
├── venv/ # Python virtual environment
└── README.md


---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/saumyakumar07/phishing-simulator.git
cd phishing-simulator 

### 2. Set Up Environment
