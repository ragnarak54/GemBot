import config

import cv2
import discord
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
        print(msg.author)
        print(msg.attachments)
        break


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(config.token)
