Fancy Example
==========

If you're using this example, it's important that you download
the entire "fancy" folder off of GitHub. 

To make this run, you will need to find your Product ID and Vendor ID and replace the one in the [main.py](main.py) file
with your own. The instructions for this are in the [YouTube tutorial](https://www.youtube.com/watch?v=NeapS5Jn_oo) for this library.

You will also need to replace the unique_id currently there with **the username** of the TikTok creator you want to print off of.

After that, you should just be able to run.

Receiving an Invalid Endpoint error with a USB printer? Try adding “in_ep = 0x81, out_ep = 0x03" to the create_usb function!
If you are not receiving this error, do not add the additional parameters! If you continue to receive this error, make a ticket & we will handle it together!