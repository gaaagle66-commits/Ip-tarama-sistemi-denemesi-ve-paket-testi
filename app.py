from flask import Flask, render_template, request
from network_utils import tcp_scan, udp_scan, ping_test

app = Flask(__name__)

PORT_LIST = [21, 22, 23, 53, 80, 443, 3306,8916,9000]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    ip = request.form["ip"]
    logs = []

    logs.append(f"Test edilen IP: {ip}\n")

    logs.append("\n--- TCP Port Sonuçları ---\n")
    for port in PORT_LIST:
        logs.append(tcp_scan(ip, port))

    logs.append("\n\n--- UDP Port Sonuçları ---\n")
    for port in PORT_LIST:
        logs.append(udp_scan(ip, port))

    logs.append("\n\n--- Ping Testi ---\n")
    logs.append(ping_test(ip))

    return render_template("result.html", logs=logs)

if __name__ == "__main__":
    print("Flask başlatılıyor...")
    app.run(host="0.0.0.0", port=5000, debug=True)
