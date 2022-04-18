import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} has connected to Discord!')
        await self.bot.change_presence(activity=discord.Game('p help'))
        print(f'Connected Guilds{self.bot.guilds}')

    # @commands.Cog.listener()
    # async def on_guild_join(self, server):
    #     """
    #     TO DO:
    #     store guild id
    #     store prefix
    #     store guides
    #     store member info
    #     :return:
    #     """
    #     pass


def setup(bot):
    bot.add_cog(Events(bot))
