# Python Keyboard Drivers
In this repository I have a working Linux keyboard-driver written
in 100% pure Python 2.7. It replaces the current kernel driver and should
work on all Linux systems.

WARNING: While this driver acts as a stand-alone replacement, it is not reccomended
         to delte your kernel's drivers! They are still being used by other applications.
         
## Rolling your own build
First you must ensure that `git` is installed on your system.
```shell
$ sudo apt-get update && sudo apt-get install git
```
Second, you must download the source tarball. 
```shell
$ git clone https://github.com/PyDever/python-keyboard-drivers
```
If the first step did not work for some reason, use `curl` to download
the source tarball from GitHub.
```shell
$ curl -X GET https://github.com/PyDever/python-keyboard-drivers
```
Once you have a copy of the source un-compressed, and are in the 
source directory, go ahead and run this command to roll a build.
```shell
$ make build
```
The `build` folder contains your fresh fully-compiled build of my driver.

## Using the keyboard driver properly
To use this simple device driver, you must first run the following command
in the source directory.
```shell
$ make install
```
Awesome! Now you can use the device driver located at:
```
/python-keyboard-drivers/src/bin/v2.0/
```
The name of the file is `driver.py`.
Or, for a more stable release, use the driver in `.../bin/v1.0`.

## Using the keyboard driver as a library (not reccomended)
To use this driver as a Python 2.7 library, repeat the above process accept move
the following folder:
```
/python-keyboard-drivers/src/bin/v2.0/
```
(or a more stable release `.../bin/v1.0`) to this folder on Linux:
```
/usr/local/lib/python2.7/dist-packages/
```

