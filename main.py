import json, os, logging, time, re, string, os.path
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks


dir = os.path.dirname(__file__)

#Program Functions
load_dotenv(os.path.join(dir, ".env"))

# Discord ID info
activity = discord.Activity(type=discord.ActivityType.watching, name="you")
author_id = "318122785807269888"
intents = discord.Intents.all()

# Logger
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)


# Bot info
bot = commands.Bot(
    token=os.environ.get("KEY"),
    intents=intents,
    command_prefix="mv.",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    activity=activity,
    status=discord.Status.idle,
)

# Author ID
bot.author_id = author_id  # Change to your discord id!!!

with open("bad-words.txt") as file: # bad-words.txt contains one phrase per line
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
self_ = bot.get_user(1052716430413541448)

#Message respond event
@bot.event
async def on_message(message):

    if (not message.author.bot):
        return

    if message.channel.id != 1145338032409563136:
        return

    if (message.author.id == 1052716430413541448):
        return
    if isinstance(message.channel, discord.channel.DMChannel):
        return

    if any(bad_word in message.content for bad_word in bad_words):
        for x in bad_words:
            bad_word_ = x
            if x in message.content:
                break

        channel = bot.get_channel(1149122307349033090)
        await message.delete()
        await channel.send(content=None, embed=discord.Embed.from_dict(
    {
      "title": f"Mortal Vex bot blocked a message in #{message.channel}" ,
      "color": 0,
      "description": f"{message.author.mention} said: {message.content}",
      "timestamp": "",
      "author": {
        "name": "",
        "icon_url": ""
      },
      "image": {},
      "thumbnail": {},
      "footer": {},
      "fields": [
        {
          "name": "Keyword:",
          "value": f"{bad_word_}"
        }
      ]
    }
  ))
    else:
        return


#run
if __name__ == "__main__":
    bot.run(os.environ.get("KEY"))