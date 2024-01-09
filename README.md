# pyorayplug

Python Wrapper for Oray Smart Plug

## RunTested

- P1
- P1 Pro

## Usage

### Install requests

```shell
pip install requests
```

### Obtain (sn, key, time) from Oray's App

Use some HTTP capture tool with SSL decryption to capture the (sn, key, time) from Oray Plug API when using Oray's App.

You will see some URL like this:

```console
https://slapi.oray.net/plug?lang=en-US&country=en_CN&sn=323*********&_api=set_plug_status&status=1&key=a6******************************&time=01******&index=0
```

In this example:

```
sn=323*********
key=a6******************************
time=01******
```

### Obtain IP address of your smart plug

By checking your DHCP log or the web console of your router.

The DHCP hostname usually starts with "ESP_".

Assume the IP address of your plug is `192.168.0.2` in the next step.

### Write a simple Python script to test

```python
from pyorayplug import orayplug

myplug = orayplug(url="http://192.168.0.2:6767", sn="323*********", key="a6******************************", time="01******")
myplug.set(2, False) # Turn off plug index 2
print(myplug.query()) # Query status
# You will get output like: {0: True, 1: True, 2: False, 3: True}
myplug.set(2, True) # Turn on plug index 2
print(myplug.query()) # Query status
# You will get output like: {0: True, 1: True, 2: True, 3: True}
myplug.set(2, False) # Turn off plug index 2
```

## Note

If you want to control the plug from the internet through `slapi.oray.net` rather than the intranet, you also need to obtain a Bearer authentication code.

If you have any idea how to obtain the Bearer, PR is welcome.