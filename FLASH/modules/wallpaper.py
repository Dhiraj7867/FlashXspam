#MIT License

#Copyright (c) 2024 DHIRAJ [AFK]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import asyncio
from random import choice
from telethon import events
from telethon import events, functions, types
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from FLASH.data import WALLPAPER
from FLASH.data import DEV

@X1.on(events.NewMessage(incoming=True, pattern=r"\%swspam(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%swspam(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%swspam(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%swspam(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%swspam(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%swspam(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%swspam(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%swspam(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%swspam(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%swspam(?: |$)(.*)" % hl))

async def wspam(event):
    if event.sender_id in SUDO_USERS:
        if event.chat_id in GROUPS: 
            #groups for error
            await event.reply("» ꜱʀʏ, ᴛʜɪꜱ ɢʀᴏᴜᴘ ɪꜱ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ʙʏ ғʟᴀsʜ 🛡️")
        else:
            try:
                counter = int(event.text.split(" ", 2)[1])
                wallpaper = choice(wallpapers)
                for _ in range(counter):
                    alt = await event.client.send_file(event.chat_id, porrn)
                    await gifspam(event, alt) 
                    await asyncio.sleep(0.2)
            except (IndexError, ValueError):
                await event.reply(f"{hl}ᴘꜱᴘᴀᴍ <ᴄᴏᴜɴᴛ>")
            except Exception as e:
                print(e)


    wallpaper_url = random.choice(walldata)
    await message.reply_photo(wallpaper_url)￼Enter
