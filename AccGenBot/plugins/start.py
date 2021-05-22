from AccGenBot import BotzCity
from telethon import events,Button
import re, os, random

bot = BotzCity

@bot.on(events.NewMessage(pattern="^[/!]start|Start|START"))
async def _(event):
    k = f"""**Heya {event.sender.first_name}, You can generate accounts by using this bot\nUse /cmds or /help to check my commands\n\nDon't forget to join my channel\n\n~ @BotzCity**"
    await bot.send_message(event.chat, k)
