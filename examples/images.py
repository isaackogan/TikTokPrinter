from TikTokLive.types.events import GiftEvent

from TikTokPrinter import TikTokPrinterClient, EscposEngineGenerator, TikTokMedia
from TikTokPrinter.types.objects import PrinterImage

client: TikTokPrinterClient = TikTokPrinterClient(
    unique_id="USERNAME_HERE",
    engine=EscposEngineGenerator.create_usb(
        vendor_id=0x1,  # Vendor ID goes here
        product_id=0x1,  # Product ID goes here
        align="center"
    )
)


@client.on("gift")
async def on_gift(event: GiftEvent):
    """
    If you want to send multiple printer commands in one go, the recommended way
    to do it is through the queue method.

    This library has support for automatically downloading & printing resources
    from the TikTok API.

    """

    # If currently streaking
    if event.gift.streaking:
        return

    client.queue(

        PrinterImage(
            # Download their avatar and print the image as a circle
            await TikTokMedia.user_image(event.user, size=150, circle=True, circle_blur_radius=2)
        ),

        PrinterImage(
            # Download the gift image and print it
            await TikTokMedia.gift_image(event.gift)
        )
    )


if __name__ == '__main__':
    """

    Receiving an Invalid Endpoint error with a USB printer?

    Try adding “in_ep = 0x81, out_ep = 0x03" to the create_usb function!
    If you are not receiving this error, do not add the additional parameters!
    If you continue to receive this error, try doing out_ep = 0x02. 

    If that still doesn't work, make a ticket & we will handle it together!

    """

    client.run()
