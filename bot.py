import discord
from discord.ext import commands
import random
import asyncio
import sys
import os
from cogs.Turkish import TRCog
from cogs.sub import subCog
from cogs.em import emCog
from cogs.economy import BeansEconomyCog

# From Heroku's own docs
DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL is None:
    DATABASE_URL = "postgres://postgres:password@127.0.0.1:5432/patridb"

bot = commands.Bot(command_prefix=[", ", "Asker " ], help_command=None, allowed_mentions=discord.AllowedMentions(roles=False, users=False, everyone=False))
bot.add_cog(TRCog(bot))
bot.add_cog(subCog(bot))
bot.add_cog(emCog(bot))
bot.add_cog(BeansEconomyCog(bot, DATABASE_URL))

@bot.event
async def on_ready():
    print("Göreve Hazır!")
    game = discord.Game("Asker yardım! Prefixim ,")    
    await bot.change_presence(status=discord.Status.idle, activity=game)

#Basic Commands

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
        embed = discord.Embed(title="Kod:3131 Aktif, Bombalar Ateşlendi", description=f"{ctx.author.name}'nin Emriyle bombalam işlemi gerçekleştirildi", color=discord.Color.dark_red())
        embed.set_image(url="https://galeri8.uludagsozluk.com/415/gif_851233.gif")
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

#help command

@bot.group(invoke_without_command=True)
async def yardım(ctx):

    embed = discord.Embed(title="TSK Bot", description="Bot işte amk", color = ctx.author.color)
    embed.set_thumbnail(url="https://cdn.freelogovectors.net/wp-content/uploads/2020/12/turk-silahli-kuvvetleri-logo.png")
    
    embed.add_field(name="yardım", value="Bu mesajı gösterir", inline=False)
    embed.add_field(name="Fun Commands", value="ara, ban, bruh, bonk, bully, declarecommunism, F, hug, invade, kick, kill, kiss, lap, marry, nuke, pat, say, suck, warn, question")
    embed.add_field(name="Useful Commands", value="pfp, ping, poll, info, vote")
    
    await ctx.send(embed=embed)

# Run the bot with a token specified via the command line or at the environment variable PATRI_DISCORD_TOKEN.
if len(sys.argv) > 1:
    os.environ["PATRI_DISCORD_TOKEN"] = str(sys.argv[1])

bot_token = os.environ.get("PATRI_DISCORD_TOKEN")

if bot_token is None:
    print("Missing a bot token! Please specify a bot token as the first command line argument.")
else:
    print("Attempting to start the bot...")
    bot.run(bot_token)
