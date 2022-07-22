TikTokPrinter - Thermal Printer Software
==================
A Python library to print to thermal printers from TikTokLive.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat-square)](https://www.linkedin.com/in/isaac-kogan-5a45b9193/ )
[![HitCount](https://hits.dwyl.com/isaackogan/TikTokPrinter.svg?style=flat)](http://hits.dwyl.com/isaackogan/TikTokLive)
![Forks](https://img.shields.io/github/forks/isaackogan/TikTokPrinter)
![Stars](https://img.shields.io/github/stars/isaackogan/TikTokPrinter)
[![Support Server](https://img.shields.io/discord/831349828578574346.svg?color=7289da&logo=discord&style=flat-square&t=3)](https://discord.gg/4Mbw58w5Qx)

Welcome to the public GitHub information page for the number one best-selling, most customizable & professional-grade tool for thermal printing on TikTok.

### **BUY HERE: https://discord.gg/4Mbw58w5Qx**

Thermal printing is a very recent, very exciting trend on TikTok. It is also a very **complex** one. Not because the topic is difficult in and of itself, but because people want so many different things.

That's why I developed an all-encompassing, multithreaded thermal printing program that does... everything, including a comprehensive [video tutorial](https://www.youtube.com/watch?v=NeapS5Jn_oo) on how to use it, made by me.

No subscription unlike many virtual printer services. One-time, life-time purchase. Can be installed in python via pip. Includes access to all future releases/updates to the project.

## ❤️ [Get It Now](#purchase-now) ❤️

### YouTube Showcase & Tutorial

If you want to see just how powerful this library is (and easy to use), we made a video tutorial & showcase
that goes through the basics of how to get started using it. Click the thumbnail below to warp.

[![YouTube Tutorial & Showcase](https://i.imgur.com/UoIrSwr.png)](https://www.youtube.com/watch?v=NeapS5Jn_oo)

### Auto-Select

Automatically find & use your USB printer.

![image](https://user-images.githubusercontent.com/65869106/166118006-7c3ccdff-4dc7-48d6-b581-99f28b5e643f.png)

### Purchase Details (Cost, Pricing Logic, etc.)

The cost is a flat `$50 USD`. That's insanely cheap.

This library is the most advanced, most purchased printer script on the market. Not only does it have an insane number of features, it was made by the person that _created_
the TikTokLive library. That gives you a benefit of ensuring that it is not only guaranteed to work, but guaranteed to be the best of the best you will possibly find.

The price is set at what it is because of the ridiculous amount of time spent learning to program, creating the TikTokLive library, figuring out how to print on Windows, MacOS and Linux, creating guides, building the
highly complex script itself, learning all the ways it can go wrong and fixing them, dealing with customer issues and so much more.

Purchasing this script is an investment that you can make thousands of dollars off of. At this price-point, that's a hell of a deal. You are recommended to have basic Python knowledge to use this library.

### [Purchase Now](https://discord.gg/4Mbw58w5Qx)

To buy this library, create a ticket in the `#tickets` channel in https://discord.gg/4Mbw58w5Qx.

Type the message "Printer Magic" in the ticket and I will immediately get you started so that you can get to printing as fast as possible!

### Printer Library Example

Here's a sample of what you can do with this library in less than 30 lines of code:

![](https://github.com/isaackogan/TikTokLive/raw/master/.github/RESOURCES/printer.gif)

To show you just how advanced the library is, here we can print a profile picture, play a sound, and do text-to-speech... in just 3 "true" lines of code. This is insane.

```py
@client.on("comment")
async def on_comment(event: CommentEvent):
    client.queue(

        # Divier Text
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
```

### Feature List (30+ Features)

#### Primary Features

- Ready-to-go script included for non-programmers (basic knowledge still recommended) that has everything you need, already put together
- Automatically find your printer device
- Print ANY Message
- Print Profile Pictures, Gift Images, Custom Images
- CUSTOM Text to Speech (perhaps when someone gifts?)
- Play Sounds (perhaps when someone gifts?)
- Support for ALL Serial, USB, and Network ESC-POS printers
- Automatic setup script
- Support for MacOS, Windows, Linux
- Fully documented API
- Quick-install with PIP
- Access to future releases/updates
- Video Set-Up Tutorial
- Made to be easy to use for newbies
- Access to private discord chat for clients

### Additional Features

- Download and print TikTok user avatars, gifts
- Extremely high level API (There is zero need to touch anything low-level, I've got it covered)
- 100% Asynchronous Programming
- Bold messages
- Left, Right, Center Adjust
- Newline character support
- Print backwards (flip the input!)
- Insert items at the start of the print queue (priority)
- Insert items at the end of the print queue
- Insert items at any index in the print queue
- Custom errors built on top of the API describing what went wrong when it happens
- Errors do not kill the script. Even if a part of a message breaks, the rest still prints!
- Send messages to the TikTok LIVE Chat (chat-bot)
- How-to example on basic usage (using formatting, text-to-speech, sounds, images, etc.)
- How-to example on using gifts
- How-to example on using commands
- How-to example on other features
- Automatically find in_ep and out_ep values

