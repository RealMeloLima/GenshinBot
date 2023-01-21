import discord as dc
from discord.ext import commands
from discord.flags import Intents
import asyncio


intents = dc.Intents.all()
client = commands.Bot(command_prefix='?', intents = intents)

@client.event
async def on_ready():
    print(f'Im ready and logged on {client.user}')



@client.command(name = 'builds')
async def build(context):
    await context.message.channel.send("""  Hello! Here are the builds I have on now :)
```Faruzan
Wanderer
Tighnari
Gyno
Albedo
Xiao
Shinobu
Yelan
Yoimiya (1)
Heizou
Kazuha
Thoma
Itto
Mona
Sara
Childe
Ganyu
Xinyan
Qiqi
Eula
Yoimiya (2)
Fischl
Venti
Sucrose
Yanfei
Sayu
Rainden
Ayaka
Zhongli
Hu tao
Bennett
Diluc ```
Don't forget to add the '?' at the beggining of the character name to see his build """)

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

# GYNO
@client.command(name = 'Gyno')
async def build(context):
    await context.message.channel.send('Here you have your Gyno build, enjoy it :)')
    await context.message.channel.send(file=dc.File("gyno.png"))

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

# YOIMIYA(1)
@client.command(name = 'Yoimiya (1)')
async def build(context):
    await context.message.channel.send('Here you have your Yoimiya (1) build, enjoy it :)')
    await context.message.channel.send(file=dc.File("yoimiya(1).png"))

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

# YOIMIYA(2)
@client.command(name = 'Yoimiya(2)')
async def build(context):
    await context.message.channel.send('Here you have your Yoimiya(2) build, enjoy it :)')
    await context.message.channel.send(file=dc.File("yoimiya(2).png"))

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

# RAYDEN
@client.command(name = 'Rayden')
async def build(context):
    await context.message.channel.send('Here you have your Rayden build, enjoy it :)')
    await context.message.channel.send(file=dc.File("rayden.png"))

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
@client.command(name = 'Bennette')
async def build(context):
    await context.message.channel.send('Here you have your Bennette build, enjoy it :)')
    await context.message.channel.send(file=dc.File("bennette.png"))

# DILUC
@client.command(name = 'Diluc')
async def build(context):
    await context.message.channel.send('Here you have your Diluc build, enjoy it :)')
    await context.message.channel.send(file=dc.File("diluc.png"))



client.run('MTA2NjQxNTkyMzQyODM0MzkxOQ.GKRqSK.yQIGz8rw1zrVf-UXFTpBHK_uwmRxXDbxWtLjvM')