import board
import time
import OneWire
import ds18x20

ow =  OneWire.OneWire(board.D2)
ds18 = ds18x20.DS18X20(ow)

def pretty_address(addr):
    return ''.join('{:02x}'.format(x) for x in addr)

print("Resetting, found anything?",ow.reset())

print("Found the following 1-Wire devices: ", end="")
for dev in ow.scan():
    print(pretty_address(dev))
print("")

while True:
    print("Found the following DS18x20 devices")
    for dev in ds18.scan():
	ds18.convert_temp()
	time.sleep(1)
	print(pretty_address(dev), ":", ds18.read_temp(dev))
    print("--------------")
    time.sleep(1)
