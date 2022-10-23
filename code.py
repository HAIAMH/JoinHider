# Created By HAIAMH
# Don't Sell Source Code For Being Money
# Read The License ✓ https://github.com/HAIAMH/JoiNHidER/main/license
# Fork & give Star to me
# Don't Change The Code and Text on your wish

import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", "")

API_HASH = os.environ.get("API_HASH", "")
bot = Client(
        "hide",
        bot_token=BOT_TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )

START_TEXT = """<b>𝙷𝚎𝚕𝚕𝚘 {}
I can do remove join member Message in Group make me admin in Group /about


[Mᴜᴛʏᴀʟᴀ Hᴀʀsʜɪᴛʜ](https://t.me/MutyalaHarshith)<b>"""


ABOUT_TEXT = """**Aʙᴏᴜᴛ Mysᴇʟғ**
• **Bᴏᴛ ɴᴀᴍᴇ:** [JoinHider](https://github.com/HAIAMH/JoinHider)
• **Cʀᴇᴀᴛᴏʀ :** [Mᴜᴛʏᴀʟᴀ Hᴀʀsʜɪᴛʜ](https://t.me/MutyalaHarshith)
• **GɪᴛHᴜʙ** : [Fᴏʟʟᴏᴡ](https://GitHub.com/HAIAMH)
• **Sᴏᴜʀᴄᴇ** : [JoinHider](https://github.com/HAIAMH/JoinHider)
• **Sᴜᴘᴘᴏʀᴛ** : [ᴍʜɢᴄʜᴀᴛ](https://t.me/MHGcHaT)
• **Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 𝟹](https://python.org)
• **Lɪʙʀᴀʀʏ :** [Pʏʀᴏɢʀᴀᴍ ᴠ𝟷.𝟸.𝟶](https://pyrogram.org)
• **Sᴇʀᴠᴇʀ :** [Hᴇʀᴏᴋᴜ](https://heroku.com)"""


@bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply_photo(
        photo="https://telegra.ph/file/236794ce4bb2213eaae1e.jpg",
        caption=START_TEXT.format(update.from_user.mention)
    )

@bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    await update.reply_photo(
        photo="https://telegra.ph/file/236794ce4bb2213eaae1e.jpg",
        caption=START_TEXT.format(update.from_user.mention)
    )


@bot.on_message(filters.new_chat_members)
async def welcome(bot,message):
	await message.delete()	
	
@bot.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	await message.delete()	


	
bot.run()
