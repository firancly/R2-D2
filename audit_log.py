import discord 
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
intents.message_content = True 
client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", client.user.name)
    print("User ID: ", client.user.id)



client.run("TOKEN")