import discord
from discord.ext import commands
import random
import asyncio
import sys
import os
from cogs.sub import subCog
from cogs.em import emCog
import requests

bot = commands.Bot(command_prefix=[",", "Asker ", "asker"], help_command=None, allowed_mentions=discord.AllowedMentions(roles=False, users=False, everyone=False))

@bot.event
async def on_ready():
    print("Göreve Hazır!")
    game = discord.Game(",yardım")
    await bot.change_presence(status=discord.Status.idle, activity=game)

#Basit

@bot.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! {round(bot.latency * 1000)} ms')

@bot.command()
async def de(ctx, *, arg):
    await ctx.send(f'{arg}')

@bot.command()
async def uyar(ctx,user:discord.Member, *, arg): 
    await ctx.send(f"{user.name} Senin ağzını yüzünü sikerim. Nedeni: {arg}")


@bot.command()
async def bomba(ctx):
    
    yas = '✔️'
    nay = '❌'

    embed = discord.Embed(title="Emin misiniz komutanım?", color = ctx.author.color)
    embed = discord.Embed(title="Nükleer bombaların kullanımını onaylıyor musunuz?", color = ctx.author.color)
    embed.add_field(name=f"ID: {ctx.author.name}", value="Erişim onaylandı...")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    message = await ctx.send(embed=embed)

    
    await message.add_reaction(yas)
    await message.add_reaction(nay)
    
    valid_reactions = ['✔️', '❌']
    
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in valid_reactions
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("İptal Edildi")
    
    if str(reaction.emoji) == yas:
        embed = discord.Embed(title="Kod:3131 Aktif, Bombalar Ateşlendi", description=f"{ctx.author.name}'nin Emriyle bombalama işlemi gerçekleştirildi", color=discord.Color.dark_red())
        embed.set_image(url="https://bestanimations.com/media/nuclear-explosions/726046542nuclear-atom-bomg-explosion-animated-gif-4.gif")
        return await ctx.send(embed=embed)
    
    await ctx.send("Süreç Terk Edildi") 
    
@bot.command()
async def ban(ctx, victim:discord.Member, *, reason= None):
    
    yas = '✔️'
    nay = '❌'

    if reason is None:
        reason = "Sebep Belirtilmedi"
    
    embed = discord.Embed(title="Bunu mu banlıyoruz?", color=discord.Color.dark_red())
    embed.add_field(name=f"Victim: {victim.name}", value="SG lan burdan irticacı pezeveng")
    embed.set_thumbnail(url=victim.avatar_url)
    message = await ctx.send(embed=embed)

    
    await message.add_reaction(yas)
    await message.add_reaction(nay)
    
    valid_reactions = ['✔️', '❌']
    
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in valid_reactions
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Tüm gün seni mi bekleyecem ben amk")
    
    if str(reaction.emoji) == yas:
        embed = discord.Embed(title=f"Eöir büyük yerden, bb {victim.name}...", description=f"{ctx.author.name} tarafından ATILDIN!. \n\n **Sebep:** {reason}", color=discord.Color.dark_red())
        embed.set_image(url="https://media1.tenor.com/images/11baffb759ae7ca9d984153cf53a7768/tenor.gif?itemid=8540510")
        return await ctx.send(embed=embed)
    
    await ctx.send("Forgiven") 

#yardım

@bot.group(invoke_without_command=True)
async def yardım(ctx):

    embed = discord.Embed(title="TSK Bot", description="Bot işte amk", color = ctx.author.color)
    embed.set_thumbnail(url="https://cdn.freelogovectors.net/wp-content/uploads/2020/12/turk-silahli-kuvvetleri-logo.png")
    
    embed.add_field(name="yardım", value="Bu mesajı gösterir", inline=False)
    embed.add_field(name="Eğlence Komutları", value="bruh, f35, F, işgal, kick, kızıl_devrim, pat, sarıl, sor, söv, vur, çay,")
    embed.add_field(name="Bi Sike Yarayan Komutlar", value="pp, ping, oy, doviz,  bilgi, anket")
    
    await ctx.send(embed=embed)

#Doviz

@bot.command()
async def doviz(ctx):

    results = requests.get('https://finans.truncgil.com/today.json').json()
    content = results['USD']['Satış']
    EUR = results['EUR']['Satış']
    GBP = results['GBP']['Satış']
    
    embed = discord.Embed(title="Kur Fiyatları", description="Ekonomi çok iyi moruk!")
    embed.set_thumbnail(url="https://www.krttv.com.tr/images/haberler/2020/05/berat_albayrak_yine_link_verdi_h36179_65dec.png")
    embed.add_field(name="USD: ", value=f"{content}")
    embed.add_field(name="EUR: ", value=f"{EUR}")
    embed.add_field(name="GBP: ", value=f"{GBP}")

    await ctx.send(embed=embed)

# Run the bot with a token specified via the command line or at the environment variable PATRI_DISCORD_TOKEN.
if len(sys.argv) > 1:
    os.environ["TSK_DISCORD_TOKEN"] = str(sys.argv[1])

bot_token = os.environ.get("TSK_DISCORD_TOKEN")

if bot_token is None:
    print("Token yok amuğoyum")
else:
    print("Attempting to start the bot...")
    bot.run(bot_token)
