import os
import platform
import random
from typing import List

from PIL import ImageDraw, Image, ImageFont
from TikTokLive.types.events import ConnectEvent

from TikTokPrinter import TikTokPrinterClient, TikTokMedia
from TikTokPrinter.client.engines.escpos import EscposEngine


class AdvancedClient(TikTokPrinterClient):
    FREDOKA_LARGE = ImageFont.truetype("./resources/fonts/fredoka.ttf", 38)
    FREDOKA_MID = ImageFont.truetype("./resources/fonts/fredoka.ttf", 26)
    FREDOKA_SMALL = ImageFont.truetype("./resources/fonts/fredoka.ttf", 16)

    MINI_ICONS: List[str] = [
        "_devil.png", "_point.png", "_shocked.png", "_shoot.png", "_uwu.png", "_wholesome.png", "cry1.png", "cry2.png", "cry3.png",
        "embarassed1.png", "embarassed2.png", "love1.png", "love2.png", "love3.png", "love4.png", "love5.png", "love6.png", "love7.png",
        "love8.png", "love9.png", "love10.png"
    ]

    def __init__(self, unique_id: str, engine: EscposEngine, **options):
        super().__init__(unique_id, engine, **options)
        self.add_listener("connect", self.on_connect)

    async def on_connect(self, _: ConnectEvent):
        print("-------------------")
        print(f"Connected to @{self.unique_id}'s TikTok LIVE")
        print(f"Python version: {platform.python_version()}")
        print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
        print("Go for launch! Prepare for madness.")

    @classmethod
    def get_cheap_amount(cls, message: str, username: str):
        image = Image.new("RGBA", (100, 200), (255, 255, 255))
        draw: ImageDraw = ImageDraw.Draw(image)

        thank_message: str = message
        thank_width, thank_height = cls.FREDOKA_SMALL.getsize(thank_message)
        thank_start = ((image.width - thank_width) / 2, 18)
        draw.text(thank_start, thank_message, (0, 0, 0), font=cls.FREDOKA_LARGE)

        thank_message: str = username
        thank_width, thank_height = cls.FREDOKA_SMALL.getsize(thank_message)
        thank_start = ((image.width - thank_width) / 2, 50)
        draw.text(thank_start, thank_message, (0, 0, 0), font=cls.FREDOKA_LARGE)

    @classmethod
    def get_semi_expensive(cls, username: str, gift: str, amount: int):
        image = Image.new("RGBA", (400, 200), (255, 255, 255))
        draw: ImageDraw = ImageDraw.Draw(image)

        # Paste heart
        heart = TikTokMedia.remove_transparency(Image.open(f"resources/icons/{random.choice(cls.MINI_ICONS)}"))
        heart.thumbnail((64, 64))

        # Thank You
        thank_message: str = "Thank You"
        thank_width, thank_height = cls.FREDOKA_LARGE.getsize(thank_message)
        thank_start = ((image.width - thank_width) / 2, 18)
        draw.text(thank_start, thank_message, (0, 0, 0), font=cls.FREDOKA_LARGE)

        # Hearts
        image.paste(heart, (int((thank_start[0] - heart.width) / 2), 15))
        image.paste(heart, (int((image.width - heart.width * 1.2)), 15))

        # Username
        username_message: str = f"@{username}"
        name_font: ImageFont = cls.FREDOKA_LARGE
        n_w, n_h = cls.FREDOKA_LARGE.getsize(username_message)

        # Auto-resize
        if n_w > (image.width - 50):
            n_w, n_h = cls.FREDOKA_MID.getsize(username_message)
            name_font = cls.FREDOKA_MID

            if n_w > (image.width - 50):
                n_w, n_h = cls.FREDOKA_SMALL.getsize(username_message)
                name_font = cls.FREDOKA_SMALL

        username_start = ((image.width - n_w) / 2, (image.height - n_h) / 2)
        draw.text(username_start, username_message, (0, 122, 122), font=name_font)

        # Gift
        gift_message: str = f"for sending {amount}x {gift}"
        gift_width, gift_height = cls.FREDOKA_MID.getsize(gift_message)
        gift_start = ((image.width - gift_width) / 2, 140)
        draw.text(gift_start, gift_message, (0, 0, 0), font=cls.FREDOKA_MID)

        image = image.resize((500, 250))

        return image.convert("L")
