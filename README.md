# ESP32_now_with_ESP32

#  Bước 1: Xác định địa chỉ MAC của 2 con ESP32

Sử dụng Thonny IDE để xác định MAC của 2 con **ESP32**.
Ta có lần lượt địa chỉ MAC của ESP32 là:
-6c:c8:40:86:87:3c (gọi là **ESP32 A**)
-00:70:07:83:f4:34 (gọi là **ESP32 B**)
Đánh giấu và phân biệt được địa chỉ của 2 con **ESP32**

---

### 🎯 Qua đó:
- Hiểu cách **ESP32** kết nối với Thonny IDE  
- Phân biệt được 2 con **ESP32** từ địa chỉ MAC

---

## 💻 Mã nguồn hoàn chỉnh (ESP32 Thonny IDE)
```cpp
import network 

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Get MAC address (returns bytes)
mac = wlan.config('mac')

# Convert to human-readable format
mac_address = ':'.join('%02x' % b for b in mac)

print("MAC Address:", mac_address)

```

