#  ESP32 AES-256 MQTT Receiver — Secure IoT Decryption Node

A MicroPython-based IoT project running on an **ESP32** that subscribes to an MQTT topic, receives AES-256-CBC encrypted payloads, decrypts them in real time, and displays the results on an **SSD1306 OLED screen**.

>  Fully simulated on Wokwi — no hardware required to run it.

> This project is the **receiver side** of a two-node secure IoT communication system. See the [sender node](https://github.com/Sakni-Anfel/cryptage-AES) for the full picture.

---

## Data flow:
1. Sender node encrypts sensor data and publishes to `CRYPT/AES` topic
2. This receiver subscribes to `CRYPT/AES` and receives the encrypted payload
3. AES-256-CBC decryption is applied using the shared key and IV
4. Decrypted plaintext (temperature & humidity) is displayed on the OLED

---

## Demo

> Add a screenshot of your Wokwi simulation running here

---

##  Hardware

| Component | Description |
|-----------|-------------|
| ESP32 DevKit C v4 | Main microcontroller (Wi-Fi enabled) |
| SSD1306 OLED | 128×64 I2C display — SDA: GPIO 21, SCL: GPIO 22 |

> No DHT22 sensor on the receiver — it only decrypts and displays.

---

##  Dependencies

| Library | Purpose |
|---------|---------|
| `ucryptolib` | Built-in MicroPython AES decryption |
| `umqtt.simple` | MQTT client for MicroPython |
| `ssd1306` | OLED display driver |
| `network` | Wi-Fi management |

---

##  Getting Started

### Run on Wokwi (no hardware needed)

Copy the `diagram.json` into a new Wokwi project with `main.py` and `ssd1306.py`, then press ▶.

Make sure the **sender node** is also running so there are messages to receive.

### Run on real hardware

1. Flash MicroPython firmware onto your ESP32
2. Upload `main.py` and `ssd1306.py` using [Thonny](https://thonny.org/) or `mpremote`
3. Update Wi-Fi credentials in `main.py`:
```python
sta_if.connect('YOUR_SSID', 'YOUR_PASSWORD')
```
4. Make sure the key and IV match exactly with the sender:
```python
key = b'anfel-fgh-145-lkj-anfel-45-sakni'  # 32 bytes
iv  = b'secret-iv-123456'                   # 16 bytes
```
5. Monitor output via serial terminal at 115200 baud

---

##  Security Details

| Parameter | Value |
|-----------|-------|
| Algorithm | AES-256-CBC |
| Key size | 256 bits (32 bytes) |
| IV size | 128 bits (16 bytes) |
| Library | `ucryptolib` (built-in MicroPython) |

**Note:** The key and IV are hardcoded and shared between sender and receiver. This is symmetric encryption — both nodes must use identical key/IV. In a production system, use a secure key exchange protocol and a fresh random IV per message.

---

##  MQTT

| Parameter | Value |
|-----------|-------|
| Broker | `test.mosquitto.org` (public) |
| Topic | `CRYPT/AES` |
| Mode | **Subscribe** (receiver) |

Manually publish a test message to verify decryption:
```bash
mosquitto_pub -h test.mosquitto.org -t "CRYPT/AES" -m "<encrypted_bytes>"
```

---

##  Project Structure

```
aes-receiver/
├── main.py          # Main application — subscribe, decrypt, display
├── ssd1306.py       # OLED display driver
├── diagram.json     # Wokwi circuit diagram
└── README.md
```

---

##  Full System: Sender + Receiver

| Node | Repo | Role |
|------|------|------|
| Sender | [cryptage-AES](https://github.com/Sakni-Anfel/cryptage-AES) | Reads DHT22, encrypts, publishes |
| Receiver | this repo | Subscribes, decrypts, displays |

Both nodes use the same AES-256-CBC key and IV, communicating through a public MQTT broker.

---

##  What This Project Demonstrates

- AES-256-CBC decryption on a microcontroller
- MQTT subscribe pattern in MicroPython
- Symmetric key communication between two ESP32 nodes
- I2C peripheral management (OLED display)
- Real-time secure IoT data reception and display

---

##  License

MIT License — feel free to use, modify, and distribute.

---

##  Author

**Anfel Sakni** — Embedded Systems Engineering Student
🔗 [GitHub](https://github.com/Sakni-Anfel)
