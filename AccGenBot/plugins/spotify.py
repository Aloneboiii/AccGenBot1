from AccGenBot import BotzCity, enjoy
from telethon import events, Button
import random
from AccGenBot.func import check 
from vars import var
import asyncio, os, re

USERNAME = var.CHANNEL_USERNAME
CHANNEL = var.CHANNEL_URL
LOGS = var.LOGS
bot = BotzCity

@bot.on(events.NewMessage(pattern="^[/!]zee"))
async def _(event):
   join = [[Button.url("Jᴏɪɴ ᴄʜᴀɴɴᴇʟ", f"{CHANNEL}")]]
   lol = await check(USERNAME, event, bot)
   if lol is False:
       await event.reply(f"**Heya {event.sender.first_name}, join my channel to use me!**", buttons=join)
       return
   gen = await event.reply("`Generating Account Pls weit`")
   with open("spotify.txt") as Alain:
     noice = Alain.read().splitlines()
     nice = random.choice(noice)
     email, pas = nice.split(":")
     okay = f"""**Account Generated Successfully**\n
**Type:** `Spotify`
**Combo:** `{email}`:`{pas}`
**Email:** **{email}**
**Password:** `{pas}`
**Generated by:** @{event.sender.username}"""

     generated = f"""**New account 📨**\n
**Type:** `Spotify`
**Generated by:** @{event.sender.username}
**User ID:** **{event.sender.id}**

**Bot:** @Acc_GenBot"""
     await gen.edit(f"{okay}\n\n{enjoy}")
     asyncio.sleep(1.5)
     await bot.send_message(LOGS, generated)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"spotify")))
async def _(event):
   join = [[Button.url("Jᴏɪɴ ᴄʜᴀɴɴᴇʟ", f"{CHANNEL}")]]
   lol = await check(USERNAME, event, bot)
   if lol is False:
       await event.reply(f"**Heya {event.sender.first_name}, join my channel to use me!**", buttons=join)
       return
   with open("spotify.txt") as Alain:
     noice = Alain.read().splitlines()
     nice = random.choice(noice)
     email, pas = nice.split(":")
     okay = f"""**Account Generated Successfully**\n
**Type:** `Spotify`
**Combo:** `{email}`:`{pas}`
**Email:** **{email}**
**Password:** `{pas}`

**Generated by:** @{event.sender.username}"""

     generated = f"""**New account 📨**\n
**Type:** `Spotify`
**Generated by:** @{event.sender.username}
**User ID:** **{event.sender.id}**

**Bot:** @Acc_GenBot"""
     await event.edit(f"{okay}\n\n{enjoy}")
     asyncio.sleep(1.5)
     await bot.send_message(LOGS, generated)

