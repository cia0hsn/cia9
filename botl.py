import discord
from discord.ext import commands,tasks


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(command_prefix="$",intents=intents)


@bot.event
async def on_ready():
    print("ready ,. ")

    channel = bot.get_channel(1497255556556001362)

    await channel.send("im Running ...")




bot.run("MTQ5NzI1MzM2MjI3MjQ0MDQ3MA.GJsiiu.XGTxHxQR-fmPsCY50obTfNWZH88SV64Sy_Zcqg")
