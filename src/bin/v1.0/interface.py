
"""
See LICENSE for more information.
See README.md for building instructions
and usage examples.
"""

import evdev 	# coomunicate w/ kernel I/O interface
import sys		# access system calls

class INTERFACE (object):

	def __init__ (self):

		self.device_file_paths = evdev.list_devices()
		self.devices = []

		for device_file_path in self.device_file_paths:
			temp_dev = evdev.InputDevice(device_file_path)

			self.devices.append(temp_dev)

	@property
	def _get_devices (self):
		"""
		grab from the interface all connected devices
		"""
		return self.devices 

	@staticmethod
	def _read_devices (self):
		"""
		show device properties such as 
		path, phys, and name
		"""
		for device in self.devices:
			print("%s    %s    %s" % (
				device.name, device.path, device.phys))

