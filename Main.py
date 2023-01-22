import discord as dc
from discord.ext import commands
from discord.ext.commands import Paginator
from discord.flags import Intents
import asyncio



intents = dc.Intents.all()
client = commands.Bot(command_prefix='?', intents = intents)

@client.event
async def on_ready():
    print(f'Im ready and logged on {client.user}')


items = ['Albedo', 'Ayaka' , 'Bennett', 'Childe' , 'Collei' ,'Cyno', 'Diluc', 'Eula' , 'Faruzan', 'Fischl', 'Ganyu', 'Heizou', 'Hu tao', 'Itto', 'Kazuha', 'Mona', 'Qiqi', 'Rainden', 'Sara', 'Sayu', 'Shinobu', 'Sucrose', 'Thoma', 'Tighnari', 'Venti', 'Wanderer', 'Xiao', 'Xinyan', 'Yanfei', 'Yelan', 'Yoimiya', 'Zhongli' ]

paginator = Paginator()
paginator.items_per_page = 10
for item in items:
    paginator.add_line(item)


@client.command(name='list')
async def list_items(ctx):
    for page in paginator.pages:
        await ctx.send(page)

@client.command(name='builds')
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
        
# FARUZAN
@client.command(name = 'Faruzan')
async def build(context):
    await context.message.channel.send('Here you have your Faruzan build, enjoy it :)')
    await context.message.channel.send(file=dc.File("faruzan.png"))

# WANDERER
@client.command(name = 'Wanderer')
async def build(context):
    await context.message.channel.send('Here you have your Wanderer build, enjoy it :)')
    await context.message.channel.send(file=dc.File("wanderer.png"))

# TIGHNARI
@client.command(name = 'Tighnari')
async def build(context):
    await context.message.channel.send('Here you have your Tighnari build, enjoy it :)')
    await context.message.channel.send(file=dc.File("Tighnari.png"))

# CYNO
@client.command(name = 'Cyno')
async def build(context):
    await context.message.channel.send('Here you have your Cyno build, enjoy it :)')
    await context.message.channel.send(file=dc.File("cyno.png"))

# ALBEDO
@client.command(name = 'Albedo')
async def build(context):
    await context.message.channel.send('Here you have your Albedo build, enjoy it :)')
    await context.message.channel.send(file=dc.File("albedo.png"))

# XIAO
@client.command(name = 'Xiao')
async def build(context):
    await context.message.channel.send('Here you have your Xiao build, enjoy it :)')
    await context.message.channel.send(file=dc.File("xiao.png"))

# SHINOBU
@client.command(name = 'Shinobu')
async def build(context):
    await context.message.channel.send('Here you have your Shinobu build, enjoy it :)')
    await context.message.channel.send(file=dc.File("shinobu.png"))

# YELAN
@client.command(name = 'Yelan')
async def build(context):
    await context.message.channel.send('Here you have your Yelan build, enjoy it :)')
    await context.message.channel.send(file=dc.File("yelan.png"))

# HEIZOU
@client.command(name = 'Heizou')
async def build(context):
    await context.message.channel.send('Here you have your Heizou build, enjoy it :)')
    await context.message.channel.send(file=dc.File("heizou.png"))

# KAZUHA
@client.command(name = 'Kazuha')
async def build(context):
    await context.message.channel.send('Here you have your Kahuza build, enjoy it :)')
    await context.message.channel.send(file=dc.File("kahuza.png"))

# THOMA
@client.command(name = 'Thoma')
async def build(context):
    await context.message.channel.send('Here you have your Thoma build, enjoy it :)')
    await context.message.channel.send(file=dc.File("thoma.png"))

# ITTO
@client.command(name = 'Itto')
async def build(context):
    await context.message.channel.send('Here you have your Itto build, enjoy it :)')
    await context.message.channel.send(file=dc.File("itto.png"))

# MONA
@client.command(name = 'Mona')
async def build(context):
    await context.message.channel.send('Here you have your Mona build, enjoy it :)')
    await context.message.channel.send(file=dc.File("mona.png"))

# SARA
@client.command(name = 'Sara')
async def build(context):
    await context.message.channel.send('Here you have your Sara build, enjoy it :)')
    await context.message.channel.send(file=dc.File("sara.png"))

