import discord
from discord.ext import commands
from urllib import parse, request
import datetime
import random
import asyncio

class subCog(commands.Cog, name="Sub"):
    def _init_(self, bot):self.bot = bot

    @commands.command(pass_context=True)
    async def oy(self, ctx, *, arg):
        
        yas = '✔️' 
        idk = '♻️'
        nay = '❌'
        
        embed = discord.Embed(title=f"{ctx.author.name} asks:", description=f"{arg}", color=ctx.author.color)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        message = await ctx.send(embed=embed)
        
        await message.add_reaction(yas)
        await message.add_reaction(idk)
        await message.add_reaction(nay)   
        await ctx.message.delete()

    @commands.command(pass_context=True)
    async def anket(self, ctx, *, arg = None):

        one = '1️⃣'
        two = '2️⃣'
        three = '3️⃣'
        four = '4️⃣'
        five = '5️⃣'

        embed = discord.Embed(title=f"{arg[:-1]}", color=ctx.author.color)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        message = await ctx.send(embed=embed)

        last = int(arg[-1])

        if last <= 1:
            await ctx.send('You need at least two options to make a poll!')
        elif last > 5:
            await ctx.send("You can't add more than 5 choices")
            await ctx.message.delete()
        elif last == 2:
            await message.add_reaction(one)
            await message.add_reaction(two)
            await ctx.message.delete()
        elif last == 3:
            await message.add_reaction(one)
            await message.add_reaction(two)
            await message.add_reaction(three)
            await ctx.message.delete()
        elif last == 4:
            await message.add_reaction(one)
            await message.add_reaction(two)
            await message.add_reaction(three)
            await message.add_reaction(four)
            await ctx.message.delete()
        elif last == 5:
            await message.add_reaction(one)
            await message.add_reaction(two)
            await message.add_reaction(three)
            await message.add_reaction(four)
            await message.add_reaction(five)
            await ctx.message.delete()
 
    @commands.command()
    async def pp(self, ctx, user:discord.Member = None):
        
        if user is None:
            user=ctx.author
        
        embed = discord.Embed(title=f"{ctx.author.name} asks to take a closer look at {user.name}", color=discord.Color.red())
        embed.set_image(url=user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def sor(self, ctx, *, arg = None):
        variable = [
            "tabii ki",
            "evet",
            "yoo",
            "dedim olabilir",
            "sankimsi",
            "niye olmasın?",
            "Valla bilmiyorum",
            "Ben nereden bileyim amk?",]
    
        if arg == None:
            await ctx.send("ee soru ne?")
            return
        if arg == "who is joe":
            embed = discord.Embed(title=f"{ctx.author.name} asks for my wisdom!", description=f"{arg}", color = discord.Color.blue())
            embed.add_field(name="My answer is...", value="Joe mama!")
            embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCtMzoeQ8IGRoiYslQrnccanwkl7DtAJXTTQ&usqp=CAU")
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return
    
        embed = discord.Embed(title=f"{ctx.author.name} benim bilgeliğime muhtaç!", description=f"{arg}", color = discord.Color.blue())
        embed.add_field(name="Cevabım Şudur!", value=(random.choice(variable)))
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCtMzoeQ8IGRoiYslQrnccanwkl7DtAJXTTQ&usqp=CAU")
        
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    async def bilgi(self, ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}", description="Ben bot!", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Sunucu Oluşturma Tarihi", value=f"{ctx.guild.created_at}")
        embed.add_field(name="Sunucu Bölgesi", value=f"{ctx.guild.region}")
        embed.add_field(name="Sunucu TC'si", value=f"{ctx.guild.id}")
    
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(subCog(bot))
    print('Sub Commands Loaded')
