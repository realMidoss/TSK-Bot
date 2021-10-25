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

    @commands.command()
    async def sarıl(self, ctx,user:discord.Member = None):
        if user is None:
            await ctx.send("Havaya sarılamazsın")
            return
        if user==ctx.author:
            await ctx.send("Kendine sarılamazsın ki amk mal mısın sen?")
            return
        
        hugv = [
        "https://c.tenor.com/XPHDV3OLciAAAAAd/hug-handshake.gif",
        "https://64.media.tumblr.com/2992a0777126f8fcba14a37c79661050/e3fdebb154b42426-62/s2048x3072/678f2a2cf79fb2013709ab964746245b930d072c.gif",
        "https://c.tenor.com/jn1rJzwlUo4AAAAd/kiss-hug.gif",
        ]

        embed = discord.Embed(title=f"{ctx.author.name}, {user.name}'a sarılıyor.", description="Tamtlı!", color = ctx.author.color)
        embed.set_image(url=random.choice(hugv)) 

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
    async def kick(self, ctx,user:discord.Member = None): 

        if user is None:
            await ctx.send("Emret! Kimi istenmeyen kişi lan ediyoruz?")
            return

        if user==ctx.author:
            await ctx.send("Sizi Non Person Greta ilan edenin amına koyum komutanım.")
            return
            
        embed = discord.Embed(title=f"{user.name} ATILDIN!", color=discord.Color.dark_red())
        embed.set_image(url="https://media.tenor.com/images/27f16871c55a3376fa4bfdd76ac2ab5c/tenor.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, user:discord.Member = None):
        if user is None:
            await ctx.send("Birini mi etiketlesen? Hani müneccim falan değilim ben")
            return

        if user==ctx.author:
            await ctx.send("Kendine niye vuruyorsun?")
            return

        bonkv = "https://media1.tenor.com/images/6493bee2be7ae168a5ef7a68cf751868/tenor.gif?itemid=17298755"

        embed = discord.Embed(title=f"{ctx.author.name}, {user.name}'ya vurdu!", description="Azma sen de amcık", color=discord.Color.red())
        embed.set_image(url=bonkv)
        
        await ctx.send(embed=embed)

    @commands.command()
    async def çay(self, ctx):

        embed = discord.Embed(title=f"{ctx.author.name} made tea and grabs a glass of it. Anyone else wants?", description="tea is great", color=discord.Color.red())
        embed.set_image(url="https://i.pinimg.com/originals/fd/35/6b/fd356b3bf3fe3a3839efa654aaf52d61.gif")

        await ctx.send(embed=embed)
    
    @commands.command()
    async def f35(self, ctx):

        embed = discord.Embed(title=f"{ctx.author.name} f35lere bakıyor ve ağlıyor")
        embed.set_image(url="https://img.piri.net/mnresize/840/-/resim/imagecrop/2019/12/10/11/45/resized_b3d5f-f1d85093mansetc.jpg")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(5, 200, commands.BucketType.user)
    async def söv(self, ctx, user:discord.Member = None):

        kufurler = [
        "Senin ben yedi ceddini dere başında sikeyim",
        "Yedi ceddinin adet suyuna ekmek banayım ",
        "Senin gibilerin hak ettiği tek yer sikimin ucudur ama kendimi boka bulamak istemiyorum",
        "Weeb'in oğlu",
        "Sana açılan ilim irfan yuvalarının menteşelerini sikeyim",
        "Bacına telif hakkı koyayım",
        "Götüne kürek sokayım, çocuklara tahteravalli yapayım",
        "Ebeni kaçırıp ormana atayım, sırtına bal sürüp ayılara siktireyim",
        "Seni müjdeleyen doktoru sikiyim",
        "Halimize şükretmeliyiz. Senin gibi olmak da vardı",
        "Senin kârını sikerim",
        "Karının karnına Ermeni yarrağı saplayayım",
        "Senin amını yeni kategori açana dek sikeyim",
        "Ebeni uzaya göndereyim, yeni nesiller üretene dek uzaylılara siktireyim",
        "Seni ben götünden omuriliğine kadar yararım, orospunun döletinin müjdelediği seni",
        "Ebeni çarprazlayayım.",
        "Seni satın alır, karını sana kuma yaparım.",
        "Allah benim canımı alsın da senin ölmüşlerini sikeyim.",
        "Senin ben ölmüş etine tenezzül eden karıncanın izzeti, nefsini sikeyim.",
        "Sikilen maymun; ıhlamur ağacına çıkarmış, onun için mi ağaçtan inmiyorsun canım?",
        "Şam şeytanı kılıklı engerek orospusu seni...",
        "Yunan Anadolu'ya girse, bu pezevenk enişte diye boynuna sarılır.",
        "Bana bak! Aklının sulu yerini sikerim senin.",
        "Senin dalağını alır, açılan deliği sikerim.",
        "Seni bir sikerim, bir hafta bulanık sıçarsın.",
        "Senin bacağındaki kılı sikiyim.",
        "Yalancıyı sikseler, senden hiç çıkarmazlardı.",
        "O elini götüne sokarım, sürahi gibi gezersin."
        ]
        
        if user is None:
            await ctx.send("kime söveyim amk?")
            return
        
        if user==ctx.author:
            await ctx.send("Kendine saygın olsun biraz.")
            return
        
        if(user.bot):
            await ctx.send(f'{ctx.author.name}, Seni yoğurtlar, çatır çutur sikerim çocuk.')
            return

        await ctx.send(f'{user.name}, {random.choice(kufurler)}')

    @söv.error
    async def toss_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = "Bekle bakalım! \n Sonraki küfre: {:.2f}s".format(error.retry_after)
            
            embed=discord.Embed(title="Sal AMK", description=f"{msg}", color = ctx.author.color)    
            embed.set_thumbnail(url="https://www.pngkit.com/png/full/603-6030012_open-11-11-clock-png.png")
            await ctx.send(embed=embed)
        else:
            raise error


def setup(commands):
    commands.add_cog(emCog(commands))
    print('Embed Commands are ready')