#!/usr/bin/python

import paho.mqtt.client as mqtt
import json
import socket
import time

RETURN_UNIQUE_ID = 'hvac_house_return_temperature'
SUPPLY_UNIQUE_ID = 'hvac_house_supply_temperature'
TOPIC_PREFIX = 'homeassistant/sensor/'


# create a connection callback function
def on_connect(client, userdata, flags, result, properties=None):
    if (result == 0):
        # create a config entry for the house hvac return temperature
        config = {}
        config['unique_id'] = RETURN_UNIQUE_ID
        config['device_class'] = 'temperature'
        config['icon'] = 'mdi:hvac'
        config['name'] = 'house_hvac_return_temperature'
        config['state_class'] = 'measurement'
        config['state_topic'] = TOPIC_PREFIX + RETURN_UNIQUE_ID + '/state'
        config['suggested_display_precision'] = 1
        config['unit_of_measurement'] = '°F'

        client.publish(TOPIC_PREFIX + RETURN_UNIQUE_ID + '/config', json.dumps(config), retain=True, properties=None)

        # create a config entry for the house hvac supply temperature
        config = {}
        config['unique_id'] = SUPPLY_UNIQUE_ID
        config['device_class'] = 'temperature'
        config['icon'] = 'mdi:hvac'
        config['name'] = 'house_hvac_return_temperature'
        config['state_class'] = 'measurement'
        config['state_topic'] = TOPIC_PREFIX + SUPPLY_UNIQUE_ID + '/state'
        config['suggested_display_precision'] = 1
        config['unit_of_measurement'] = '°F'

        client.publish(TOPIC_PREFIX + SUPPLY_UNIQUE_ID + '/config', json.dumps(config), retain=True, properties=None)


# create a mqtt client
client = mqtt.Client(client_id=socket.getfqdn(), transport='tcp', protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.connect('mqtt-01.aenea.org', 1883, properties=None)
client.loop_start()

while True:
    try:
        # read the supply and return temperatures from the 1wire temperature probes
        tempSupply = float(open("/mnt/1wire/28.BC224A060000/temperature12", "r").read())
        tempReturn = float(open("/mnt/1wire/28.2A514A060000/temperature12", "r").read())

        # convert to F
        tempSupply = (tempSupply * 1.8) + 32
        tempReturn = (tempReturn * 1.8) + 32

        # publish the data to the mqtt server
        client.publish(TOPIC_PREFIX + RETURN_UNIQUE_ID + '/state', tempReturn)
        client.publish(TOPIC_PREFIX + SUPPLY_UNIQUE_ID + '/state', tempSupply)

        time.sleep(30)
    except:
        client.loop_stop()
        client.disconnect()
        break
