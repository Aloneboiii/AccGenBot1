from AccGenBot import BotzCity
from telethon import events,Button
import re, os, random
from AccGenBot.func import check
from vars import var

USERNAME = var.CHANNEL_USERNAME
CHANNEL = var.CHANNEL_URL
LOGS = var.LOGS

bot = BotzCity

@bot.on(events.NewMessage(pattern="^[/!]start|Start|START$"))
async def _(event):
   join = [[Button.url("Jᴏɪɴ ᴄʜᴀɴɴᴇʟ", f"{CHANNEL}")]]
   lol = await check(USERNAME, event, bot)
   if lol is False:
       await event.reply(f"**Heya {event.sender.first_name}, join my channel to use me!**", buttons=join)
       return
   if event.is_private:
        k = f"**Heya {event.sender.first_name}, You can generate accounts by using this bot\nUse /cmds or /help to check my commands\n\nDon't forget to join my channel\n\n~ @BotzCity**"
        await bot.send_message(event.chat, k)
   else:
        await bot.send_message(event.chat, "Sorry to say btw i only works in pm, I'm leaving this group kek")
        await bot.delete_dialog(event.chat_id)