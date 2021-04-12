import config

import discord
from io import BytesIO
from PIL import Image
import pytesseract

from discord.ext import commands

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('ready')


@bot.command()
async def get_gems(ctx, channel: discord.TextChannel):
    hist = channel.history()
    async for msg in hist:
        buffer = BytesIO()
        await msg.attachments[0].save(buffer)
        buffer.seek(0)
        img = Image.open(buffer)
        print(pytesseract.image_to_string(img))
        break


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(config.token)
