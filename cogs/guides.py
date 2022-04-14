from discord.ext import commands


class Guides(commands.Cog, name='Guides'):
    @commands.command(name="guide")
    async def _guides_(self, ctx, message=None):
        with open(f"{message}.txt", 'r') as f:
            guide = f.read(2000)
            if len(guide) >= 2000:
                x = guide.rfind('\n')
                f.seek(0)
                guide = f.read(x)
            await ctx.send(guide)
            while len(guide) > 0:
                guide = f.read(2000)
                await ctx.send(guide)
