import discord,pymongo
from discord.ext import commands


class Emoji(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def thumb(self, ctx):

        accept_decline = await ctx.send("Test")
        await accept_decline.add_reaction('👍')
        await accept_decline.add_reaction('👎')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except self.bot.asyncio.TimeoutError:
            await ctx.send('👎')
        else:
            await ctx.send('👍')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction)
        print(user)

def setup(bot):
    bot.add_cog(Emoji(bot))