
"""
See LICENSE for more information.
See README.md for building instructions
and usage examples.
"""

import evdev 		# coomunicate w/ kernel I/O interface
import sys			# access system calls
import interface 	# communicate w/ kernel I/O interface
import device 	 	# create efficient device modules

def list_devices ():
	interface_communicator = interface.INTERFACE()
	return interface_communicator._read_devices(interface_communicator)

class KEYBOARD_DRIVER (device.DEVICE):

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

keyboard_driver = KEYBOARD_DRIVER()

keyboard_driver._detach_kernel_driver()
keyboard_driver._write_keyb_events()
keyboard_driver._exit()

