import os
import discord
from discord.ext import commands
import tracemoepy

tracemoe = tracemoepy.tracemoe.TraceMoe()


def road_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = road_token()

client = commands.Bot(command_prefix='.', case_insensitive=True)
client.remove_command("help")


@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="Help", description="Use .help <command> for more information on a command.",
                          color=ctx.author.color)
    embed.add_field(name="Find Anime Sauce", value="``Sauce``")
    embed.add_field(name="\nFun", value="``ily, Hi, Bye, 8ball, kms,\n kiss, hug, pat, slap, punch ``")
    embed.add_field(name="\nBot", value="\n``ping``")
    await ctx.send(embed=embed)


@help.command()
async def sauce(ctx):
    embed = discord.Embed(title="Sauce", description="Use this command to find the source of the Anime! ",
                          color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".sauce *[insert anime image link here, gifs do not work]*\n"
                                             "You can use command *.reasons* to know the possible reasons on why the "
                                             "command is not working.")
    await ctx.send(embed=embed)


@help.command()
async def ily(ctx):
    embed = discord.Embed(title="I love you", description="Use this command to get an *I love you too* <mention>",
                          color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".ily")
    await ctx.send(embed=embed)


@help.command()
async def hi(ctx):
    embed = discord.Embed(title="Hi", description="Use this command to get a *Konnichiwa* <mention>",
                          color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".hi")
    await ctx.send(embed=embed)


@help.command()
async def bye(ctx):
    embed = discord.Embed(title="Bye", description="Use this command to get a *Sayonara* <mention>",
                          color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".bye")
    await ctx.send(embed=embed)


@help.command()
async def kms(ctx):
    embed = discord.Embed(title="Kill my self", description="Use this command to Kill yourself! with a gif",
                          color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".kms")
    await ctx.send(embed=embed)


@help.command("8ball")
async def _8ball(ctx):
    embed = discord.Embed(title="8Ball", description="Use this command and a yes or no question next to it,"
                                                     "and the bot will convey you the truth",
                          color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".8ball <yes or no question>")
    await ctx.send(embed=embed)


@help.command()
async def ping(ctx):
    embed = discord.Embed(title="Ping", description="Get bot ping.", color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".ping")
    await ctx.send(embed=embed)


@help.command()
async def kiss(ctx):
    embed = discord.Embed(title="Kiss", description="Kiss someone", color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".kiss <mention>")
    await ctx.send(embed=embed)


@help.command()
async def hug(ctx):
    embed = discord.Embed(title="Hug", description="Hug someone", color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".hug <mention>")
    await ctx.send(embed=embed)


@help.command()
async def pat(ctx):
    embed = discord.Embed(title="Pat", description="Pat someone", color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".Pat <mention>")
    await ctx.send(embed=embed)


@help.command()
async def punch(ctx):
    embed = discord.Embed(title="Punch", description="Punch someone", color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".punch <mention>")
    await ctx.send(embed=embed)


@help.command()
async def slap(ctx):
    embed = discord.Embed(title="Slap", description="Slap someone", color=ctx.author.color)
    embed.add_field(name="**Syntax**", value=".Slap <mention>")
    await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Hey! Please enter the required context. Type *.help* if you need more info on a command!")

    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send(
            "Hey! Looks like you did not use the command properly, Type *.help* for more info\n If using *.sauce* "
            "Either the image is too malformed, or the url provided was not valid.\n "
            "Remember: Gif urls will not work. You can use command *.reasons* to know the possible reasons.")

    elif isinstance(error, commands.CommandNotFound):
        print("")

    else:
        raise error


@client.command(aliases=["reason"])
async def reasons(ctx):
    await ctx.send("***Possible reasons are:***"
                   "```\n1. Your image is not an original anime screenshot: You may try to use SauceNAO and iqdb.org "
                   "which is best for searching anime artwork. "
                   "\n2. The anime has not been analyzed yet: New animes currently airing would be analyzed around 24 "
                   "hours after TV broadcast. Long-running animes / cartoons are excluded at this stage. See What "
                   "anime are indexed at the bottom of this page. "
                   "\n3. Your image is flipped: If your image comes from AMV / Anime Compilations, it's likely that "
                   "it's flipped horizontally. "
                   "\n4. Your image is of bad quality: The image search algorithm is designed for almost-exact match, "
                   "not similar match. It analyze the color layout of the image. So, when your image is not a full "
                   "un-cropped original 16:9 screenshot (i.e. cropped image), the search would likely fail.``` "
                   "\n```Color is an important factor for the correct search, if heavy tints and filters are applied "
                   "to the screenshot "
                   "(i.e. grayscale, contrast, saturation, brightness, sepia), too much information are lost. In this "
                   "case the search would also fail. "
                   "The Edge Histogram can solve this issue by ignoring colors and only search edges. But I am "
                   "running out of computing resource to support another image descriptor. "
                   "Image transform is also an important factor. If the image is not scaled without maintaining "
                   "original aspect ratios (i.e. elongated, flipped, rotated), the search would also fail. "
                   "Text occupied too much of the image. Large texts on the image would interfere the original image. "
                   "The system is not smart enough to ignore the text. "
                   "If your image has too little distinguish features (e.g. dark images or images with large plain "
                   "blocks of plain colors), the search would also fail. "
                   "Searching with a real photo (of an anime) definitely won't work.```")


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
