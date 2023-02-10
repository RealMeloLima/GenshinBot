import os
import discord as dc
from discord.ext import commands
from discord.ext.commands import Paginator
import asyncio

# INTENTS
intents = dc.Intents.all()

client = commands.Bot(command_prefix='?', intents = intents)

# HELP
@client.command(name='Help')
async def help(ctx):
    await ctx.message.channel.send("""Feeling lost ? The following commands are currently avaiable:
```?builds (all builds avaiable))
?Character name (ex: ?Qiqi)```
For any futher questions send to my Github:https://github.com/RealMeloLima""")

# TESTE
@client.event
async def on_ready():
    print(f'Im ready and logged on {client.user}')

# LISTA DOS PERSONAGENS
items = ['Albedo', 'Alhaitham', 'Ayaka' , 'Bennett', 'Childe' , 'Collei' ,'Cyno', 'Diluc', 'Eula' , 'Faruzan', 'Fischl', 'Ganyu', 'Gorou' ,'Heizou', 'Hutao', 'Itto', 'Kazuha', 'Mona', 'Nahida' ,'Qiqi', 'Rainden', 'Sara', 'Sayu', 'Shinobu', 'Sucrose'  , 'Thoma', 'Tighnari', 'Venti', 'Wanderer', 'Xiao', 'Xingqiu' ,'Xinyan', 'Yanfei', 'YaoYao', 'Yelan', 'Yoimiya', 'Zhongli']
pages = [items[i:i + 10] for i in range(0, len(items), 10)]

@client.command(name='Builds')
async def list_items(ctx):
    current_page = 0
    await ctx.message.channel.send("All the builds we have on now are:")
    message = await ctx.send("```\n" + "\n".join(pages[current_page]) + "```")
    await message.add_reaction("⬅️")
    await message.add_reaction("➡️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["⬅️", "➡️"]

    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
            if str(reaction.emoji) == "⬅️":
                current_page = max(current_page - 1, 0)
                await message.edit(content="```\n" + "\n".join(pages[current_page]) + "```")
            elif str(reaction.emoji) == "➡️":
                current_page = min(current_page + 1, len(pages) - 1)
                await message.edit(content="```\n" + "\n".join(pages[current_page]) + "```")
        except asyncio.TimeoutError:
            break
# IMAGEM DO PERSONAGEM   
for item in items:
    def build_func(item):
        @client.command(name=item)
        async def build(ctx):
            file_name = f"{item.lower()}.png"
            if not os.path.exists(file_name):
                await ctx.message.channel.send("Sorry, We do not have this build right now :(")
                return
            await ctx.message.channel.send(f"Here's you {item} build, enjoy it :)")
            await ctx.message.channel.send(file=dc.File(file_name))
    build_func(item)

client.run('MTA2NjQxNTkyMzQyODM0MzkxOQ.GhbcnW.N91zW5fxPMssV5YymSYfrH0QhJeZA_i_ECJ8yw')