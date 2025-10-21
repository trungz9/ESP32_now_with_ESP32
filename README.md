# ESP32_now_with_ESP32

# 🧠 Bài tập 1: ESP32 Wi-Fi Client (Station Mode)

Tài liệu này mô tả bài tập thực hành với **ESP32**:  
Kết nối vào mạng Wi-Fi hiện có (station mode), nhận IP qua DHCP,  
và hoạt động như **TCP client** để gửi dữ liệu đến server (PC).  
Code còn hỗ trợ nhận chuỗi từ Serial Monitor và chuyển tiếp lên server.

---

### 🎯 Qua bài tập:
- Hiểu cách **ESP32** kết nối Wi-Fi và nhận IP DHCP.  
- Quan sát kết nối **TCP** đến server và gửi dữ liệu.  
- Theo dõi việc chuyển tiếp dữ liệu từ Serial Monitor lên server.

---

## 💻 Mã nguồn hoàn chỉnh (ESP32 Arduino Sketch)
```cpp
#include <WiFi.h>

const char* ssid = "W_I_F_I";
const char* password = "P_A_S_S";

// TCP server
const char* host = "IP_PC";
const uint16_t port = 5000;

WiFiClient client;

void setup() {
  Serial.begin(115200);
  delay(1000);
}
