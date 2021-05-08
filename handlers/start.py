from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>ꃅꍏꀤꀤ ꁅꀎꌩꌗ 👋🏻🦇 {message.from_user.first_name} Perkenalkan Aku 𓊈ᴄʀʏꜱᴛᴀʟ ᴍᴜꜱɪᴄ𓊉\n
𝐀𝐤𝐮 𝐚𝐝𝐚𝐥𝐚𝐡 𝐁𝐨𝐭 𝐌𝐮𝐬𝐢𝐤 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦, 𝐀𝐩𝐚𝐛𝐢𝐥𝐚 𝐈𝐧𝐠𝐢𝐧 𝐌𝐞𝐧𝐠𝐠𝐮𝐧𝐚𝐤𝐚𝐧 𝐀𝐤𝐮 𝐈𝐧𝐯𝐢𝐭𝐞 𝐀𝐤𝐮 𝐃𝐚𝐧 𝐀𝐬𝐬𝐢𝐬𝐭𝐞𝐧 𝐀𝐤𝐮 𝐘𝐚 𝐁𝐢𝐚𝐫 𝐁𝐞𝐫𝐣𝐚𝐥𝐚𝐧 𝐃𝐞𝐧𝐠𝐚𝐧 𝐋𝐚𝐧𝐜𝐚𝐫.
𝐀𝐩𝐚𝐛𝐢𝐥𝐚 𝐀𝐝𝐚 𝐊𝐞𝐧𝐝𝐚𝐥𝐚 𝐓𝐢𝐝𝐚𝐤 𝐓𝐚𝐮 𝐂𝐚𝐫𝐚 𝐏𝐚𝐤𝐚𝐢𝐧𝐲𝐚 𝐁𝐢𝐬𝐚 𝐏𝐂 𝐎𝐖𝐍𝐄𝐑 𝐀𝐊𝐔!:))
┏━━━━━━━━━━━━━━
┣ > 𝙼𝚎𝚖𝚞𝚝𝚊𝚛 𝚖𝚞𝚜𝚒𝚔 𝚍𝚒𝚐𝚛𝚞𝚙 𝚔𝚊𝚖𝚞.
┣ > 𝙱𝚒𝚜𝚊 𝚕𝚒𝚜𝚝 𝚕𝚊𝚐𝚞, 𝚌𝚞𝚖𝚊𝚗 𝚓𝚊𝚗𝚐𝚊𝚗 𝚜𝚎𝚔𝚊𝚕𝚒𝚐𝚞𝚜 𝚝𝚊𝚔𝚞𝚝 𝚎𝚛𝚛𝚘𝚛.
┣ > 𝙼𝚎𝚗𝚌𝚊𝚛𝚒 𝚍𝚊𝚗 𝚖𝚎𝚖𝚞𝚕𝚊𝚒 𝚕𝚊𝚐𝚞 𝚋𝚎𝚛𝚜𝚊𝚖𝚊 𝚝𝚎𝚖𝚊𝚗-𝚝𝚎𝚖𝚊𝚗𝚖𝚞.
┣ > 𝙼𝚎𝚗𝚌𝚊𝚛𝚒 𝚕𝚊𝚐𝚞 𝚔𝚊𝚖𝚞 𝚍𝚊𝚗 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝚕𝚊𝚐𝚞 𝚔𝚊𝚖𝚞 𝚖𝚎𝚕𝚊𝚕𝚞𝚒 𝚊𝚔𝚞.
┗━━━━━━━━━━━━━━
❃ 𝓜𝓪𝓷𝓪𝓰𝓮𝓶𝓮𝓷𝓽 𝓦𝓲𝓽𝓱 🦇 𝓑𝔂 : [Afterday](https://t.me/afterdaytoxic)
❃ 𝓣𝓱𝓪𝓷𝓴𝓼 𝓣𝓸 : [Grup Support](https://t.me/humangabutguys)
━━━━━━━━━━━━━━━
𝐁𝐨𝐭 𝐌𝐮𝐬𝐢𝐤 𝐀𝐤𝐮 : @crystalisticbot - 𝐀𝐬𝐬𝐢𝐬𝐭𝐞𝐧 𝐌𝐮𝐬𝐢𝐤 : @assistencrystal
</b>""",
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

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aku sudah online, ayo kita joget ceria! 🎶**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦇 Owner Aku!", url="https://t.me/afterdaytoxic"
                    )
                ],[
                    InlineKeyboardButton(
                        "✅ Yes!", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ No!", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Klik tombol dibawah untuk melihat panduan menggunakan bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦇 Cara Memakai Bot Music!", url="https://t.me/humangabutguys/91577"
                    )
                ]
            ]
        ),
    )
