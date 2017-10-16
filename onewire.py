# 1-Wire driver for CircuitPython
# MIT license; Copyright (c) 2016 Damien P. George, Limor Fried

from micropython import const
import busio
from digitalio import DigitalInOut, Direction, Pull

class OneWireError(Exception):
    pass

class OneWire:
    SEARCH_ROM = const(0xf0)
    MATCH_ROM = const(0x55)
    SKIP_ROM = const(0xcc)

    def __init__(self, pin):
	self._ow = busio.OneWire(pin)

    def reset(self, required=False):
        reset = self._ow.reset()
        if required and reset:
            raise OneWireError
        return not reset

    def readbit(self):
        return self._ow.read_bit()

    def readbyte(self):
	val = 0
	for i in range(8):
	    val |= self._ow.read_bit() << i
        return val

    def readinto(self, buf):
        for i in range(len(buf)):
            buf[i] = self.readbyte()

    def writebit(self, value):
        return self._ow.write_bit(value)

    def writebyte(self, value):
	for i in range(8):
	    bit = (value >> i) & 0x1
	    self._ow.write_bit(bit)
        return 

    def write(self, buf):
        for b in buf:
            self.writebyte(b)

    def select_rom(self, rom):
        self.reset()
        self.writebyte(MATCH_ROM)
        self.write(rom)

    def scan(self):
        devices = []
        diff = 65
        rom = False
        for i in range(0xff):
            rom, diff = self._search_rom(rom, diff)
            if rom:
                devices += [rom]
            if diff == 0:
                break
        return devices

    def _search_rom(self, l_rom, diff):
        if not self.reset():
            return None, 0
        self.writebyte(SEARCH_ROM)
        if not l_rom:
            l_rom = bytearray(8)
        rom = bytearray(8)
        next_diff = 0
        i = 64
        for byte in range(8):
            r_b = 0
            for bit in range(8):
                b = self.readbit()
                if self.readbit():
                    if b: # there are no devices or there is an error on the bus
                        return None, 0
                else:
                    if not b: # collision, two devices with different bit meaning
                        if diff > i or ((l_rom[byte] & (1 << bit)) and diff != i):
                            b = 1
                            next_diff = i
                self.writebit(b)
                if b:
                    r_b |= 1 << bit
                i -= 1
            rom[byte] = r_b
        return rom, next_diff

    def crc8(self, data):
	#print("Calc CRC for ", data)
	crc = 0

	for byte in data:
	    #print("byte: 0x%02x" % byte)
	    crc ^= byte
	    for bit in range(8):
		if (crc & 0x01):
		    crc = ( crc >> 1 ) ^ 0x8C
		else:
		    crc >>= 1
	    crc &= 0xFF
	    #print("crc: 0x%02x" % crc)
	return crc
