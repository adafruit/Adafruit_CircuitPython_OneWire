# The MIT License (MIT)
#
# Copyright (c) 2017 Carter Nelson for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`OneWire Device`
====================================================

Provides access to a single device on the 1-Wire bus.

* Author(s): Carter Nelson
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_OneWire.git"

from micropython import const

_MATCH_ROM = const(0x55)

class OneWireDevice(object):
    """A class to represent a single device on the 1-Wire bus."""

    def __init__(self, bus, address):
        self._bus = bus
        self._address = address

    def __enter__(self):
        self._select_rom()
        return self

    def __exit__(self, *exc):
        return False

    def readinto(self, buf, **kwargs):
        """
        Read into ``buf`` from the device. The number of bytes read will be the
        length of ``buf``.

        If ``start`` or ``end`` is provided, then the buffer will be sliced
        as if ``buf[start:end]``. This will not cause an allocation like
        ``buf[start:end]`` will so it saves memory.

        :param bytearray buf: buffer to write into
        :param int start: Index to start writing at
        :param int end: Index to write up to but not include
        """
        self._bus.readinto(buf, **kwargs)
        if kwargs is None and len(buf) >= 8:
            if self._bus.crc8(buf):
                raise Exception('CRC error')

    def write(self, buf, **kwargs):
        """
        Write the bytes from ``buf`` to the device.

        If ``start`` or ``end`` is provided, then the buffer will be sliced
        as if ``buffer[start:end]``. This will not cause an allocation like
        ``buffer[start:end]`` will so it saves memory.

        :param bytearray buf: buffer containing the bytes to write
        :param int start: Index to start writing from
        :param int end: Index to read up to but not include
        """
        return self._bus.write(buf, **kwargs)

    def _select_rom(self):
        self._bus.reset()
        self.write(bytearray([_MATCH_ROM]))
        self.write(self._address.rom)
