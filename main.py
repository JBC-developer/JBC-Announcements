import discord
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix="?", intents= discord.Intents.all())

@bot.event
async def on_ready():
    print("Im JBC announcement bot")

    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name="announce", description="Send a message to every member of the server")
@app_commands.describe(message = "The message to send")
async def announce(interaction : discord.Interaction, message : str):
    dev_id = ["857892645543215116","745583659389681675"]
    if str(interaction.user.id) not in dev_id:
        await interaction.response.send_message("This command is only for the owner", ephemeral=True)
        return 

    i = 0
    await interaction.response.send_message(f"Sending messages...", ephemeral=True)

    guild = bot.get_guild(interaction.guild_id)
    try:
        for member in guild.members:
            try:
                embed = discord.Embed(title="**Announcement from JBC!**", description=message, color=0x00ff00)
                await member.send(embed=embed)
                i+=1
            except:
                pass
        await interaction.edit_original_response(content=f"Message announced to {i} members")
    except:
        await interaction.edit_original_response(content="There was an error, try again in some time.")

    

bot.run("MTIzMDAwNDQ0MTE5MzY0ODE1OA.GS7s8i.HTcIXjd8adhCOX-tAy_hnW_KwqcCIvhGXYKS6s")