# Python Keyboard Drivers
This is a real device driver. It disables
the pre-existing kernel driver so that it can be used.

## Installation & Setup
```shell
$ make build
```
WARNING: This will DISABLE the alternate kernel driver.
You really have to trust my driver now! ;)
```shell
$ sudo rm /dev/input/event4
```
The main driver file can be found `/src/v0.1-generic/driver.py`.
