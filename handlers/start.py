from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hai {message.from_user.first_name}!</b>

Aku adalah Bot Musik Telegram, Apabila Ingin Menggunakan Aku Invite Aku Dan Assisten Aku Ya Biar Berjalan Dengan Lancar, Apabila Ada Kendala Tidak Tau Cara Pakainya Bisa PC OWNERNYA!:))
━━━━━━━━━━━━━━━━━━━━━━
Bot : @Crystalisticbot - Asisten : @Assistencrystal
        """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "⚡ Owner Aku!", url="https://t.me/afterdaytoxic")
                  ],[
                    InlineKeyboardButton(
                        "🍃 Channel Aku!", url="https://t.me/captionanakmuda"
                    ),
                    InlineKeyboardButton(
                        "❤️ Grup Aku!", url="https://t.me/humangabutguys") 
                  ],[
                    InlineKeyboardButton(
                        "👸 My Bot Help!", url="https://t.me/naylaanggitabot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🎧 Pemutar Musik Is The On!**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/humangabutguys"
                    ),
                    InlineKeyboardButton(
                        "⚡ Owner Aku!", url="https://t.me/afterdaytoxic"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🎧 Pemutar Musik Is The On!**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ Pemilik", url="https://t.me/afterdaytoxic") 
                ],[
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/humangabutguys"
                    )
                ]
            ]
        )
   )
