#!/usr/bin/python

import paho.mqtt.client as mqtt

# create a mqtt client
client = mqtt.Client('pi-hvac')
client.connect('mqtt-01.aenea.org')

# read the supply and return temperatures from the 1wire temperature probes
tempSupply = float(open("/mnt/1wire/28.BC224A060000/temperature12", "r").read())
tempReturn = float(open("/mnt/1wire/28.2A514A060000/temperature12", "r").read())

tempSupply = (tempSupply * 1.8) + 32
tempReturn = (tempReturn * 1.8) + 32

# publish the data to the mqtt server
client.publish("hvac/return", tempReturn)
client.publish("hvac/supply", tempSupply)

client.disconnect()
