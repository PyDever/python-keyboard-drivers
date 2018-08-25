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

## Using the keyboard driver
To use this simple device driver, you must first run the following command
in the source directory.
```shell
$ make build
```
