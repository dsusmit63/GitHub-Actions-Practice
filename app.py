from flask import Flask, jsonify
import socket
import time

app = Flask(__name__)
start_time = time.time()

@app.route("/")
def home():
    return "Hello from Flask DevOps Demo!"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "uptime_seconds": int(time.time() - start_time)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
