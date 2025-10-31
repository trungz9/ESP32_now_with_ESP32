import network
import espnow
import time


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(channel=1)  
wlan.disconnect()


e = espnow.ESPNow()
e.active(True)

print("Gửi thông tin cho ESP32 A...\n")


while True:
    host, msg = e.recv()   
    if msg:  
        try:
            text = msg.decode()  
        except UnicodeDecodeError:
            text = str(msg)  
        print(f"ESP32 A Nhận từ {host.hex().upper()}: {text}")
    time.sleep(1)
