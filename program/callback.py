"""
Video + Music Stream Telegram Bot
Copyright (c) 2022-present levina=lab <https://github.com/levina-lab>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but without any warranty; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/licenses.html>
"""


from driver.core import me_bot, me_user
from driver.queues import QUEUE
from driver.decorators import check_blacklist
from program.utils.inline import menu_markup, stream_markup

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("dm_start"))
@check_blacklist()
async def dm_set(_, query: CallbackQuery):
    await query.answer("Start")
    await message.reply_photo(
        photo=f"https://telegra.ph/file/50c77a56c2489872836dc.jpg",
        caption=f"""**Welcome - {message.from_user.mention()} 👋
This is the Broken music bot, a bot for playing high quality and unbreakable music in your groups voice chat.
Just add me to your group and make a admin with needed admin permission to perform a right actions !!
Use the given buttons for more ❗️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Commands❓", callback_data="command_list"),
                    InlineKeyboardButton("About❕", callback_data="bot_about")
                ],[
                    InlineKeyboardButton("Basic Guide❔", callback_data="basic_guide")
                ],[
                    InlineKeyboardButton("✚ Add Me To Your Group ✚", url=f"https://t.me/{me_bot.username}?startgroup=true")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("basic_guide"))
@check_blacklist()
async def basic_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""⚠️ Read Basic Guide Carefully !!

» First add this bot in your group

» Make a bot admin

» Give needed admin permission

» Type /refresh in your group

» Start your groups voice chat

» Now play your song and enjoy !!""",
        reply_markup=InlineKeyboardMarkup(
            [    
                [
                    InlineKeyboardButton("Common Error ×", callback_data="common_error")
                ],[
                    InlineKeyboardButton("🔙 Back Home", callback_data="dm_start")
                  ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("common_error"))
@check_blacklist()
async def common_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""**Mostly Faced Error ⚠️

There wiil be the main error about to music assistant. If you are facing any type of error in your group then that time first make sure @BrokenxMusicAssistant is available in your group. If not then add it manually and before that make sure also it is not banned in ur chat.

Thanks !!**""",
        reply_markup=InlineKeyboardMarkup(
             [    
                [
                    InlineKeyboardButton("Owner Contact❗️", callback_data="contact_owner")
                ],[
                    InlineKeyboardButton("🔙 Back Home", callback_data="dm_start")
                  ]
             ] 
        ),
    )


@Client.on_callback_query(filters.regex("bot_about"))
@check_blacklist()
async def bot_set(_, query: CallbackQuery):
    await query.answer("bot about")
    await query.edit_message_text(
        f"""**This Music Bot is designed by a noob for playing a high quality and unbreakable music in your groups voice chat.

This bot helps you to play and download music from youtube server and many more features related to telegram voice chat.

Thanks !!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Make your own Bot 🤖", callback_data="own_bot")
                ],[
                    InlineKeyboardButton("🔙 Back Home", callback_data="dm_start")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("own_bot"))
@check_blacklist()
async def own_set(_, query: CallbackQuery):
    await query.answer("Create Your Bot")
    await query.edit_message_text(
        f"""**Tutorial soon at : @TeamBrokenProjects

The Tutorial video about to making your own bot like this will be soon available at @TeamBrokenSupport. Also source code and all information about making bot published soon. Stay connected with us at our update channel.

Thanks !!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Owner Contact❗️", callback_data="contact_owner")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="bot_about")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("contact_owner"))
@check_blacklist()
async def contact_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""**• This bot is developed by this noob 
- @Its_romeoo

• Powered by
- @TeamBrokenProjects
- @TeamBrokenSupport

Note : Contact developer only that time if you have really need a help or facing any type of issues. Don't try to waste our and your time by asking useless queries !!**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Back Home", callback_data="dm_start")]]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""**Check out the menu below to read the module information & see the list of available Commands !!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Voice Chat❓", callback_data="user_command"),
                    InlineKeyboardButton("Controller❗️", callback_data="admin_command")
                ],[
                    InlineKeyboardButton("Extra 🕹", callback_data="extra_command")
                ],[
                    InlineKeyboardButton("🔙 Back Home", callback_data="dm_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""⚠️ Voice Chat Commands.

» /play (song name/youtube link) - play the music from youtube
» /vplay (video name/youtube link) - play the video from youtube
» /stream (m3u8/youtube live link) - play youtube/m3u8 live stream music
» /vstream (youtube live link) - play youtube/m3u8 live stream video
» /playlist - view the queue list of songs and current playing song
» /lyric (query) - search for song lyrics based on the name of the song
» /song (query) - download song from YouTube
» /video (query) - download video from YouTube""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""⚠️ Only Group admins can use this commands.

» /pause - pause the current track being played
» /resume - play the previously paused track
» /skip - goes to the next track
» /stop - stop playback of the track and clears the queue
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /refresh - refresh the bot server and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("extra_command"))
@check_blacklist()
async def extra_set(_, query: CallbackQuery):
    await query.answer("extra commands")
    await query.edit_message_text(
        f"""⚠️ Extra Commands List.

» /eval - run an code
» /sh - run an code
» /repo - Get The Bot Repo !!
» /alive - show the bot alive info (in Group only)
» /info - Get Janam Kundli Of the user in Group
» /telegraph - Generate the Telegraph link of the replied media
» /speedtest - run the bot server speedtest
» /search (query) - search for the youtube video link
» /ping - show the bot ping status
» /uptime - show the bot uptime status""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    if user_id not in SUDO_USERS:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""✏️ Command list for sudo user.
» /stats - get the bot current statistic
» /calls - show you the list of all active group call in database
» /block (`chat_id`) - use this to blacklist any group from using your bot
» /unblock (`chat_id`) - use this to whitelist any group from using your bot
» /blocklist - show you the list of all blacklisted chat
» /sysinfo - show the system information
» /logs - generate the current bot logs
» /eval - run an code
» /sh - run an code""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    if user_id not in OWNER_ID:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""✏️ Command list for bot owner.

» /gban (`username` or `user_id`) - for global banned people, can be used only in group
» /ungban (`username` or `user_id`) - for un-global banned people, can be used only in group
» /update - update your bot to latest version
» /restart - restart your bot server
» /leaveall - order userbot to leave from all group
» /leavebot (`chat id`) - order bot to leave from the group you specify
» /broadcast (`message`) - send a broadcast message to all groups in bot database
» /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⚠️ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("Nothing is streaming in the vc❗️", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⚠️ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⚠️ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
