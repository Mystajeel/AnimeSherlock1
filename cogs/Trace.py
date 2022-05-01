import discord
import random
from discord.ext import commands
import requests
from urllib.parse import quote
import tracemoepy

tracemoe = tracemoepy.tracemoe.TraceMoe()


class Sauce(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game(
            'Use .sauce to find the sauce! Use .help for a list of commands!'))
        print('bot is alive')
        print(f'Currently at {len(self.client.guilds)} servers!')
        print('Servers connected to:')
        print('')
        for server in self.client.guilds:
            print(server.name)

    @commands.command(aliases=['T', 'sauce', 's'])
    async def trace(self, ctx, *, url):


        res = tracemoe.search(url, is_url=True ).docs[0]


        thumbnail = "https://api.trace.moe/thumbnail.php?anilist_id={}&file={}&t={}&token={}".format(res.anilist_id,
                                                                                                 quote(res.filename),
                                                                                                 res.at, res.tokenthumb)
        colors = [discord.Colour.blue(), discord.Colour.blurple(), discord.Colour.dark_gold(),
                  discord.Colour.dark_blue(),
                  discord.Colour.dark_magenta(), discord.Colour.dark_red()]

        embed = discord.Embed(
            title="Anime: {} \nSimilarity: {}%\nSource:".format(res.title_english, int(res.similarity * 100)),
            color=random.choice(colors))

        embed.set_image(url=thumbnail)

        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Sauce(client))
