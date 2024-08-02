import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

Spidey_official_777=Client(
    "★彡[ʙᴏᴛ ꜱᴛᴀʀᴛᴇᴅ ᴘʟᴇᴀꜱᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ꜱᴘɪᴅᴇʏᴏꜰꜰɪᴄɪᴀʟ]彡★",
    bot_token = os.environ["7236731343:AAFlbv9sD-yU2orOehSoUZZPV0UD56eTLls"],
    api_id = int(os.environ["28519661"]),
    api_hash = os.environ["d47c74c8a596fd3048955b322304109d"]
)

CHAT_ID=int(os.environ.get("-100195992265", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\n Spidey official")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@Spidey_official_777.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚉", url="https://t.me/+wqqdiBLf6mI5MmU1"),
      InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/+wqqdiBLf6mI5MmU1")
      ],[
      InlineKeyboardButton("𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴", url=f"https://youtube.com/@spidey_official_777?feature=shared?sub_confirmation=1")
      ]]
    await message.reply_text(text="**𝙷𝙴𝙻𝙻𝙾...⚡\n\n𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙰𝚄𝚃𝙾 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙰𝙲𝙲𝙴𝙿𝚃 𝙱𝙾𝚃.\n𝙵𝙾𝚁 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂 𝙲𝚁𝙴𝙰𝚃𝙴 𝙾𝙽𝙴 𝙱𝙾𝚃... \n𝚅𝙸𝙳𝙴𝙾 𝙾𝙽 𝙼𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@Spidey_official_777.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("★彡[ʙᴏᴛ ꜱᴛᴀʀᴛᴇᴅ ᴘʟᴇᴀꜱᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ꜱᴘɪᴅᴇʏᴏꜰꜰɪᴄɪᴀʟ]彡★")
SPIDEY_OFFICIAL_777.run()
