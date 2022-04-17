from pyrogram import Client as app, filters

@app.on_message(filters.private)
def id_formatter(_, msg):

  user = msg.from_user
  txt = "Requested information about message:"
  txt += f"\n**You:** __{user.first_name} __"
  txt += f"__{user.last_name}__" if user.last_name is not None else ""
  txt += f"__ (@{user.username})__" if user.username is not None else ""
  txt += f"\n**Your ID:** __{user.id}__"

  if msg.forward_from_chat is not None:
      txt += "\n**Forwarded from:**"
      txt += f"\n**Chat:** __{msg.forward_from_chat.title}__"
      txt += f"\n**Chat ID:** __{msg.forward_from_chat.id}__"
  if msg.forward_from_message_id is not None:
      txt += f"** / **__{msg.forward_from_message_id}__"

  if msg.forward_from is not None:
      user = msg.forward_from
      txt += f"\n**User:** __{user.first_name} __"
      txt += f"__{user.last_name}__" if user.last_name is not None else ""
      txt += f"__ (@{user.username})__" if user.username is not None else ""
      txt += f"\n**User ID:** __{user.id}__"
  if msg.forward_sender_name is not None:
      txt += "\n**Forwarded from user:**"
      txt += f"\n**User:** __{msg.forward_sender_name} __"

  if msg.text is not None:
      txt += f"\n**Text:**\n{msg.text.html}"

  if msg.media is not None and msg.media:
      if msg.audio is not None:
          txt += f"\n**Audio ID**: __{msg.audio.file_id}__"
      elif msg.document is not None:
          txt += f"\n**Document ID**: __{msg.document.file_id}__"
      elif msg.photo is not None:
          txt += f"\n**Photo ID**: __{msg.photo.file_id}__"
      elif msg.sticker is not None:
          txt += f"\n**Sticker ID**: __{msg.sticker.file_id}__"
      elif msg.animation is not None:
          txt += f"\n**Animation ID**: __{msg.animation.file_id}__"
      elif msg.video is not None:
          txt += f"\n**Video ID**: __{msg.video.file_id}__"
      elif msg.voice is not None:
          txt += f"\n**Voice ID**: __{msg.voice.file_id}__"
      elif msg.video_note is not None:
          txt += f"\n**Video note ID**: __{msg.video_note.file_id}__"
      if msg.media_group_id is not None:
          txt += f"\n**Media group ID**: __{msg.media_group_id}__"
      if msg.caption is not None:
          txt += f"\n**Caption**:\n{msg.caption}\n"

  msg.reply(txt)
