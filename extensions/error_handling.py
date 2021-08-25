import discord 
from discord.ext import commands 



class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Please provide all the arguments!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You do not have the permissions to the run this command!')
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'This command is on cooldown! Please try again in {int(error.retry_after)} seconds!')


def setup(bot : commands.Bot):
    bot.add_cog(Error(bot))