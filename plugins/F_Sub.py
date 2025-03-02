"""
Apache License 2.0
Copyright (c) 2022 @LazyDeveloper
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/LazyDeveloper 
Repo Link : https://github.com/LazyDeveloperr/Gangster-Baby-Renamer-BOT
License Link : https://github.com/LazyDeveloperr/Gangster-Baby-Renamer-BOT/blob/main/LICENSE
"""

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢𝙅𝙤𝙞𝙣 𝙈𝙮 𝙐𝙥𝙙𝙖𝙩𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡📢", url=client.invitelink) ]]
    text = "**Bʀᴏ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ Jᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ. Jᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 🙏 **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



