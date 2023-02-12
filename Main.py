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
?Character name (ex: ?Qiqi)
?Banner (Current and next Banners)```
For any futher questions send to my Github:https://github.com/RealMeloLima""")

# TESTE
@client.event
async def on_ready():
    print(f'Im ready and logged on {client.user}')

# LISTA DOS PERSONAGENS
items = ['Albedo', 'Alhaitham', 'Aloy', 'Amber_DPS', 'Amber_SUP','Ayaka', ' Ayato', 'Barbara', 'Beidou' ,'Bennett','Candace' ,'Childe', 'Chongyun' ,'Collei' ,'Cyno', 'Diluc', 'Diona', 'Dori' ,'Eula' , 'Faruzan', 'Fischl', 'Ganyu', 'Gorou' ,'Heizou', 'Hutao', 'Itto', 'Jean', 'Kaeya', 'Kazuha', 'Keqing', 'Klee', 'Kokomi', 'Layla', 'Lisa', 'Mona', 'Mona_FREEZE', 'Mona_NUKE', 'Nahida', 'Nilou', 'Ningguang', 'Noelle', 'Qiqi', 'Rainden', 'Razor', 'Rosaria' ,'Sara', 'Sayu', 'Shenhe' ,'Shinobu', 'Shogun', 'Sucrose', 'Tartaglia' ,'Thoma', 'Tighnari', 'Venti', 'Wanderer', 'Xiangling' ,'Xiao', 'Xingqiu' ,'Xinyan', 'Yaemiko' ,'Yanfei', 'YaoYao', 'Yelan', 'Yoimiya', 'Yunjin' ,'Zhongli']
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
    path = 'C:/Users/Paulo R. Melo Lima/Documents/GitHub/GenshinBot/imagens'
    file_name = os.path.join(path, f"{item.lower()}.png")
    def build_func(item, file_name):
        @client.command(name=item)
        async def build(ctx):
            if not os.path.exists(file_name):
                await ctx.message.channel.send("Sorry, We do not have this build right now :(")
                return
            await ctx.message.channel.send(f"Here's you {item} build, enjoy it :)")
            await ctx.message.channel.send(file=dc.File(file_name))
    build_func(item, file_name)

# BANNER (ROTATIVO)
@client.command(name='Banner')
async def banner(ctx):
    await ctx.message.channel.send("Crrent aund future Banners. Enjoy it :)")
    await ctx.message.channel.send(file=dc.File('banner.png'))

client.run('Your TOKEN goes here')
