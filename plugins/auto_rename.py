from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import madflixbotz

@Client.on_message(filters.private & filters.command("autorename"))
async def auto_rename_command(client, message):
    user_id = message.from_user.id

    # Extract the format from the command
    format_template = message.text.split("/autorename", 1)[1].strip()

    # Save the format template to the database
    await madflixbotz.set_format_template(user_id, format_template)

    await message.reply_text("**Auto Rename Format Updated Successfully! ✅**")
