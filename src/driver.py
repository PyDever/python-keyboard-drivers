
"""
See LICENSE for more information.
See README.md for building instructions
and usage examples.
"""

import evdev 	# coomunicate w/ kernel I/O interface
import sys		# access system calls

class device_driver_module (object):

	def __init__ (self, device_file):
		"""
		initialize the device driver module
		"""
		self.device_file = device_file

		# create device comm. object
		self.device = evdev.InputDevice(
			self.device_file)

		# disable the default kernel driver
		self.device.grab()

		# file object for writing
		# to the device file

		# data structure to store 
		# device file operations
		"""required for kernel programming of any sort
		not actually used, however"""
		self.file_ops = {}

	def _exit (self, exit_code):
		"""
		cleanup and relase device control
		"""
		sys.stdout.flush(); self.device.ungrab()
		sys.exit(int(exit_code))


	def _read_keyb_events (self):
		"""
		push keyboard bytes to stdout
		"""
		if self.device and self.device_file:

			# okay... everything exists. we are g to g
			try:
				for keyb_event in self.device.read_loop():

					# check to make sure the byte is a key-code
					if keyb_event.type == evdev.ecodes.EV_KEY:

						print("%s" % keyb_event)

			except (OSError, Exception) as error_messge:
				sys.stdout.write("%s" % str(error_messge))

	def _write_keyb_events (self):
		dev_obj = evdev.UInput()
		"""
		write keyb bytes to the device file
		"""
		if self.device and self.device_file:

			# okay... everything exists. we are g to g
			try:
				for keyb_event in self.device.read_loop():

					# check to make sure the byte is a key-code
					if keyb_event.type == evdev.ecodes.EV_KEY:

						dev_obj.write(keyb_event.type, keyb_event.code, keyb_event.value)

			except (OSError, Exception) as error_messge:
				sys.stdout.write("%s" % str(error_messge))


module = device_driver_module('/dev/input/event5')

module._write_keyb_events()
module._exit(0)

