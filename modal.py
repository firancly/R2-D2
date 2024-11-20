import discord
from discord.ext import commands
from discord import app_commands
import traceback
from discord.ui import Button, View
import time

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix = "!", intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.command()
async def sync(ctx):
  await client.tree.sync(guild=discord.Object(id=TEST_GUILD))
  await ctx.message.delete()
  print("Synced!")

TEST_GUILD = 844747238445023242

class Questionnaire(discord.ui.Modal, title='Question'):
    name = discord.ui.TextInput(label='Name')
    answer = discord.ui.TextInput(label='Question', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        channel = discord.utils.get(interaction.guild.channels, id=963010017836011591)
        msg = await interaction.response.send_message(f'Thanks for your response, {self.name}!', ephemeral=True)
        time.sleep(2)
        await channel.send(f"{self.name}'s feedback")
        await channel.send(f"{self.answer} is the persons feedback")

@client.tree.command(description="Ask questions")
@app_commands.guilds(TEST_GUILD)
async def question(interaction: discord.Interaction):
    await interaction.response.send_modal(Questionnaire())

client.run("TOKEN")