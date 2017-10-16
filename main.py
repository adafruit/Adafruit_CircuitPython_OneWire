import board
import time
import OneWire
import ds18x20

ow =  OneWire.OneWire(board.D2)
ds18 = ds18x20.DS18X20(ow)

print("Resetting!",ow.reset())

print("Found the following 1-Wire devices: ", end="")
for dev in ow.scan():
    address = ''.join('{:02x}'.format(x) for x in dev)
    print(address)

print("Found the following DS18x20 devices: ", end="")
for dev in ds18.scan():
    address = ''.join('{:02x}'.format(x) for x in dev)
    print(address)

while True:
    for dev in ds18.scan():
	print(ds18.read_temp(dev))
