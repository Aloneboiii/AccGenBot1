from AccGenBot import BotzCity
from telethon import events, Button
import random
from AccGenBot.func import check 
from vars import var
import asyncio

USERNAME = var.CHANNEL_USERNAME
CHANNEL = var.CHANNEL_URL
LOGS = var.LOGS
bot = BotzCity

@bot.on(events.NewMessage(pattern="^[/!]voot"))
async def _(event):
   join = [[Button.url("Jᴏɪɴ ᴄʜᴀɴɴᴇʟ", f"{CHANNEL}")]]
   lol = await check(USERNAME, event, bot)
   if lol is False:
       await event.reply(f"**Heya {event.sender.first_name}, join my channel to use me!**", buttons=join)
       return
   gen = await event.reply("`Generating Account Pls weit`")
   with open("voot.txt") as Alain:
     noice = Alain.read().splitlines()
     nice = random.choice(noice)
     email, pas = nice.split(":")
     okay = f"""**Account Generated Successfully**\n
**Type:** `Voot`
**Combo:** `{email}`:`{pas}`
**Email:** **{email}**
**Password:** `{pas}`
**Generated by:** @{event.sender.username}"""

     generated = f"""**New account 📨**\n
{okay}"""
     await gen.edit(okay)
     asyncio.sleep(1)
     await bot.send_message(LOGS, generated)
