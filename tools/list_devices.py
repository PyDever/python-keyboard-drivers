
"""
See LICENSE for more information.
See README.md for building instructions
and usage examples.
"""

import evdev 	# coomunicate w/ kernel I/O interface
import sys		# access system calls

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

# list the devices attached to the kernel I/O interface
for device in devices:
	print(device.path, device.name, device.phys)

# device.capabilities(verbose=True)

