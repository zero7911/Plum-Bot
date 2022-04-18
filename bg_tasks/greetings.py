from discord.ext import commands


class Greetings(commands.Cog, name='Greetings'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'A wild {member.mention} has appeared!')


def setup(bot):
    bot.add_cog(Greetings(bot))
