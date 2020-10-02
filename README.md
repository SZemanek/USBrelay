# USBrelay
Python library and command line to control "SainSmart" 16 Channel USB Serial Relay Board

This python library / command line utility is for controlling SainSmart brand 16 Channel USB Serial Relay Board  
SKU# 101-70-208  ASIN: B0793MZH2B

This device shows up as a USB->Serial device (at least on Linux).   On most linux distro's it will show up as '/dev/ttyUSB0' by default.

Command line example:

./pyUSBrelay.py ch01on ch02off ch03on 

You might need to adjust permissions on /dev/ttyUSB0 or run the script w/ sudo to make this work properly. 
