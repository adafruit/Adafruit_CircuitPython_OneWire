
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-OneWire/badge/?version=latest

    :target: https://circuitpython.readthedocs.io/projects/onewire/en/latest/

    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

Classes for use in communicating with devices on a 1-Wire bus.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block:: python

    >>> import board
    >>> from adafruit_onewire.bus import OneWireBus
    >>> ow_bus = OneWireBus(board.D2)
    >>> devices = ow_bus.scan()
    >>> for d in devices:
    ...     print("ROM={}\tFamily=0x{:02x}".format(d.rom, d.family_code))
    ...
    ROM=bytearray(b'(\xff\xc3\x80\xc2\x16\x04\xc6') Family=0x28

API Reference
=============

.. toctree::
   :maxdepth: 2

   api

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_OneWire/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

To build this library locally you'll need to install the
`circuitpython-travis-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block::shell

    python3 -m venv .env
    source .env/bin/activate
    pip install -r requirements.txt

Once installed, make sure you are in the virtual environment:

.. code-block::shell

    source .env/bin/activate

Then run the build:

.. code-block::shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-onewire --library_location .
