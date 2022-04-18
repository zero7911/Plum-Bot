from discord.ext import commands


class Guides(commands.Cog, name='Guides'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="guide")
    async def _guides_(self, ctx, message=None):
        with open(f"./guides/{message}.txt", 'r') as f:
            guide = f.read(2000)
            if len(guide) >= 2000:
                x = guide.rfind('\n')
                f.seek(0)
                guide = f.read(x)
            await ctx.send(guide)
            if len(guide) >= 2000:
                guide = f.read(2000)
                await ctx.send(guide)


def setup(bot):
    bot.add_cog(Guides(bot))
