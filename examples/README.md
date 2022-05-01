Examples
=========
Within this folder are various examples showcasing the TikTokPrinter library.

If you are looking for a plug & play example, use "fancy." It does pretty much everything
a normal printer stream does, and more.

If you want to learn how to customize this library yourself, check out the other examples.

### Current Examples

#### Paste & Go (Use right away)

- [Chat Commands (Ready-2-Go)](commands.py)
- [Fancy Printer (Ready-2-Go)](fancy)

#### Tutorial (Needs Customization)

- [Using Images (Tutorial)](images.py)
- [Basic Implementation (Tutorial)](basic.py)
- [Manually VID/PID (Tutorial)](manual.py)

### Contributing Examples

Create a [pull request](https://github.com/isaackogan/TikTok-Live-Connector/pulls) & I will add your example when I have free time!

### Troubleshooting: Invalid Endpoint Address 0x1

If you receive something like this:

```bash
  File "C:\Users\tiger\AppData\Local\Programs\Python\Python310\lib\site-packages\usb\core.py", line 986, in write
    intf, ep = self._ctx.setup_request(self, endpoint)
  File "C:\Users\tiger\AppData\Local\Programs\Python\Python310\lib\site-packages\usb\core.py", line 113, in wrapper
    return f(self, *args, **kwargs)
  File "C:\Users\tiger\AppData\Local\Programs\Python\Python310\lib\site-packages\usb\core.py", line 228, in setup_request
    intf, ep = self.get_interface_and_endpoint(device, endpoint_address)
  File "C:\Users\tiger\AppData\Local\Programs\Python\Python310\lib\site-packages\usb\core.py", line 113, in wrapper
    return f(self, *args, **kwargs)
  File "C:\Users\tiger\AppData\Local\Programs\Python\Python310\lib\site-packages\usb\core.py", line 244, in get_interface_and_endpoint
    raise ValueError('Invalid endpoint address ' + hex(endpoint_address))
ValueError: Invalid endpoint address 0x3
```

Try adding “in_ep = 0x81, out_ep = 0x03" to the create_usb function! If you are not receiving this error, do not add the additional parameters! 
If you continue to receive this error, try doing out_ep = 0x02.

If that still doesn't work, make a ticket & we will handle it together!
