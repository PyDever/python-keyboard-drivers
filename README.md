# Python Keyboard Drivers
These are not user-space drivers! This is a real kernel driver. It disables
the pre-existing kernel driver so that it can be used.

## Installation & Setup
```shell
$ make build
```
WARNING: This will delte the alternate kernel driver.
You really have to trust my driver now! ;)
```shell
$ sudo rm /dev/input/event4
```

## Driver Usage
```shell
$ sudo python src/driver.py
```
