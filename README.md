# decryptage-AES
ESP32 MQTT subscriber that receives AES-CBC encrypted sensor data, decrypts it in real time, and displays the result on an SSD1306 OLED screen.

A MicroPython-based IoT project simulated on Wokwi. This ESP32 device acts as the receiver in a secure MQTT communication system. It subscribes to a topic on test.mosquitto.org, receives AES-CBC encrypted temperature and humidity payloads published by a separate sender device, decrypts them using a shared key and IV, and displays the plaintext result on an SSD1306 OLED screen in real time.
