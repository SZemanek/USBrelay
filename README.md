# USBrelay
Python library and command line to control "SainSmart" 16 Channel USB Serial Relay Board

This python library / command line utility is for controlling:

SainSmart brand 16 Channel USB Serial Relay Board  

SKU# 101-70-208  ASIN: B0793MZH2B

Wiki: http://wiki.sainsmart.com/index.php/101-70-208 

Vendor Documentation: http://s3.amazonaws.com/s3.image.smart/download/101-70-208/101-70-208.zip 

The vendor documentation is very poor.
This board usually does not have a model number on it.  It is a white PCB, labeled "SainSmart:  Power to the makers" and islabeled "Serial Relay".



There is a jumper on the board "USB/COM" which controls where the power to the board comes from. (USB or "common" DC input) you might want to run this board off a separate DC power source if turning off the relays unexpectedly would cause a problem.  


WARNING: This board sometimes will miss a command and the relay won't engage properly.  As a lazy workaround, in the command line version, I send each command twice.  

This device shows up as a USB->Serial device (at least on Linux).   On most linux distro's it will show up as '/dev/ttyUSB0' by default.

If you need to run multiple USB relay board from the same computer (or have other USB->Serial Devices), try using "/dev/serial/by-path/____________" instead of /dev/ttyUSB0  that will be a symbolic link that should be tied to a specific USB port on the computer. 

The sainsmart supplied documentation included a serial command for "Status" and "Status Return Value" and I've never been able to make sense of the values it actually returned.  


Command line usage example:

./pyUSBrelay.py ch01on ch02off ch03on 

You might need to adjust permissions on /dev/ttyUSB0 or run the script w/ sudo to make this work properly. 



Other similar projects: 
See ldnelso2's SainSmart Python Library here https://github.com/ldnelso2/sainsmart he's got more information there. 
