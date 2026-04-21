from machine import Pin, I2C,Timer
from time import sleep
import ssd1306
import network 
from umqtt.simple import MQTTClient
from ucryptolib import aes

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    print(".", end="")
    sleep(0.1)
print(" Connected!")
print("Network config:", sta_if.ifconfig())
tim=Timer(1)
MQTT_CLIENT_ID="AES-RECEIVER "
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC_AES = "CRYPT/AES"



key = b'anfel-fgh-145-lkj-anfel-45-sakni'
iv = b'secret-iv-123456' 

MODE_CBC = 2


i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
def on_message(topic,mssg):
    print("topic: {}".format(topic))
    encrypted= eval(mssg)
    decipher = aes(key, MODE_CBC, iv)
    decrypted = decipher.decrypt(encrypted)
    result = decrypted.decode().strip()
    print('Decrypted: {}'.format(decrypted.strip()))
    oled.fill(0)
    oled.text("Decrypted:", 0, 0)
    oled.text(result[:16], 0, 16)   
    oled.show()

client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
client.set_callback(on_message)
client.connect()
client.subscribe(MQTT_TOPIC_AES)
print('Sebscribed to %s' % MQTT_TOPIC_AES)

while True:
    client.check_msg()
    sleep(0.1)
   
    