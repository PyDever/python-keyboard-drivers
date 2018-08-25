
"""
See LICENSE for more information.
See README.md for building instructions
and usage examples.
"""

import evdev 	# coomunicate w/ kernel I/O interface
import sys		# access system calls

class DEVICE (object):

	def __init__ (self):

		self.device_file = '/dev/input/event5'

		# create kernel interface
		self.device = evdev.InputDevice(self.device_file)

	def _detach_kernel_driver (self):
		"""
		tell the kernel to relase control of the device
		"""
		self.device.grab()

	def _attach_kernel_driver (self):
		"""
		tell the kernel to take back control of the device
		"""
		self.device.ungrab()

	def _exit (self): 
		"""
		call the exit sys-call and cleanup
		"""
		self._attach_kernel_driver()
		sys.exit(0)

