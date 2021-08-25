from os import name
import discord 
from discord.ext import commands 



class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def mute(self, ctx : commands.Context, member : discord.Member, *, reason : str):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if role == None:
            role = ctx.guild.create_role(name='Muted')
            for channel in ctx.guild.text_channels:
                perms = {
                    role : discord.PermissionOverwrite(send_messages=False)
                }
                await channel.edit(overwrites=perms)
        if role in member.roles:
            embed = discord.Embed(title="Bully", description = f"They're already muted!", colour = discord.Colour.random())
            await ctx.send(embed=embed)

        else:
            await member.add_roles(role)
            embed = discord.Embed(title="Muted them!", description = f"{member} has been muted!", colour = discord.Colour.random())
            await ctx.send(embed=embed)
            await member.send(f"You have been muted by **{ctx.author}** in **{ctx.guild.name}** for **{reason}**")


    @commands.command()
    async def unmute(self, ctx : commands.Context, member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if role == None:
            role = ctx.guild.create_role(name='Muted')
            for channel in ctx.guild.text_channels:
                perms = {
                    role : discord.PermissionOverwrite(send_messages=False)
                }
                await channel.edit(overwrites=perms)
        if role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(title='Unmuted!', description = f"{member} has now been unmuted!", colour = discord.Colour.random())
            await ctx.send(embed=embed)
            await member.send(f'You have been unmuted in **{ctx.guild}** by **{ctx.author}**')
        else:
            await ctx.send("They're not muted!")

def setup(bot : commands.Bot):
    bot.add_cog(Mod(bot))