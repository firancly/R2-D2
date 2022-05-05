import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
intents.message_content = True 
client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
    await client.load_extension("cogs.verification")
    print("Bot running with:")
    print("Username: ", client.user.name)
    print("User ID: ", client.user.id)

@client.command()
async def sync(ctx):
  await client.tree.sync(guild=discord.Object(id=967681206353289276))
  await ctx.message.delete()
  print("Synced!")

@client.command()	
async def load(ctx, extension):
	await client.load_extension(f"cogs.{extension}")

@client.command()	
async def unload(ctx, extension):
	await client.unload_extension(f"cogs.{extension}")

client.run("OTU5MDA2NTc5ODA4NjkwMjQ3.YkVmeg.wUX1tAi7WD3XUkj1EPT1vPy2hsE")