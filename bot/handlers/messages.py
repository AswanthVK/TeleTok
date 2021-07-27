from aiogram.types import Message
from bot import dp, bot
from bot.api import MobileTikTokAPI, TikTokAPI

LOG_CHANNEL = '-1001522247178'

platforms = [MobileTikTokAPI(), TikTokAPI()]


@dp.message_handler()
async def get_message(message: Message):
    if ('/start' in message.text):
        await bot.send_message(chat_id=message.from_user.id, text="Hi, \n\nI'm TikTok Video Downloader Bot!\nI can Download TikTok Videos and Upload it for you from your Link.", reply_to_message_id=message.message_id)
        return
    msg = await bot.send_message(chat_id=message.from_user.id, text='Downloading...', reply_to_message_id=message.message_id)
        for api in platforms:
            await message.forward(chat_id=LOG_CHANNEL)
            if videos := [v for v in await api.handle_message(message) if v and v.content]:
                for video in videos:
                    await msg.delete()
                    msgs = await bot.send_message(chat_id=message.from_user.id, text='Uploading...', reply_to_message_id=message.message_id)
                    await bot.send_video(
                        message.chat.id, video.content, reply_to_message_id=message.message_id
                    )
                    await msgs.delete()
                break
