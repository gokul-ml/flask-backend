from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Backend Running</h1>"

@app.route("/dashboard")
def dashboard():
    return "<h2>📊 Student Monitoring Dashboard</h2>"

if __name__ == "__main__":
    app.run()