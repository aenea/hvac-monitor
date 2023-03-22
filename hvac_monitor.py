#!/usr/bin/python

import paho.mqtt.client as mqtt
import json

# create a publish callback function
def on_publish(client, userdata, result):
    pass


# create a config entry for the house hvac return temperature
config = {}
config['device_class'] = 'temperature'
config['entity_id'] = 'hvac_house_return_temperature'
config['icon'] = 'mdi:hvac'
config['unique_id'] = 'hvac_house_return_temperature'
config['name'] = 'house_hvac_return_temperature'
config['state_class'] = 'measurement'
config['suggested_display_precision'] = 1
config['unit_of_measurement'] = '°F'
config['state_topic'] = 'homeassistant/sensor/' + config['unique_id'] + '/state'

# create a mqtt client
client = mqtt.Client('pi-hvac')
client.connect('mqtt-01.aenea.org')
client.on_publish = on_publish

client.publish('homeassistant/sensor/' + config['unique_id'] + '/config', json.dumps(config), retain=True)
#client.publish('homeassistant/sensor/' + config['unique_id'] + '/config', '')

# read the supply and return temperatures from the 1wire temperature probes
#tempSupply = float(open("/mnt/1wire/28.BC224A060000/temperature12", "r").read())
#tempReturn = float(open("/mnt/1wire/28.2A514A060000/temperature12", "r").read())

#tempSupply = (tempSupply * 1.8) + 32
#tempReturn = (tempReturn * 1.8) + 32

# publish the data to the mqtt server
#client.publish("hvac/return", tempReturn)
#client.publish("hvac/supply", tempSupply)

client.disconnect()
