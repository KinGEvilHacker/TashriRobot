import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from TashriRobot import telethn as bot
from TashriRobot import telethn as tgbot
from TashriRobot.events import register

edit_time = 5
""" =======================❦ᴍɪss 𝐑σႦσ𝐓 ✗ ᴍᴜꜱɪᴄ====================== """
file1 = "https://graph.org/file/83ec2821355336e588265.jpg"
file2 = "https://graph.org/file/c4dc510f7532f842f59bb.jpg"
file3 = "https://graph.org/file/75196b8e864cf0cd4046f.jpg"
file4 = "https://graph.org/file/c0b2daa066d96d61571e4.jpg"
file5 = "https://graph.org/file/704f892c63d58e6f12a80.jpg"
""" =======================❦ᴍɪss 𝐑σႦσ𝐓 ✗ ᴍᴜꜱɪᴄ====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"Hey {firstname}, \n Click on the button below \n to get info about you",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = "ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❦⚠ᙓᖇᖇටᖇ︵⚠⁴⁰⁴࿐​​​​​​​​​​  𝐑𝐨𝐛𝐨𝐭\n\n"
        LILIE += f"ғɪʀsᴛ ɴᴀᴍᴇ: {PRO.first_name} \n"
        LILIE += f"ʟᴀsᴛ ɴᴀᴍᴇ: {PRO.last_name}\n"
        LILIE += f"ʏᴏᴜ ʙᴏᴛ : {PRO.bot} \n"
        LILIE += f"ʀᴇsᴛʀɪᴄᴛᴇᴅ : {PRO.restricted} \n"
        LILIE += f"ᴜsᴇʀ ɪᴅ: {boy}\n"
        LILIE += f"ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
__mod_name__ = "ɪɴғᴏ"
__help__ = """
 /myinfo  ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ɪɴғᴏ 

☆............𝙱𝚈 » [⚠ᙓᖇᖇටᖇ︵⚠⁴⁰⁴](https://t.me/I_am_dead_smile)............☆"""
