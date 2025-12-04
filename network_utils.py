import socket
import subprocess
import time

# -------------------------------------------------
# TCP TARAYICI
# -------------------------------------------------
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


# -------------------------------------------------
# UDP TARAYICI
# -------------------------------------------------
def udp_scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.4)
        s.sendto(b"", (ip, port))
        try:
            s.recvfrom(1024)
            return f"[AÇIK/CEVAP] UDP Port: {port}"
        except socket.timeout:
            return f"[CEVAP YOK] UDP Port: {port}"
    except:
        return f"[HATA] UDP Port: {port}"


# -------------------------------------------------
# PAKET TESTİ (TCP / UDP)
# -------------------------------------------------
def packet_test(ip, port, protocol, packet_count, byte_size):
    logs = []
    data = b"A" * byte_size

    for i in range(packet_count):
        try:
            if protocol == "tcp":
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.3)
                s.connect((ip, port))
                s.sendall(data)
                s.close()
                logs.append(f"[{i+1}] TCP paket gönderildi ({byte_size} byte)")

            elif protocol == "udp":
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(data, (ip, port))
                logs.append(f"[{i+1}] UDP paket gönderildi ({byte_size} byte)")
        except:
            logs.append(f"[{i+1}] HATA → Paket gönderilemedi")

        time.sleep(0.05)

    return logs


# -------------------------------------------------
# PING TESTİ
# -------------------------------------------------
def ping_test(ip):
    try:
        res = subprocess.check_output(["ping", "-c", "3", ip], stderr=subprocess.STDOUT)
        return res.decode()
    except:
        return "Ping başarısız."
