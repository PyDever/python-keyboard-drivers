# Python Keyboard Drivers
These are not user-space drivers! This is a real kernel driver. It disables
the pre-existing kernel driver so that it can be used.

## Installation
```shell
$ make build
```

## Driver Usage
```shell
$ sudo python src/driver.py
```
