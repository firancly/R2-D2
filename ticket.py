from cProfile import label
from unicodedata import name
import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ui import Button, View
from discord import Intents
import asyncio
import json


intents = discord.Intents.all()
intents.message_content = True 
client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", client.user.name)
    print("User ID: ", client.user.id)

@client.command()
async def sync(ctx):
  await client.tree.sync(guild=discord.Object(id=844747238445023242))
  await ctx.message.delete()
  print("Synced!")

@client.command()
@has_permissions(manage_channels=True)
async def rename(ctx, new_name: str='new-name'):
  await ctx.channel.edit(name=new_name)

@client.command()
async def ticket(ctx): 
  button1 = Button(label = "Ticket", style = discord.ButtonStyle.green)
  button2 = Button(label = "Close", style = discord.ButtonStyle.red)
  category = discord.utils.get(ctx.guild.categories, name="tickets")

  async def button_callback(interaction: discord.Interaction):
    ticket_channel = await interaction.guild.create_text_channel(name="ticket", category=category)

    async def button2_callback(interaction: discord.Interaction):
      await interaction.channel.delete()

    button2.callback = button2_callback
    view2 = View()
    view2.add_item(button2)
    await ticket_channel.set_permissions(interaction.user, read_messages=True, send_messages=True, read_message_history=True)
    await ticket_channel.edit(permissions_synced=True)
    

    await ticket_channel.send(embed=embed, view=view2)

  view = View()
  button1.callback = button_callback
  view.add_item(button1)

  embed = discord.Embed(title="New ticket from {}#{}".format(ctx.author.name, ctx.author.discriminator), description= "お待ちください。まもなくご案内します。", color=0x00a8ff)

  await ctx.send(embed = discord.Embed(title = "Ticket", description = "サーバーへようこそ！ チケットを開いて私に連絡してください。"), view = view)


client.run("TOKEN")