from TikTokPrinter import TikTokPrinterClient, EscposEngineGenerator, TikTokMedia

client: TikTokPrinterClient = TikTokPrinterClient(
    unique_id="USERNAME_HERE",
    engine=EscposEngineGenerator.create_usb(
        vendor_id=0x1234,  # Manually input a vendor ID
        product_id=0x1234,  # Manually input a product ID
        auto_find=True,  # Automatically find your printer if vendor id & product id are invalid
        align="center"
    )
)


if __name__ == '__main__':
    """
    
    [MANUALLY FIND PRINTER]

    Not keen on auto_find? Use the USBDeview, or auto_find, to determine your printer's vendor ID and product ID.
    If you include them as parameters in create_usb, TikTokPrinter will first try to connect using them
    before automatically finding your printer, so you don't have to pick each time.
    
    [INVALID ENDPOINT ADDRESS]
    
    Receiving an Invalid Endpoint error with a USB printer?

    Try adding “in_ep = 0x81, out_ep = 0x03" to the create_usb function!
    If you are not receiving this error, do not add the additional parameters!
    If you continue to receive this error, try doing out_ep = 0x02. 

    If that still doesn't work, make a ticket & we will handle it together!

    """

    client.run()
