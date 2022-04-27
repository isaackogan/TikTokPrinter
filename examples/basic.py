from TikTokLive.types.events import ShareEvent, CommentEvent

from TikTokPrinter import TikTokPrinterClient, EscposEngineGenerator, TikTokMedia
from TikTokPrinter.types.objects import VoiceText, PrinterText, SoundFile, PrinterImage

client: TikTokPrinterClient = TikTokPrinterClient(
    unique_id="USERNAME_HERE",
    engine=EscposEngineGenerator.create_usb(
        vendor_id=0x1,  # Vendor ID goes here
        product_id=0x1,  # Product ID goes here
        align="center"
    )
)


@client.on("share")
async def on_share(event: ShareEvent):
    """
    You can interface with the library to directly print text!

    """

    client.text(f"Thank you, @{event.user.uniqueId}, for sharing the LIVE!")

    # client.voice("Do some text to speech ;)")
    # client.image(pil_image)
    # client.send_message("Send this to the TikTok Live chat as a bot!")
    # client.sound("./path/to/sound.mp3")


@client.on("comment")
async def on_comment(event: CommentEvent):
    """
    If you want to send multiple printer commands in one go, the recommended way
    to do it is through the queue method.

    """

    client.queue(
        PrinterText("-" * 20),

        # Speak the comment
        VoiceText(event.user.uniqueId + " said " + event.comment),

        # Print the comment to printer
        PrinterText(event.user.uniqueId + " -> " + event.comment),

        # Play a sound
        SoundFile("enchanted.wav"),

        # Download their avatar and print the image
        PrinterImage(await TikTokMedia.user_image(event.user, circle=False))

    )


if __name__ == '__main__':
    client.run()
