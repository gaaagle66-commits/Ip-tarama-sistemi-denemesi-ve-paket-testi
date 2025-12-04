import socket
import subprocess

# --------------------------
# TCP TARAYICI
# --------------------------
def tcp_scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.4)
        result = s.connect_ex((ip, port))
        s.close()

        if result == 0:
            return f"[AÇIK] TCP Port: {port}"
        else:
            return f"[KAPALI] TCP Port: {port}"
    except:
        return f"[HATA] TCP Port: {port}"


# --------------------------
# UDP TARAYICI
# --------------------------
def udp_scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.4)

        s.sendto(b"", (ip, port))
        try:
            data, addr = s.recvfrom(1024)
            return f"[AÇIK/CEVAP] UDP Port: {port}"
        except socket.timeout:
            return f"[CEVAP YOK] UDP Port: {port}"
    except:
        return f"[HATA] UDP Port: {port}"


# --------------------------
# PING TESTİ
# --------------------------
def ping_test(ip):
    try:
        res = subprocess.check_output(["ping", "-c", "3", ip], stderr=subprocess.STDOUT)
        return res.decode()
    except:
        return "Ping başarısız."
