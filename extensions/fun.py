import discord 
from discord.ext import commands 
from dipytools import tools
import aiohttp


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    async def get_meme(self):
        async with aiohttp.ClientSession() as r:
            async with r.get("https://meme-api.herokuapp.com/gimme/memes") as web:
                content = await web.json()
                title = content['title']
                upvote = content['ups']
                img = content['url']
                author = content['author']

                embed = discord.Embed(title=title, description = author, colour = discord.Colour.red())
                embed.set_image(url=img)
                embed.set_footer(text=f'{upvote} votes!')
                return embed

    @commands.command()
    async def meme(self, ctx : commands.Context):
        embed = await self.get_meme()
        await ctx.send(embed=embed)


def setup(bot : commands.Bot):
    bot.add_cog(Fun(bot))