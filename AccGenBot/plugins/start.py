from AccGenBot import BotzCity
from telethon import events,Button
import re, os, random
from AccGenBot.func import check
from vars import var

USERNAME = var.CHANNEL_USERNAME
CHANNEL = var.CHANNEL_URL

LOGS = var.LOGS

bot = BotzCity

@bot.on(events.NewMessage(pattern="^[/!](start|Start|START)$"))
async def _(event):
   join = [[Button.url("Jᴏɪɴ ᴄʜᴀɴɴᴇʟ", f"{CHANNEL}")]]
   lol = await check(USERNAME, event, bot)
   if lol is False:
       await event.reply(f"**Heya {event.sender.first_name}, join my channel to use me!**", buttons=join)
       return
   if event.is_private:
        button = [[Button.inline("Generate Accounts",data="gen"), Button.url("Channel","t.me/BotzCity")]]
        button += [[Button.url("Support","t.me/BotzCityChat")]]
        k = f"**Heya {event.sender.first_name}, You can generate accounts by using this bot\nUse /cmds or /help to check my commands\n\nDon't forget to join my channel\n\n~ {USERNAME}**"
        await bot.send_message(event.chat, k, buttons=button)
   else:
        await bot.send_message(event.chat, "**Sorry to say btw i only works in pm,\nI'm leaving this group kek**")
        await bot.delete_dialog(event.chat_id)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def _(event):
    button = [[Button.inline("Generate Accounts",data="gen"), Button.url("Channel","t.me/BotzCity")]]
    button += [[Button.url("Support","t.me/BotzCityChat")]]
    k = f"**Heya {event.sender.first_name}, You can generate accounts by using this bot\nUse /cmds or /help to check my commands\n\nDon't forget to join my channel\n\n~ {USERNAME}**"
    await event.edit(k, buttons=button)

@bot.on(events.NewMessage(pattern="^[/!](help|cmds|commands|Help|HELP|CMDS|Cmds)$"))
async def _(event):
   if event.is_private:
      k = """**Moi commands:**\n
**/start** - Which you have already done / Send start message...!
**/help** - List of all commands.
**/cmds** - List of all commands.
**/generate** - Get all commands for generating account..
**/netflix** - To generate netflix account!
**/voot** - To generate voot account!
**/zee** - To generate Zee5 account!
**/Spotify** - To generate spotify account!
**/balaji** - To generate Alt Balaji account!"""
      await bot.send_message(event.chat, k)
   else:
      await bot.send_message(event.chat, "Use me only in PM not here!\n**Me leaving this group kek**")
      await bot.delete_dialog(event.chat_id)

      
lol = [[Button.inline("Netflix", data="netflix"),Button.inline("Voot", data="voot")]]
lol += [[Button.inline("Zee5",data="zee"), Button.inline("Spotify", data="spotify")]]
lol += [[Button.inline("Alt Balaji", data="balaji"), Button.inline("⬅️ Back", data="start")]]

@bot.on(events.NewMessage(pattern="^[/!](gen|GEN|GENERATE|generate)$"))
async def _(event):
   await event.reply(f"**Choose which account you would like to generate**\n\n**~ @BotzCity**",buttons=lol)
   
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gen")))
async def _(event):
   await event.edit(f"**Choose which account you would like to generate**\n\n**~ @BotzCity**",buttons=lol)
