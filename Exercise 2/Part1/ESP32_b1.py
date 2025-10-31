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

count = 0
while True:
    msg = f"Hello #{count}"
    e.send(peer, msg)
    print(f"ESP B Đã gửi: {msg}")
    count += 1
    time.sleep(1)
