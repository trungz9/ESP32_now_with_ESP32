import network
import espnow
import time

# --- Wi-Fi cấu hình ---
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(channel=1)
wlan.disconnect()

# --- ESP-NOW ---
e = espnow.ESPNow()
e.active(True)

print("ESP32 B sẵn sàng...\n")

while True:
    host, msg = e.recv()
    if msg:
        try:
            text = msg.decode()
        except:
            text = str(msg)
        print(f" Nhận từ {host.hex().upper()}: {text}")
        
        # --- Gửi lại ACK ---
        ack_msg = "Received"
        e.send(host, ack_msg)
        print(f"Gửi lại phản hồi: {ack_msg}")
    time.sleep(0.1)