# CHILDE
@client.command(name = 'Childe')
async def build(context):
    await context.message.channel.send('Here you have your Childe build, enjoy it :)')
    await context.message.channel.send(file=dc.File("childe.png"))

# GANYU
@client.command(name = 'Ganyu')
async def build(context):
    await context.message.channel.send('Here you have your Ganyu build, enjoy it :)')
    await context.message.channel.send(file=dc.File("ganyu.png"))

# XINYAN
@client.command(name = 'Xinyan')
async def build(context):
    await context.message.channel.send('Here you have your Xinyan build, enjoy it :)')
    await context.message.channel.send(file=dc.File("xinyan.png"))

# QIQI
@client.command(name = 'Qiqi')
async def build(context):
    await context.message.channel.send('Here you have your Qiqi build, enjoy it :)')
    await context.message.channel.send(file=dc.File("qiqi.png"))

# EULA
@client.command(name = 'Eula')
async def build(context):
    await context.message.channel.send('Here you have your Eula build, enjoy it :)')
    await context.message.channel.send(file=dc.File("eula.png"))

# YOIMIYA
@client.command(name = 'Yoimiya')
async def build(context):
    await context.message.channel.send('Here you have your Yoimiya build, enjoy it :)')
    await context.message.channel.send(file=dc.File("yoimiya.png"))

# FISCHL
@client.command(name = 'Fischl')
async def build(context):
    await context.message.channel.send('Here you have your Fischl build, enjoy it :)')
    await context.message.channel.send(file=dc.File("fischl.png"))

# VENTI
@client.command(name = 'Venti')
async def build(context):
    await context.message.channel.send('Here you have your Venti build, enjoy it :)')
    await context.message.channel.send(file=dc.File("venti.png"))

# SUCROSE
@client.command(name = 'Sucrose')
async def build(context):
    await context.message.channel.send('Here you have your Sucrose build, enjoy it :)')
    await context.message.channel.send(file=dc.File("sucrose.png"))

# YANFEI
@client.command(name = 'Yanfei')
async def build(context):
    await context.message.channel.send('Here you have your Yanfei build, enjoy it :)')
    await context.message.channel.send(file=dc.File("yanfei.png"))

# SAYU
@client.command(name = 'Sayu')
async def build(context):
    await context.message.channel.send('Here you have your Sayu build, enjoy it :)')
    await context.message.channel.send(file=dc.File("sayu.png"))

# RAIDEN
@client.command(name = 'Raiden')
async def build(context):
    await context.message.channel.send('Here you have your Raiden build, enjoy it :)')
    await context.message.channel.send(file=dc.File("raiden.png"))

# AYAKA
@client.command(name = 'Ayaka')
async def build(context):
    await context.message.channel.send('Here you have your Ayaka build, enjoy it :)')
    await context.message.channel.send(file=dc.File("ayaka.png"))

# ZHONGLI
@client.command(name = 'Zhongli')
async def build(context):
    await context.message.channel.send('Here you have your Zhongli build, enjoy it :)')
    await context.message.channel.send(file=dc.File("zhongli.png"))

# HU TAO
@client.command(name = 'Hutao')
async def build(context):
    await context.message.channel.send('Here you have your Hu tao build, enjoy it :)')
    await context.message.channel.send(file=dc.File("hutao.png"))

# BENNETTE
@client.command(name = 'Bennett')
async def build(context):
    await context.message.channel.send('Here you have your Bennett build, enjoy it :)')
    await context.message.channel.send(file=dc.File("bennette.png"))

# DILUC
@client.command(name = 'Diluc')
async def build(context):
    await context.message.channel.send('Here you have your Diluc build, enjoy it :)')
    await context.message.channel.send(file=dc.File("diluc.png"))

# COLLEI
@client.command(name = 'Collei')
async def build(context):
    await context.message.channel.send('Here you have your Collei build, enjoy it :)')
    await context.message.channel.send(file=dc.File("collei.png"))


client.run('MTA2NjQxNTkyMzQyODM0MzkxOQ.GIqaYr.Kjz7cklmtf4iHgUA7jL_9z_0azUMRW6mT69_bs')

