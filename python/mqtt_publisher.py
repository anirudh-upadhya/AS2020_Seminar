import paho.mqtt.publish as publish
import numpy as np
import time

MQTT_SERVER = "192.168.1.22"
MQTT_PATH = "test_channel"
while True:

    rand1 = np.random.randint(0,255)
    rand2 = np.random.randint(0,700)
    rand3 = np.random.randint(0,5)
    rand = str([rand1,rand2,rand3])
    publish.single(MQTT_PATH, rand, hostname=MQTT_SERVER)
    print(rand)
    time.sleep(2)