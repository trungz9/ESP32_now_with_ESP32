import network
import espnow
import time


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(channel=1)
wlan.disconnect()

e = espnow.ESPNow()
e.active(True)

peer = b'\x24\x7A\x20\x51\xF3\xB0'   
e.add_peer(peer)

print("ESP32 A sẵn sàng...\n")


while True:
    sensor_value = 25.4
    msg = f"Sensor={sensor_value}"

    e.send(peer, msg)
    print(f"📤 Đã gửi: {msg}")
    
    start_time = time.ticks_ms()
    while True:
        host, rmsg = e.recv()
        if rmsg:
            print(f"Nhận phản hồi từ {host.hex()}: {rmsg.decode()}")
            break
        if time.ticks_diff(time.ticks_ms(), start_time) > 2000:
            print("Không nhận được ACK trong 2 giây.")
            break
    
    time.sleep(2)
