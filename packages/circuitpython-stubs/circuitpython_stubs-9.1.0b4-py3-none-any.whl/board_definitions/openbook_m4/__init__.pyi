# SPDX-FileCopyrightText: 2024 Justin Myers
#
# SPDX-License-Identifier: MIT
"""
Board stub for The Open Book Feather
 - port: atmel-samd
 - board_id: openbook_m4
 - NVM size: 256
 - Included modules: _asyncio, _bleio, _pixelmap, adafruit_bus_device, adafruit_pixelbuf, aesio, alarm, analogio, array, atexit, audiobusio, audiocore, audioio, audiomixer, audiomp3, binascii, bitbangio, bitmaptools, board, builtins, builtins.pow3, busdisplay, busio, busio.SPI, busio.UART, codeop, collections, countio, digitalio, displayio, epaperdisplay, errno, floppyio, fontio, fourwire, framebufferio, frequencyio, getpass, gifio, i2cdisplaybus, i2ctarget, io, json, keypad, keypad.KeyMatrix, keypad.Keys, keypad.ShiftRegisterKeys, locale, math, microcontroller, msgpack, neopixel_write, nvm, onewireio, os, os.getenv, paralleldisplaybus, ps2io, pulseio, pwmio, rainbowio, random, re, rgbmatrix, rotaryio, rtc, samd, sdcardio, select, sharpdisplay, storage, struct, supervisor, sys, terminalio, time, touchio, traceback, ulab, usb_cdc, usb_hid, usb_midi, vectorio, warnings, watchdog, zlib
 - Frozen libraries: 
"""

# Imports
import busio
import displayio


# Board Info:
board_id: str


# Pins:


# Members:
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """

def SPI() -> busio.SPI:
    """Returns the `busio.SPI` object for the board's designated SPI bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.SPI`.
    """

def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """

"""Returns the `displayio.EPaperDisplay` object for the board's built in display.
The object created is a singleton, and uses the default parameter values for `displayio.EPaperDisplay`.
"""
DISPLAY: displayio.EPaperDisplay


# Unmapped:
#   none
