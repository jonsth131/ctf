#!/bin/bash

tshark -r klas.pcapng -T fields -e usbhid.data.axis.x -e usbhid.data.axis.y usb.src=="3.4.1" 2> /dev/null | python3 usb.py
