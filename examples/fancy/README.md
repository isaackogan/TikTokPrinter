Fancy Example
==========

If you're using this example, it's important that you download
the entire "fancy" folder off of GitHub. 

To make this run, you will need to find your Product ID and Vendor ID and replace the one in the [main.py](main.py) file
with your own. The instructions for this are in the [YouTube tutorial](https://www.youtube.com/watch?v=NeapS5Jn_oo) for this library.

You will also need to replace the unique_id currently there with **the username** of the TikTok creator you want to print off of.

After that, you should just be able to run.

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