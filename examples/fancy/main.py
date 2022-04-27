import random

from TikTokLive.types.events import ShareEvent, JoinEvent, FollowEvent, GiftEvent

from TikTokPrinter import EscposEngineGenerator, TikTokMedia
from TikTokPrinter.types.objects import PrinterText, PrinterImage, VoiceText
from examples.fancy.client import AdvancedClient

client: AdvancedClient = AdvancedClient(
    unique_id="@tiktokecidn",
    engine=EscposEngineGenerator.create_usb(
        vendor_id=0x1,  # Vendor ID goes here
        product_id=0x1,  # Product ID goes here
        align="center"
    )
)


@client.on("share")
async def on_share(event: ShareEvent):
    # Check if valid
    if not event.user:
        return

    client.queue(
        PrinterText("-" * 20),
        PrinterText(f"@{event.user.uniqueId}", bold=True),
        PrinterText("Thank you for sharing the LIVE!")
    )


@client.on("like")
async def on_share(event: ShareEvent):
    # Check if valid
    if not event.user:
        return

    # Only do this if the viewer count is less than 50
    if client.viewer_count and client.viewer_count > 50:
        return

    client.queue(
        PrinterText("-" * 20),
        PrinterText(f"@{event.user.uniqueId}", bold=True),
        PrinterText("Thank you for the likes!! <3<3")
    )


@client.on("join")
async def on_join(event: JoinEvent):
    # Check if valid
    if not event.user:
        return

    # Only do this if the viewer count is less than 20
    if client.viewer_count and client.viewer_count > 20:
        return

    client.queue(
        PrinterText("-" * 20),
        PrinterText(f"@{event.user.uniqueId}", bold=True),
        PrinterText("Welcome to the LIVE!")
    )


@client.on("follow")
async def on_follow(event: FollowEvent):
    # Check if valid
    if not event.user:
        return

    # Only do this if the viewer count is less than 20
    if client.viewer_count and client.viewer_count > 20:
        return

    client.queue(
        PrinterText("-" * 20),
        PrinterText(f"@{event.user.uniqueId}", bold=True),
        PrinterText("Thank you for the follow!!!")
    )


@client.on("gift")
async def on_gift(event: GiftEvent):
    # Check if valid
    if not event.user:
        return

    # Calculate cost for streakable items that have ended
    if event.gift.streakable and not event.gift.streaking:
        diamonds: int = event.gift.extended_gift.diamond_count * event.gift.repeatCount

    # Calculate cost for non-streakable items
    elif not event.gift.streakable:
        diamonds: int = event.gift.extended_gift.diamond_count

    # Streakable items that have not ended their streak
    else:
        return

    # If less than 5 diamonds (CHEAP)
    if diamonds < 5:
        client.queue(
            PrinterText("-" * 20),
            PrinterText(f"Thank you so much!! :D"),
            PrinterText(f"@{event.user.uniqueId}", bold=True),
            PrinterText(f"For sending {event.gift.repeatCount}x {event.gift.extended_gift.name}")
        )

        return

    # If between 5 & 10 diamonds (SEMI-EXPENSIVE)
    if 5 <= diamonds <= 10:
        client.queue(
            PrinterImage(
                # Download the gift image and print it
                await TikTokMedia.gift_image(event.gift)
            ),
            PrinterImage(
                # Get a custom special image :)
                client.get_semi_expensive(event.user.uniqueId, event.gift.extended_gift.name, event.gift.repeatCount)
            )
        )

        return

    # If diamonds are greater than 10
    client.queue(

        PrinterImage(
            # Get a custom special image :)
            client.get_semi_expensive(event.user.uniqueId, event.gift.giftDetails.giftName, event.gift.repeatCount)
        ),

        PrinterImage(
            # Download the gift image and print it
            await TikTokMedia.gift_image(event.gift)
        ),

        PrinterImage(
            # Download the user image and print it
            await TikTokMedia.user_image(event.user)
        ),

        VoiceText(
            # Say thanks for the gift
            random.choice([
                f"Woah, hotshot! Thanks {event.user.uniqueId} for the {event.gift.repeatCount} {event.gift.giftDetails.giftName}",
                f"Woah, thanks {event.user.uniqueId} for the {event.gift.repeatCount} {event.gift.giftDetails.giftName}",
                f"You're on fire! Thanks {event.user.uniqueId} for the {event.gift.repeatCount} {event.gift.giftDetails.giftName}",
                f"That's freaking insane! Thanks {event.user.uniqueId} for the {event.gift.repeatCount} {event.gift.giftDetails.giftName}",
            ])
        )
    )


if __name__ == '__main__':
    client.run()
