import os
import discord
import pymongo
from discord.ext import commands


class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.myclient = pymongo.MongoClient(os.environ.get("MONGODB_URI"))
        self.mydb = self.myclient["guild_db"]
        print(self.mydb)



#text_channels是TextChannel的列表一定要進行迴圈再呼叫參數
    @commands.command()
    async def joinchannel(self, ctx):
        for x in ctx.guild.text_channels:
            print(x.id)






def setup(bot):
    bot.add_cog(Welcome(bot))
