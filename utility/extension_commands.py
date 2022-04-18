from discord.ext import commands


class Extensions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, extension):
        if ctx.author.id == 605027605539717130:
            self.bot.load_extension(f'commands.{extension}')
            await ctx.send(f"{extension} loaded")
        else:
            await ctx.send(f"Permission Denied.")

    @commands.command()
    async def unload(self, ctx, extension):
        if ctx.author.id == 605027605539717130:
            self.bot.unload_extension(f'commands.{extension}')
            await ctx.send(f"{extension} unloaded")
        else:
            await ctx.send(f"Permission Denied.")


def setup(bot):
    bot.add_cog(Extensions(bot))
