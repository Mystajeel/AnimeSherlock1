import discord
from discord.ext import commands
import random


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['latency', 'p'])
    async def ping(self, ctx):
        await ctx.send(f'Your Ping is: {round(self.client.latency * 1000)}ms')

    @commands.command(aliases=['hello', 'Konnichiwa'])
    async def hi(self, ctx):
        await ctx.send(f"Konnichiwa! {ctx.message.author.mention}")

    @commands.command(aliases=['sayonara'])
    async def bye(self, ctx):
        await ctx.send(f"Sayonara~! {ctx.message.author.mention}")

    @commands.command()
    async def ily(self, ctx):
        await ctx.send(f"I love you too {ctx.message.author.mention}")

    @commands.command("8ball")
    async def _8ball(self, ctx, *, question):
        responses = [
            "Certainly my dude!",
            "Guess it's true bro.",
            "No doubt my dude!",
            "Definitely my guy!",
            "Ehh, you can rely on it.",
            "As much as I see it, sure",
            "lol probably.",
            "Damn looks like it's true huh.",
            "Yeah.",
            "My ~~spider~~ detective sense tells me it's true.",
            "Lole idk.",
            "Ayo, can you ask me later dude.",
            "Don't think I'd wanna tell you now.",
            "Lunch time, come back later.",
            "Come on bro, try again but spice it up a bit you know!",
            "I wouldn't trust it fam.",
            "Yeah no.",
            "Yeah def no.",
            "Damn looks like it's not true huh.",
            "idk about that my dude."]

        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(aliases=["kms", 'Die'])
    async def suicide(self, ctx):
        responsess = ['https://imgur.com/3WMLsd1.gif',
                      'https://imgur.com/7Srvk5e.gif',
                      'https://imgur.com/CiJTRvM.gif',
                      'https://imgur.com/umw1GsG.gif',
                      'https://imgur.com/e1xc1jp.gif',
                      'https://imgur.com/quCZ4ja.gif',
                      'https://imgur.com/QZDPlWR.gif',
                      'https://imgur.com/ZSFKnU5.gif',
                      'https://imgur.com/JeRyiIL.gif',
                      'https://imgur.com/1PmYW5T.gif']

        colors = [discord.Colour.blue(), discord.Colour.blurple(), discord.Colour.dark_gold(),
                  discord.Colour.dark_blue(),
                  discord.Colour.dark_magenta(), discord.Colour.dark_red()]

        embed = discord.Embed(title=f"{ctx.message.author.display_name} **Has killed themselves**",
                              color=random.choice(colors))
        embed.set_image(url=f'{random.choice(responsess)}')
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, kisser):
        responses = ["https://imgur.com/O1uLViq.gif",
                     "https://imgur.com/2BWoXx8.gif",
                     "https://imgur.com/MsPkSLD.gif",
                     "https://imgur.com/XOYXcP6.gif",
                     "https://imgur.com/MhDsJyd.gif",
                     "https://imgur.com/iOxVW1l.gif",
                     "https://imgur.com/I6XKUvl.gif",
                     "https://imgur.com/hX0esyD.gif",
                     "https://imgur.com/Dt7FpWz.gif",
                     "https://imgur.com/OPBlqcG.gif",
                     "https://imgur.com/xq5zOFV.gif",
                     "https://imgur.com/T9cUMKn.gif",
                     "https://imgur.com/Nl1nYHI.gif",
                     "https://imgur.com/8CQ4jWn.gif",
                     "https://imgur.com/EyjgDCE.gif",
                     "https://imgur.com/cMC6kfg.gif",
                     "https://imgur.com/0Cs88br.gif"]
        mention = ctx.message.mentions[0].display_name

        colors = [discord.Colour.blue(), discord.Colour.blurple(), discord.Colour.dark_gold(),
                  discord.Colour.dark_blue(),
                  discord.Colour.dark_magenta(), discord.Colour.dark_red()]
        embed = discord.Embed(title=f'{ctx.message.author.display_name} kisses {mention}',
                              color=random.choice(colors))
        embed.set_image(url=f'{random.choice(responses)}')
        responsess = ['https://imgur.com/2WgWwe7.gif',
                      'https://imgur.com/req1ZSZ.gif',
                      'https://imgur.com/hNNBxMF.gif',
                      'https://imgur.com/Ukq47qB.gif',
                      'https://imgur.com/95P0fzG.gif',
                      'https://imgur.com/Oal4bL3.gif',
                      'https://imgur.com/rOiXxgw.gif',
                      'https://imgur.com/Yb287eo.gif',
                      'https://imgur.com/UxL1yxG.gif',
                      'https://imgur.com/RuDGmlv.gif',
                      'https://imgur.com/xeslhf3.gif']
        embid = discord.Embed(title=f'{ctx.message.author.display_name} kisses themself and dies alone',
                              color=random.choice(colors))
        embid.set_image(url=f'{random.choice(responsess)}')

        if mention == ctx.message.author.display_name:
            await ctx.send(embed=embid)

        elif mention is not None:
            await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, kisser):
        responses = ["https://imgur.com/BH63dWV.gif",
                     "https://imgur.com/ClrMXTH.gif",
                     "https://imgur.com/DdvW2e6.gif",
                     "https://imgur.com/2qQhwzp.gif",
                     "https://imgur.com/4AwmwW9.gif",
                     "https://imgur.com/4DWNQw5.gif",
                     "https://imgur.com/UV1J1qb.gif",
                     "https://imgur.com/cosrMO6.gif",
                     "https://imgur.com/e6dEjET.gif",
                     "https://imgur.com/Am386Ow.gif",
                     "https://imgur.com/NAlcb6h.gif",
                     "https://imgur.com/agDG282.gif",
                     "https://imgur.com/IoLx5Nw.gif",
                     "https://imgur.com/E9Ez1mp.gif",
                     "https://imgur.com/D7qZHMO.gif",
                     "https://imgur.com/GjtdSWW.gif",
                     "https://imgur.com/NiBwfwh.gif"]
        mention = ctx.message.mentions[0].display_name

        colors = [discord.Colour.blue(), discord.Colour.blurple(), discord.Colour.dark_gold(),
                  discord.Colour.dark_blue(),
                  discord.Colour.dark_magenta(), discord.Colour.dark_red()]
        embed = discord.Embed(title=f'{ctx.message.author.display_name} Hugs {mention}',
                              color=random.choice(colors))
        embed.set_image(url=f'{random.choice(responses)}')
        responsess = ['https://imgur.com/2WgWwe7.gif',
                      'https://imgur.com/req1ZSZ.gif',
                      'https://imgur.com/hNNBxMF.gif',
                      'https://imgur.com/Ukq47qB.gif',
                      'https://imgur.com/95P0fzG.gif',
                      'https://imgur.com/Oal4bL3.gif',
                      'https://imgur.com/rOiXxgw.gif',
                      'https://imgur.com/Yb287eo.gif',
                      'https://imgur.com/UxL1yxG.gif',
                      'https://imgur.com/RuDGmlv.gif',
                      'https://imgur.com/xeslhf3.gif']
        embid = discord.Embed(title=f'{ctx.message.author.display_name} Hugs themself and dies alone',
                              color=random.choice(colors))
        embid.set_image(url=f'{random.choice(responsess)}')

        if mention == ctx.message.author.display_name:
            await ctx.send(embed=embid)

        elif mention is not None:
            await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, kisser):
        responses = ["https://imgur.com/sW3tg2q.gif",
                     "https://imgur.com/YczqTE2.gif",
                     "https://imgur.com/1lvCWlj.gif",
                     "https://imgur.com/i0Rr3w9.gif",
                     "https://imgur.com/wMkS6bM.gif",
                     "https://imgur.com/l4PICut.gif",
                     "https://imgur.com/FyeulbA.gif",
                     "https://imgur.com/2OrhT6U.gif",
                     "https://imgur.com/xQwIqgH.gif",
                     "https://imgur.com/R2Oaa09.gif",
                     "https://imgur.com/w2tYC6F.gif",
                     "https://imgur.com/w9d3ooQ.gif",
                     "https://imgur.com/p80HxFb.gif",
                     "https://imgur.com/m3Fm7XE.gif",
                     "https://imgur.com/Ihv8kRx.gif",
                     "https://imgur.com/UowzVEu.gif",
                     "https://imgur.com/G2L24hk.gif"]
        mention = ctx.message.mentions[0].display_name

        colors = [discord.Colour.blue(), discord.Colour.blurple(), discord.Colour.dark_gold(),
                  discord.Colour.dark_blue(),
                  discord.Colour.dark_magenta(), discord.Colour.dark_red()]
        embed = discord.Embed(title=f'{ctx.message.author.display_name} Pats {mention}',
                              color=random.choice(colors))
        embed.set_image(url=f'{random.choice(responses)}')
        responsess = [
            'https://imgur.com/1aLRWVB.gif'
        ]
        embid = discord.Embed(
            title=f'{ctx.message.author.display_name} Pats themself *What a weirdo*',
            color=random.choice(colors))
        embid.set_image(url=f'{random.choice(responsess)}')

        if mention == ctx.message.author.display_name:
            await ctx.send(embed=embid)

        elif mention is not None:
            await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, kisser):
        responses = ["https://imgur.com/oOQbWdL.gif",
                     "https://imgur.com/ug2X4xn.gif",
                     "https://imgur.com/76lteRC.gif",
                     "https://imgur.com/vsR6hFu.gif",
                     "https://imgur.com/yHSnH5R.gif",
                     "https://imgur.com/1f8On3A.gif",
                     "https://imgur.com/MnxOCpU.gif",
                     "https://imgur.com/5GaK54Z.gif",
                     "https://imgur.com/vUoBkIw.gif",
                     "https://imgur.com/5g8znp7.gif",
                     "https://imgur.com/sZuK97m.gif",
                     "https://imgur.com/2iLzACL.gif",
                     "https://imgur.com/5NzdYT1.gif",
                     "https://imgur.com/xp82jEJ.gif",
                     "https://imgur.com/rRcB7qy.gif",
                     "https://imgur.com/7AGJxnz.gif"]
        mention = ctx.message.mentions[0].display_name

        colors = [discord.Colour.blue(), discord.Colour.blurple(), discord.Colour.dark_gold(),
                  discord.Colour.dark_blue(),
                  discord.Colour.dark_magenta(), discord.Colour.dark_red()]
        embed = discord.Embed(title=f'{ctx.message.author.display_name} Slaps {mention}',
                              color=random.choice(colors))
        embed.set_image(url=f'{random.choice(responses)}')
        responsess = ['https://imgur.com/pIP7B9H.gif']
        embid = discord.Embed(title=f'{ctx.message.author.display_name} Slaps themself and cries',
                              color=random.choice(colors))
        embid.set_image(url=f'{random.choice(responsess)}')

        if mention == ctx.message.author.display_name:
            await ctx.send(embed=embid)

        elif mention is not None:
            await ctx.send(embed=embed)

    @commands.command()
    async def punch(self, ctx, kisser):
        responses = ["https://imgur.com/FfvFEaf.gif",
                     "https://i.imgur.com/M72hAHE.gif",
                     "https://imgur.com/FAn5EXU.gif",
                     "https://imgur.com/1sZ389f.gif",
                     "https://imgur.com/XfGNpJ3,gif",
                     "https://imgur.com/vdKQXIi.gif",
                     "https://imgur.com/d3mVhdj.gif",
                     "https://imgur.com/ahvg2cN.gif",
                     "https://imgur.com/lTASfgw.gif",
                     "https://imgur.com/C2YvpFIgif",
                     "https://imgur.com/mB8Yr6mgif",
                     "https://imgur.com/IIudoQ0gif",
                     "https://imgur.com/k1whopwgif",
                     "https://imgur.com/4aW8fdqgif",
                     "https://imgur.com/oA2HvNAgif",
                     "https://imgur.com/mWuy3LYgif",
                     "https://imgur.com/XDVajzigif"]
        mention = ctx.message.mentions[0].display_name

        colors = [discord.Colour.blue(), discord.Colour.blurple(), discord.Colour.dark_gold(),
                  discord.Colour.dark_blue(),
                  discord.Colour.dark_magenta(), discord.Colour.dark_red()]
        embed = discord.Embed(title=f'{ctx.message.author.display_name} Punches {mention}',
                              color=random.choice(colors))
        embed.set_image(url=f'{random.choice(responses)}')
        responsess = ["https://imgur.com/kn0FL1ugif"]

        embid = discord.Embed(title=f'{ctx.message.author.display_name} punches themself in the nuts...',
                              color=random.choice(colors))
        embid.set_image(url=f'{random.choice(responsess)}')

        if mention == ctx.message.author.display_name:
            await ctx.send(embed=embid)

        elif mention is not None:
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
