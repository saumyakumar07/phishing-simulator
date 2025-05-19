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
git clone https://github.com/yourusername/phishing-simulator.git
cd phishing-simulator
```
 
### 2. Set Up Environment

python3 -m venv venv
source venv/bin/activate.fish  # For Fish shell
# Or for Bash/Zsh:
# source venv/bin/activate

### 3. Install Dependencies

pip install Flask

### 4. Run the App
python3 app.py

Navigate to: http://127.0.0.1:5000

✍️ Captured Data
Captured credentials are saved in cred.txt in the following format:


2025-05-19 12:34:56 | IP: 192.168.1.10 | UA: Mozilla/5.0 ... | Username: user@example.com | Password: password123

🛡️ Ethical Use
This tool is meant for training, awareness, and controlled red team simulations. Never deploy or use this tool against systems or users without explicit written consent.

📃 License
This project is licensed under the MIT License.
