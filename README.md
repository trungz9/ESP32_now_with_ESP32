# Thực hiện chức năng ESP-NOW

# Part1: Một chiều One-way (Sender → Receiver)

## Chức năng kiểm tra:  

- **ESP32 A**  gửi gói tin (ví dụ: "Hello" hoặc giá trị sensor) qua ESP-NOW.  
- **ESP32 B**  nhận gói tin và in ra Serial.  

### Mục tiêu: Sinh viên thấy cách ESP32 truyền thông tin không cần router/AP.  

*Bản thân sử dụng Thonny IDE để xác định MAC của 2 con **ESP32**.  
Ta có lần lượt địa chỉ MAC của ESP32 là:  
-6c:c8:40:86:87:3c (gọi là **ESP32 A**)  
-00:70:07:83:f4:34 (gọi là **ESP32 B**)  
Đánh giấu và phân biệt được địa chỉ của 2 con **ESP32***   

## Giải thích:

-`network, espnow, time`: Là những thư viện cung cấp để hoạt động **ESP-NOW**.
-`network.WLAN(network.STA_IF)`: Tạo đối tượng Wi-fi ở chế độ **Station**.
-`.disconnect()`: Ngắt kết nối Wi-fi để đảm bảo hoạt động đúng kênh tần số.
-`espnow.ESPnow()  
  e.active(TRUE)` khởi tạo, bật **ESP_NOW**  
  
### 💻 Mã code part1 (phần của ESP32 A) 
```py
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

```



# Part2: Hai chiều Two-way (Bidirectional)  

## Chức năng kiểm tra:

-ESP32 A gửi giá trị cảm biến sang ESP32 B.
-ESP32 B phản hồi bằng 1 ACK (ví dụ "Received").

### Mục tiêu: Hiểu cơ chế trao đổi dữ liệu hai chiều qua ESP-NOW.  

*Cần có 2 file và mỗi file nạp cho mỗi con ESP32, mỗi con ESP32 là cổng COM khác nhau.  
Và trong file chỉ ra địa chỉ MAC của ESP32 còn lại ở file khác*  

## Giải thích:  

-`sensor_value = 25.4`:Gán giá trị cảm biến
-`e.send(peer, msg)`: e là đối tượng ESP-NOW, peer là địa chỉ MAC.
-`host, rmsg = e.recv()`: Xác định địa chỉ MAC của thiết bị gửi và nội dung nhận được. Để trả về giá trị của đối tượng **e**
-` if time.ticks_diff(time.ticks_ms(), start_time) > 2000:
            print("Không nhận được ACK trong 2 giây.")
            break` :Nếu quá 2 giây, in dòng thông báo và thoát vòng chờ.  
  
## 💻 Mã code part 2(ESP32 A gọi ESP32 B)  
```py
import network
import espnow
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(channel=1)
wlan.disconnect()

e = espnow.ESPNow()
e.active(True)

peer = b'\x00\x70\x07\x83\xf4\x34'
e.add_peer(peer)

print("ESP32 A sẵn sàng...\n")


while True:
    sensor_value = 25.4
    msg = f"Sensor={sensor_value}"

    e.send(peer, msg)
    print(f"Đã gửi: {msg}")
    
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
```

# Part 3: Kết nối thiết bị đa chiều Multi-device (Broadcast/Multicast)  

## Chức năng kiểm tra:  

-Một ESP32 gửi broadcast gói tin đến nhiều ESP32 khác.
-Các ESP32 nhận đồng thời (có thể kiểm tra bằng nhiều board hoặc giả lập).

### Mục tiêu: Nắm được ESP-NOW thích hợp cho mạng mesh nhỏ hoặc cảm biến phân tán.
-***ESP32 A** đóng vai thiết bị phát sóng gửi bản tin cho **ESP32 B,C.**
-**ESP32 B và C** đóng vai thiết bị nhận broadcast, in ra tất cả tin gửi từ bất kỳ thiết bị nào trên cùng channel.*

## 💻 Mã code part 3 (của ESP32 A)
```py
import network
import aioespnow
import asyncio

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)
sta.disconnect()

e = aioespnow.AIOESPNow()
e.active(True)

broadcast_mac = b'\xff\xff\xff\xff\xff\xff'

async def send_broadcast():
    count = 0
    while True:
        msg = f"Broadcast message #{count}"
        await e.asend(broadcast_mac, msg)
        print(f"Sent: {msg}")
        count += 1
        await asyncio.sleep(2)

asyncio.run(send_broadcast())

```
## 💻 Mã code part 3 (của ESP32 B,C)  
```py
import network
import aioespnow
import asyncio

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)
sta.disconnect()

e = aioespnow.AIOESPNow()
e.active(True)

async def receive_messages():
    async for mac, msg in e:
        print(f"Received from {mac.hex().upper()}: {msg.decode()}")

asyncio.run(receive_messages())
```
