import os
import discord as dc
from discord.ext import commands
from discord.ext.commands import Paginator
import asyncio

# INTENTS
intents = dc.Intents.all()
client = commands.Bot(command_prefix='?', intents = intents)

# TESTE
@client.event
async def on_ready():
    print(f'Im ready and logged on {client.user}')

# LISTA DOS PERSONAGENS
items = ['Albedo', 'Alhaitham', 'Ayaka' , 'Bennett', 'Childe' , 'Collei' ,'Cyno', 'Diluc', 'Eula' , 'Faruzan', 'Fischl', 'Ganyu', 'Gorou' ,'Heizou', 'Hu tao', 'Itto', 'Kazuha', 'Mona', 'Qiqi', 'Rainden', 'Sara', 'Sayu', 'Shinobu', 'Sucrose', 'Thoma', 'Tighnari', 'Venti', 'Wanderer', 'Xiao', 'Xinyan', 'Yanfei', 'YaoYao', 'Yelan', 'Yoimiya', 'Zhongli']

paginator = Paginator()
paginator.items_per_page = 10
for item in items:
    paginator.add_line(item)

@client.command(name='Builds')
async def list_items(ctx):
    current_page = 0
    message = await ctx.send(paginator.pages[current_page])
    await message.add_reaction("⬅️")
    await message.add_reaction("➡️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["⬅️", "➡️"]

    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
            if str(reaction.emoji) == "⬅️":
                current_page = max(current_page - 1, 0)
                await message.edit(content=paginator.pages[current_page])
            elif str(reaction.emoji) == "➡️":
                current_page = min(current_page + 1, len(paginator.pages) - 1)
                await message.edit(content=paginator.pages[current_page])
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
            await ctx.message.channel.send(f'Here you have your {item} build, enjoy it :)')
            await ctx.message.channel.send(file=dc.File(file_name))
    build_func(item)


client.run('YOUR TOKEN GOES HERE')
