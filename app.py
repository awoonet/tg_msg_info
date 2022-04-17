from os import getenv as env
from pyrogram import Client

Client(
    "session/id_finder",
    env("API_ID"),
    env("API_HASH"),
    bot_token=env("TG_TOKEN"),
    plugins=dict(root="plugins"),
).run()
