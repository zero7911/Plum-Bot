import discord


class Guides(discord.ext.commands.Cog, name='Guides'):
    def __init__(self, bot):
        self.bot = bot

    aliases_ = "dili".split(" ")

    @discord.ext.commands.command(name="_guides_", aliases=aliases_)
    async def _guides_(self, ctx):
        titles = {
            'b9': f'Basement Floor 9 Guide',

            'dili': f'Dilitherio Super Guide',

            'duroc': f'Duroc Super Guide',

        }

        message = ctx.message.content
        for i in self.aliases_:
            if i in message:
                message = i
                break

        if message == 'dili':
            with open(f"{message}.txt") as f:
                guide = f.readlines()
                guide = ''.join(guide)
            with open(f"{message}2.txt") as f2:
                guide2 = f2.readlines()
                guide2 = ''.join(guide2)
            await ctx.send(f'{guide}')
            await ctx.send(f'{guide2}')
