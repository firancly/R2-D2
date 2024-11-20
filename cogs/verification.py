import discord
from discord.ext import commands
from discord.ui import Button, View

class verification(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def verification(self, ctx):
        button = Button(label = "Verify!", style = discord.ButtonStyle.green, emoji="✅")
        async def button_callback(interaction : discord.Interaction):
            member = interaction.user
            role = interaction.guild.get_role(970225359322751037)
            await member.add_roles(role)
            await interaction.response.send_message(embed = discord.Embed(f"Welcome! {ctx.author.name}, you have been granted {role.name} role!", color = discord.Colour.green))

        button.callback = button_callback
        view = View()
        view.add_item(button)
        await ctx.send("click the button below to verify", view=view)

async def setup(client):
    await client.add_cog(verification(client))