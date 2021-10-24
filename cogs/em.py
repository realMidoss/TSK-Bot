import discord
from discord.ext import commands
import random
import asyncio

class emCog(commands.Cog, name="Sub"):
    def _init_(self, bot):self.bot = bot


    @commands.command()
    async def işgal(self, ctx):

        ww2 = [
        "https://thumbs.gfycat.com/AdventurousUnknownFiddlercrab-size_restricted.gif",
        "https://i.hizliresim.com/XRlk5m.jpg",      
        "https://media1.tenor.com/images/3429b07976597362b241a26f3e4aae44/tenor.gif?itemid=16949276", 
        "https://i.makeagif.com/media/8-03-2015/6BUOZw.gif", 
        "https://thumbs.gfycat.com/GentleCostlyDevilfish-max-1mb.gif",
        "https://thumbs.gfycat.com/WelloffAdventurousArkshell-size_restricted.gif"  
        ]

        embed = discord.Embed(title="Her şey vatan için!", description="Savulun Ulan deyyuslar!!!", color=discord.Color.red())
        embed.set_image(url=random.choice(ww2))

        await ctx.send(embed=embed)

    @commands.command()
    async def vur(self, ctx,user:discord.Member = None):
        if user is None:
            await ctx.send("Kimi vurayım?")
            return

        if user==ctx.author:
            
            intihar = [
            "https://media2.giphy.com/media/9EQD6VsEbMEb6/giphy.gif",
            "https://galeri14.uludagsozluk.com/776/hoslanilan-kizi-3-erkekle-kahkaha-atarken-gormek_1519340.gif",
            "https://thumbs.gfycat.com/AdorableAggravatingCaimanlizard-max-1mb.gif",]

            embed = discord.Embed(title=f"{ctx.author.name} intihar etti ", description="F")
            embed.set_image(url=random.choice(intihar))  
            
            await ctx.send(embed=embed)

            return
        
        killv = [
        "https://c.tenor.com/2LpRjHPPMdAAAAAC/military.gif",
        "https://i.pinimg.com/originals/4d/03/1b/4d031bee032331b45718aec28bcd7993.gif",
        "https://i2.milimaj.com/i/milliyet/75/0x0/5edb4202554287169cb60b2c.gif",] 

        embed = discord.Embed(title=f"{ctx.author.name}'nın namlusunun ucunda {user.name}", description="Bam Bam Bam", color=discord.Color.dark_red())
        embed.set_image(url=random.choice(killv)) 

        await ctx.send(embed=embed)    

    @commands.command()
    async def bruh(self, ctx):
        
        embed = discord.Embed(title=f"{ctx.author.name}, bunun bir bilader anı olduğnu düşünüyor", description="birader anı;", color=discord.Color.darker_gray())
        embed.set_image(url="https://i.ytimg.com/vi/ZF57zsOWdB0/maxresdefault.jpg")

        await ctx.send(embed=embed)

    @commands.command()
    async def kızıl_devrim(self, ctx):

        komün = [
        "https://media2.giphy.com/media/RMrNQ0HszuxzmvdBdw/giphy.gif",
        "https://31.media.tumblr.com/1c34ba04ed84aa28afa59511a1b4f99c/tumblr_inline_np4407k8KS1rfowug_500.gif",
        ]
        embed = discord.Embed(title=f"vay amk komünisti seni {ctx.author}", description="SG lan bu sunucudan", color=discord.Color.dark_red())
        embed.set_image(url=random.choice(komün)) 

        await ctx.send(embed=embed)

    #Burda Kaldın

    @commands.command()
    async def sarıl(self, ctx,user:discord.Member = None):
        if user is None:
            await ctx.send("You can't hug air. Tag our lucky boy UwU")
            return
        if user==ctx.author:
            await ctx.send("You cant hug yourself. but your left hand is available")
            return
        
        hugv = [
        "https://data.whicdn.com/images/125740919/original.gif",
        "https://i.pinimg.com/originals/f2/80/5f/f2805f274471676c96aff2bc9fbedd70.gif",
        "https://media2.giphy.com/media/l2QDM9Jnim1YVILXa/source.gif",
        ]

        embed = discord.Embed(title=f"{ctx.author.name} hugs {user.name}", description="Ain't this cute? I envy them...", color = ctx.author.color)
        embed.set_image(url=random.choice(hugv)) 

        await ctx.send(embed=embed)

    @commands.command()
    async def bully(self, ctx,user:discord.Member = None):
        if user is None:
            await ctx.send("ummm... Ever heard of mentioning other users?")
            return
        if user==ctx.author:
            await ctx.send("Why would you want to bully yourself? Just look at the mirror")
            return

        embed = discord.Embed(title=f"{ctx.author.name} bullies {user.name}", color=discord.Color.blue())
        embed.set_image(url="https://i.pinimg.com/736x/73/08/39/730839953404c1d46a158f12c5c4f78f.jpg")

        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx,user:discord.Member = None):
        if user is None:
            await ctx.send("Kiss what? More likely who? :kekw: Will you kiss air, you poor thing?")
            return
        if user==ctx.author:
            await ctx.send("OMG did you just try to kiss yourself :kekw:")
            return

        öp = [
        "https://media3.giphy.com/media/12VXIxKaIEarL2/giphy.gif",
        "https://37.media.tumblr.com/7bbfd33feb6d790bb656779a05ee99da/tumblr_mtigwpZmhh1si4l9vo1_500.gif",
        "https://data.whicdn.com/images/239776661/original.gif",
        "https://i.pinimg.com/originals/f8/e8/8e/f8e88eccd2737d5805d645a85d1dbc0f.gif",
        "https://i.pinimg.com/originals/21/82/d8/2182d81bc459732fdf9bf94d1dd068c4.gif",
        ]

        embed = discord.Embed(title=f"{ctx.author.name} kissed {user.name}...", description="Ahh young love...", color=discord.Color.magenta())
        embed.set_image(url=random.choice(öp)) 

        await ctx.send(embed=embed)

    @commands.command()
    async def suck(self, ctx):

        embed = discord.Embed(title=f"{ctx.author.name} sucks", description="no not like that you perverted!")
        embed.set_image(url="https://cdn.discordapp.com/attachments/757701650537250957/780183991474454528/popsicleporn.gif")

        await ctx.send(embed=embed)

    @commands.command()
    async def F(self, ctx):

        Fv = [
        "https://i.kym-cdn.com/entries/icons/mobile/000/017/039/pressf.jpg",
        "https://i.pinimg.com/originals/4c/c5/3a/4cc53a5ae71234a0fd79998a8d2a802f.png",
        "https://cdn.ebaumsworld.com/thumbs/2019/02/14/060133/85886769/meme-fixed.jpg"
        ]

        embed = discord.Embed(title="F", color = ctx.author.color)
        embed.set_image(url=random.choice(Fv))

        await ctx.send(embed=embed)


    @commands.command()
    async def pat(self, ctx,user:discord.Member = None):
        if user is None:
            await ctx.send("Pat what? Mention someone")
            return
        
        if user==ctx.author:
            embed = discord.Embed(title=f"{ctx.author.name} pats theirselves... It's just sad")
            embed.set_image(url="https://pa1.narvii.com/6400/6a38438c39e60789ac39cfd7340acd868baeac90_00.gif")
            await ctx.send(embed=embed)
            return

        patv = [
        "https://i.imgur.com/LUChfFZ.gif",
        "https://66.media.tumblr.com/d743a5e5ecc65be5cb6ac8de7978fb22/tumblr_pfyit1ofSu1th206io1_500.gif",
        "https://i.imgur.com/LUypjw3.gif",
        "https://i.pinimg.com/originals/ec/b8/7f/ecb87fb2827a022884d5165046f6608a.gif",
        "https://thumbs.gfycat.com/ImpurePleasantArthropods-small.gif",
        ]

        embed = discord.Embed(title=f"{ctx.author.name} pats, {user.name}", description="pat pat", color=discord.Color.gold())
        embed.set_image(url=random.choice(patv))

        await ctx.send(embed=embed)

    @commands.command()
    async def lap(self, ctx,user:discord.Member = None):
        
        if user is None:
            await ctx.send("You need to give lap pillows. That's cute but mention someone")
            return
        
        if user==ctx.author:
            await ctx.send("That's a bro moment. But you cant lie on your own lap unless you broke your neck...")
            return   
        
        yastik = [
        "https://i.hizliresim.com/pgTnCN.gif",
        "https://media.tenor.com/images/6eb51ecba07ba236ab717ca1fa3a02a0/tenor.gif",
        "https://media.tenor.com/images/f6053a70c19ac74045aae1cfc9c85e78/tenor.gif",
        "https://cdn.awwni.me/t3m5.gif"
        ]

        embed = discord.Embed(title=f"{user.name} gets a cute lap pillow from {ctx.author.name}", description="That's so lovely!", color = ctx.author.color)
        embed.set_image(url=random.choice(yastik))

        await ctx.send(embed=embed)

    @commands.command()
    async def ara(self, ctx):
        
        arav = [
        "https://i.pinimg.com/originals/14/16/8e/14168e97f35efe70cbdb386122e1b5e9.gif",
        "https://i.pinimg.com/originals/11/90/66/119066a6751819f2d20e4760a2ad4277.gif",
        "https://64.media.tumblr.com/6f917421b530790905865539cb919dad/tumblr_p1o3qcsLqO1wmel88o3_500.gifv",
        "https://i.hizliresim.com/MQaeNF.gif",
        "https://media.tenor.com/images/7ea76f356b64ec0fbb47341e872f7ea2/tenor.gif",
        "https://64.media.tumblr.com/2086b091452d87e5b3322923b9bb2256/tumblr_px6l0gh5ZH1vip2zbo2_500.gifv",
        ]

        embed = discord.Embed(title=f"{ctx.author.name} ara ara's...", description="Kinda cute", color=discord.Color.red())
        embed.set_image(url=random.choice(arav))
        
        await ctx.send(embed=embed)

    @commands.command()
    async def kick(self, ctx,user:discord.Member = None): 

        if user is None:
            await ctx.send("You need to mention the person that you wanted to kick")
            return

        if user==ctx.author:
            await ctx.send("You can not kick yourself. It is not 1984")
            return
            
        embed = discord.Embed(title=f"{user.name} has been kicked", color=discord.Color.dark_red())
        embed.set_image(url="https://media.tenor.com/images/27f16871c55a3376fa4bfdd76ac2ab5c/tenor.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def bonk(self, ctx, user:discord.Member = None):
        if user is None:
            await ctx.send("Mantion someone for god's sake")
            return

        if user==ctx.author:
            await ctx.send("I wouldn't bonk myself")
            return

        bonkv = "https://media1.tenor.com/images/6493bee2be7ae168a5ef7a68cf751868/tenor.gif?itemid=17298755"

        embed = discord.Embed(title=f"{ctx.author.name} Bonks {user.name}", description="Should have hurt", color=discord.Color.red())
        embed.set_image(url=bonkv)
        
        await ctx.send(embed=embed)


def setup(commands):
    commands.add_cog(emCog(commands))
    print('Embed Commands are ready')
