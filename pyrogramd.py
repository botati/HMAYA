from pyrogram import Client, filters

bot_token = "6015943087:AAESayEILdp5Eu2tpHyUZGmNKjdaTXQqYzM"

api_id = 26594855
api_hash = "714a6f72d41876b9209b7c1383c2a3c9"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

