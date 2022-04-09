from discord.ext import commands


class Guides(commands.Cog, name='Guides'):
    @commands.command(aliases="dili".split())
    async def _guides_(self, ctx):
        # titles = {
        #     'b9': f'Basement Floor 9 Guide',
        #
        #     'dili': f'Dilitherio Super Guide',
        #
        #     'duroc': f'Duroc Super Guide',
        #
        # }

        message = ctx.invoked_with
        if message == 'dili':
            with open(f"guides\{message}.txt") as f:
                guide = f.readlines()
                guide = ''.join(guide)
            with open(f"guides\{message}2.txt") as f2:
                guide2 = f2.readlines()
                guide2 = ''.join(guide2)
            await ctx.send(f'{guide}')
            await ctx.send(f'{guide2}')
