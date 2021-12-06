from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""**ᴍᴇʀʜᴀʙᴀ Ben Netd Music Bot 👋** ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴜᴘʟᴀʀɪɴɪɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛʟᴇʀɪɴᴅᴇ ᴅᴏɴᴍᴀᴅᴀɴ ᴍᴜᴢɪᴋ ᴄᴀʟᴀʙɪʟɪʏᴏʀᴜᴍ. **Ban Yetkisine İhtiyacım Yoktur.**🥳 \n\n❗️ **ᴛᴇʟᴇɢʀᴀᴍᴅᴀ ʙᴇɴɪ ɴᴀꜱɪʟ ᴋᴜʟʟᴀɴᴀʙɪʟᴇᴄᴇɢɪɴɪᴢɪ ᴏɢʀᴇɴᴍᴇᴋ ɪᴄɪɴ ʟᴜᴛꜰᴇɴ >> /help ʙᴜᴛᴏɴᴜɴᴀ ʙᴀꜱɪɴɪᴢ.** \n\n❗️ **ɢʀᴜʙᴜɴᴜᴢᴜɴ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛɪɴᴅᴇ, ᴍᴜᴢɪᴋ ᴄᴀʟᴀʙɪʟᴍᴇᴍ ɪᴄɪɴ ᴀꜱɪꜱᴛᴀɴɪɴ ɢʀᴜʙᴜɴᴜᴢᴅᴀ ᴏʟᴍᴀꜱɪ ɢᴇʀᴇᴋɪʀ.**
      """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎯 BOTU GRUBA EKLE", url="https://t.me/NetdMusicBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👨 ASİSTAN", url="https://t.me/NetdMusicAsistan" 
                    ),
                    InlineKeyboardButton(
                        "💬 DESTEK", url="https://t.me/NetdDestek"
                    ),
                    InlineKeyboardButton(
                        "🤖 Tagger Bot", url="https://t.me/MiaTagBot") 
                ],
                [
                    InlineKeyboardButton(
                        "🎛 KOMUTLAR 🎛", url="https://t.me/NetdBots/15"
                    )
                ]
            ]
        ), 
     disable_web_page_preview=True
   ) 
    
@Client.on_message(
    filters.command("start@NetdMusicBot")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
       """Harika! bot gruba eklendi. ❗️ Asistan Olmadan Çalışamam ❗️\n 1.Yöntem Bota İlk Önce Bağlantı İle Davet Etme Yetkisi Verip\n/asistan Komutunu Gruba Göndermek. [Önerilir]\n 2.Yöntem @NetdMusicAsistan 'ı Gruba Normal Üye Eklermiş Gibi Manuel OLarak Eklemek.""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 DESTEK GRUBU 👥", url="https://t.me/NetdDestek")
                ]
            ]
        )
   )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Merhaba {message.from_user.first_name} İşte Desteklediğim Komutlar ; 
\n/play şarkı adı - ʏᴏᴜᴛᴜʙᴇ'ᴅᴀɴ ɪꜱᴛᴇᴅɪɢɪɴɪᴢ ᴍᴜᴢɪɢɪ ᴄᴀʟᴀʀ\n📃 **Örnek : /play Ceza Suspus** 
\n/oynat - Yanıtlanan ses dosyasını Oynatır.
/durdur - ᴄᴀʟᴀɴ ꜱᴀʀᴋɪʏɪ ᴅᴜʀᴀᴋʟᴀᴛɪʀ.
/devam - ᴅᴜʀᴀɴ ꜱᴀʀᴋɪʏɪ ᴅᴇᴠᴀᴍ ᴇᴛᴛɪʀɪʀ.
/atla - ꜱᴏɴʀᴀᴋɪ ꜱᴀʀᴋɪʏɪ ᴄᴀʟᴀʀ.
/son - ꜱᴇꜱʟɪ ᴍᴜᴢɪɢɪ ᴋᴀᴘᴀᴛɪʀ.
/reload - Botu yeniden başlatır.
/asistan - Asistanı Gruba Ekler 💎
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎋 Reklam ve Önerileriniz İçin 🙋🏻‍♂️", url="https://t.me/Emirreis"
                    )
                ]
            ]
        )
    )    
