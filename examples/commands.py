import functools
from dataclasses import dataclass
from typing import List

from TikTokLive.types.events import GiftEvent, CommentEvent

from TikTokPrinter import TikTokPrinterClient, EscposEngineGenerator, TikTokMedia
from TikTokPrinter.types.objects import VoiceText, PrinterText, PrinterImage


@dataclass
class Context:
    name: str
    args: List[str]
    event: CommentEvent


class TikTokLiveCommandPrinterClient(TikTokPrinterClient):
    """
    Command System Client that overrides the main client
    """

    def __init__(self, unique_id: str, command_prefix: str = "/", donation_threshold: int = 0, **options):
        options["process_initial_data"] = False
        super().__init__(unique_id, **options)
        self.command_prefix: str = command_prefix
        self.add_listener("comment", functools.partial(self._parse_comments))
        self.add_listener("gift", functools.partial(self._parse_gifts))
        self.donations: dict = dict()
        self.donation_threshold: int = donation_threshold

    async def _parse_comments(self, event: CommentEvent):
        # Not a command
        if not event.comment.startswith(self.command_prefix):
            return

        _command: List[str] = event.comment.split(" ")
        _name: str = _command[0].replace(self.command_prefix, "", 1)

        self.emit(f"/{_name}", Context(name=_name, args=_command[1:], event=event))

    async def _parse_gifts(self, event: GiftEvent):
        # Check if valid
        if not event.user:
            return

        # If it's type 1 and the streak is over
        if not ((event.gift.gift_type == 1 and event.gift.repeat_end == 1) or event.gift.gift_type != 1):
            return

        diamonds: int = event.gift.extended_gift.diamond_count * event.gift.repeatCount

        # Threshold stuff
        before = client.donations.get(event.user.uniqueId, 0)
        after = diamonds + before
        client.donations[event.user.uniqueId] = after

        # If they hit the threshold, let them know
        if before < self.donation_threshold <= after:
            await self.send_message(f"Congratulations, {event.user.uniqueId}, you just unlocked command access!")


client: TikTokLiveCommandPrinterClient = TikTokLiveCommandPrinterClient(
    unique_id="jakeandrich",
    engine=EscposEngineGenerator.create_usb(
        vendor_id=0x0416,  # Vendor ID goes here
        product_id=0x5011,  # Product ID goes here
        align="center"
    ),
    command_prefix="/"
)


@client.on("/tts")
async def on_tts(context: Context):
    message = " ".join(context.args)

    client.queue(
        VoiceText(content=message),
        PrinterText(f"{context.event.user.uniqueId}", bold=True),
        PrinterText(content=f"{client.command_prefix}{context.name} {message}"),
        PrinterImage(await TikTokMedia.user_image(context.event.user, circle=False), padding=True)
    )


if __name__ == '__main__':
    client.run("SESSION_ID_HERE")
