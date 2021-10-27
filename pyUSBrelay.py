#!  /usr/bin/python3
import serial     # pip install pyserial 

relaycommands = {"ch01on": "3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A",
			 "ch01off": "3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A",
			 "ch02on": "3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A",
			 "ch02off": "3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A",
			 "ch03on": "3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A",
			 "ch03off": "3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A",
			 "ch04on": "3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A",
			 "ch04off": "3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A",
			 "ch05on": "3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A",
			 "ch05off": "3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A",
			 "ch06on": "3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A",
			 "ch06off": "3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A",
			 "ch07on": "3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A",
			 "ch07off": "3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A",
			 "ch08on": "3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A",
			 "ch08off": "3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A",
			 "ch09on": "3A 46 45 30 35 30 30 30 38 46 46 30 30 46 36 0D 0A",
			 "ch09off": "3A 46 45 30 35 30 30 30 38 30 30 30 30 46 35 0D 0A",
			 "ch10on": "3A 46 45 30 35 30 30 30 39 46 46 30 30 46 35 0D 0A",
			 "ch10off": "3A 46 45 30 35 30 30 30 39 30 30 30 30 46 34 0D 0A",
			 "ch11on": "3A 46 45 30 35 30 30 30 41 46 46 30 30 46 34 0D 0A",
			 "ch11off": "3A 46 45 30 35 30 30 30 41 30 30 30 30 46 33 0D 0A",
			 "ch12on": "3A 46 45 30 35 30 30 30 42 46 46 30 30 46 33 0D 0A",
			 "ch12off": "3A 46 45 30 35 30 30 30 42 30 30 30 30 46 32 0D 0A",
			 "ch13on": "3A 46 45 30 35 30 30 30 43 46 46 30 30 46 32 0D 0A",
			 "ch13off": "3A 46 45 30 35 30 30 30 43 30 30 30 30 46 31 0D 0A",
			 "ch14on": "3A 46 45 30 35 30 30 30 44 46 46 30 30 46 31 0D 0A",
			 "ch14off": "3A 46 45 30 35 30 30 30 44 30 30 30 30 46 30 0D 0A",
			 "ch15on": "3A 46 45 30 35 30 30 30 45 46 46 30 30 46 30 0D 0A",
			 "ch15off": "3A 46 45 30 35 30 30 30 45 30 30 30 30 46 46 0D 0A",
			 "ch16on": "3A 46 45 30 35 30 30 30 46 46 46 30 30 46 46 0D 0A",
			 "ch16off": "3A 46 45 30 35 30 30 30 46 30 30 30 30 46 45 0D 0A",
			 "allon": "3A 46 45 30 46 30 30 30 30 30 30 31 30 30 32 46 46 46 46 45 33 0D 0A",
			 "alloff": "3A 46 45 30 46 30 30 30 30 30 30 31 30 30 32 30 30 30 30 45 31 0D 0A"}

class RelayBoardConnection():
	#ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)  # open serial port
	serialPortPath = '/dev/ttyUSB0'

	def __init__(self, serialPortPath='/dev/ttyUSB0'):
		self.serialPortPath = serialPortPath
		self.ser = serial.Serial(port=self.serialPortPath, baudrate=9600)  # open serial port

	def __enter__(self):
		#print("__enter__ start")
		if not self.ser.isOpen():
			self.ser = serial.Serial(port=self.serialPortPath, baudrate=9600)  # open serial port
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		#print("__exit__")
		self.ser.close()  # close port

	def sendCommand(self, command):
		self.ser.write(bytes.fromhex(relaycommands[command]))

	def sendtestpattern(self):
		#ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600)  # open serial port

		#print(self.ser.name)  # check which port was really used



		while True:
			for command in relaycommands:
				#time.sleep(0.05)
				print(command)
				if (command != "allon") and (command != "alloff"):
					self.ser.write(bytes.fromhex(relaycommands[command]))


def main(argv):
	relayboard = RelayBoardConnection()
	for command in argv:
		assert command in relaycommands, "invalid command"
	for command in argv:
		relayboard.sendCommand(command)
		relayboard.sendCommand(command)  #send twice for reliability


if __name__ == "__main__":
	import sys
	main(sys.argv[1:])
