#!/usr/bin/env python3

import urllib.request, json
import pdb
from pprint import pprint
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(8, gpio.OUT, initial = gpio.LOW)
gpio.setup(14, gpio.OUT, initial = gpio.LOW)
gpio.setup(15, gpio.OUT, initial = gpio.LOW)




from time import sleep

while(True):
    url = "https://apigateway.malankabn.by/central-system/api/v1/locations/map/info?locationId=02c8c27f-a830-454b-bf6a-cb2803964571"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    i=0
    for device in data['devices']:

        for connector in device['connectors']:
            status = False
            if(connector['typeEn'] == 'Plug Type2'):
                pprint(f"{i:} {connector['status']}")
                if connector['status'] == 'Available':
                    status = gpio.HIGH
                else:
                    status = gpio.LOW
                if i == 0:
                    pout = 8
                elif i == 1:
                    pout = 14
                else:
                    pout = 15

                gpio.output(pout,status)   
                i+=1
            #breakpoint()

    sleep(60)
