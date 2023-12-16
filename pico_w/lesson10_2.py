import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('iPhone','0987654321')

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
    
print(wlan.ifconfig())