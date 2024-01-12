import discord
from discord.ext import commands
from os import environ

TOKEN = environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    converted_message = convert_to_large_letter(message.content)
    if converted_message:
        await message.channel.send(converted_message)

def convert_to_large_letter(text):
    if isinstance(text, int):
        print("Message is number")
        return
    # Convert each character to the corresponding regional indicator
    converted_text = ""
    for lol in text:
        converted_text += "  " + ":regional_indicator_" + lol.lower() + ":"
    # converted_text = ' '.join([f':regional_indicator_{char.lower()}:' if char.isalpha() else char for char in text])
    return converted_text

# Replace 'YOUR_TOKEN' with your bot token
bot.run(TOKEN)
