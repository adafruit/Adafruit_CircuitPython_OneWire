
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-onewire/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/onewire/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_OneWire/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_OneWire/actions/
    :alt: Build Status

Classes for use in communicating with devices on a 1-Wire bus.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

**Note:** This library does **not** work on the Raspberry Pi as there is no kernel interface for it

Usage Example
=============

.. code-block:: python

    import board
    from adafruit_onewire.bus import OneWireBus
    ow_bus = OneWireBus(board.D2)
    devices = ow_bus.scan()
    for d in devices:
        print("ROM={}\tFamily=0x{:02x}".format(d.rom, d.family_code))


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/onewire/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_OneWire/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
