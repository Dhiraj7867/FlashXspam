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

from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"""
✨ **ʙᴏᴛ ʜᴇʟᴘ** ✨

**[ꜱᴛᴏʀᴍ ꜱᴘᴀᴍ ʙᴏᴛ](https://t.me/II_DHIRAJ_II) ʜᴇʟᴘ ᴍᴇɴᴜ** 🥀

**ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ꜱᴛᴏʀᴍ](https://github.com/dhiraj7867/FlashXspam)** ✨

**ᴄʜᴀɴɴᴇʟ: [ꜱᴛᴏʀᴍ ᴛᴇᴄʜ 🇮🇳](https://t.me/flash_TECHH)**
**ꜱᴜᴘᴘᴏʀᴛ: [ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ 🇮🇳](https://t.me/flash_CHATZ)**
"""
HELP_BUTTON = [
    [
      Button.inline("• ꜱᴘᴀᴍ •", data="spam"),
      Button.inline("• ʀᴀɪᴅ •", data="raid")
    ],
    [
      Button.inline("• ᴇxᴛʀᴀꜱ •", data="extra"),
      Button.inline("• ᴏᴡɴᴇʀ •", data="owner")
    ],
    [
      Button.url("• ꜱᴜᴘᴘᴏʀᴛ •", "https://t.me/flash_CHATZ")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://telegra.ph/file/e91c5cf1d7283053bfed4.mp4",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ᴏᴄᴄᴜʀᴇᴅ!\n\n**ᴇʀʀᴏʀ:** {str(e)}")

extra_msg = f"""
**» ᴇ​🇽​ᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ⦂**

 ˣ ᴄʜᴇᴄᴋ ᴘɪɴɢ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴘɪɴɢ

 ˣ ʀᴇꜱᴛᴀʀᴛ ʙᴏᴛ ɪᴛ ᴡɪʟʟ ᴛᴀᴋᴇ 5 ᴍɪɴ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʀᴇꜱᴛᴀʀᴛ

 ˣ ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴇᴄʜᴏ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʀᴍᴇᴄʜᴏ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʟᴇᴀᴠᴇ (ɢʀᴏᴜᴘ/ᴄʜᴀᴛ ɪᴅ)
🔸 {hl}ʟᴇᴀᴠᴇ (ʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ)

 ˣ ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʜᴀɴɢ (ᴄᴏᴜɴᴛᴇʀ)

 ˣ ꜱᴇɴᴅꜱ ᴇᴍᴏᴊɪ ᴡɪᴛʜ ᴛʜᴇ ɢɪᴠᴇ ᴄᴏᴜɴᴛᴇʀ ᴏɴ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴇᴍᴏᴊɪ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ᴇᴍᴏᴊɪ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʟᴏᴠᴇʀᴀɪᴅ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ʟᴏᴠᴇʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜰʟɪʀᴛꜱ ᴡɪᴛʜ ᴛʜᴇ ɢɪᴠᴇ ᴄᴏᴜɴᴛᴇʀ ᴏɴ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ꜰʟɪʀᴛ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ꜰʟɪʀᴛ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ꜱʀᴀɪᴅ (ᴄᴏᴜɴᴛᴇʀ) (ᴜꜱᴇʀɴᴀᴍᴇ)
🔸 {hl}ꜱʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ) 

**© @KKEX_XD**
"""


owner_msg = f"""
**» ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ⦂**

 ˣ ꜱᴜᴅᴏ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴀᴅᴅꜱᴜᴅᴏ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

**© @KKEX_XD**
"""      
          
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**

 ˣ ꜱᴛᴀʀᴛ ᴛʜᴇ ʀᴀɪᴅ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʀᴀɪᴅ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʀᴀɪᴅ (ᴄᴏᴜɴᴛꜱ) (ᴜꜱᴇʀɴᴀᴍᴇ)

 ˣ ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀᴛ.

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʀʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʀʀᴀɪᴅ (ᴜꜱᴇʀɴᴀᴍᴇ)

 ˣ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴅʀʀᴀɪᴅ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ᴅʀʀᴀɪᴅ (ᴜꜱᴇʀɴᴀᴍᴇ)

**© @KKEX_XD**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**

 ˣ ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ) (ᴀᴜᴛʜᴏʀ)
🔸 {hl}ꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏɪɴɢ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ)

 ˣ ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ᴘꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ)

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ɢᴍ (ᴄᴏᴜɴᴛꜱ)
🔸 {hl}ɢᴍ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ɢᴍ -ᴜ
🔸 {hl}ɢᴍ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ᴀꜰᴛᴇʀɴᴏᴏɴ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ɢᴀ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ɢᴀ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ɢᴏᴏᴅ ɴɪɢʜᴛ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ɢɴ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ɢɴ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

 ˣ ꜱᴘᴀᴍ ᴛʜᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʙᴅᴀʏ ᴍꜱɢꜱ

👨‍💻 ᴜꜱᴀɢᴇ :
🔸 {hl}ʙꜱᴘᴀᴍ (ᴄᴏᴜɴᴛꜱ) (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)
🔸 {hl}ʙꜱᴘᴀᴍ -ᴜ (ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏᴏɴᴇ)

** © @KKEX_XD**
"""                                
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("• ꜱᴘᴀᴍ •", data="spam"),
                Button.inline("• ʀᴀɪᴅ •", data="raid")
              ],
              [
                Button.inline("• ᴇxᴛʀᴀꜱ •", data="extra"),
                Button.inline("• ᴏᴡɴᴇʀ •", data="owner")
              ],
              [
                Button.url("• ꜱᴜᴘᴘᴏʀᴛ •", "https://t.me/STORM_CHATZ")
              ]
            ]
          )
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ꜱᴛᴏʀᴍ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @KKEX_XD", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
              ) 
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ꜱᴛᴏʀᴍ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @KKEX_XD", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
          )
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ꜱᴛᴏʀᴍ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @KKEX_XD", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("🔙 ʙᴀᴄᴋ", data="help_back"),],],
            )
    else:
        await event.answer("ɴᴏᴏʙ ! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ꜱᴛᴏʀᴍ ꜱᴘᴀᴍ ʙᴏᴛꜱ !! @KKEX_XD", cache_time=0, alert=True)
