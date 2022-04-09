import discord
from discord.ext import commands
import random


class Reactions(commands.Cog, name='Reactions'):
    images = {
        'baka': ['https://imgur.com/8x792Sx.gif'],

        'blush': ['https://imgur.com/8x792Sx.gif'],

        'cry': ['https://imgur.com/8x792Sx.gif'],

        'dance': ['https://imgur.com/8x792Sx.gif'],

        'grin': ['https://imgur.com/8x792Sx.gif'],

        'lewd': ['https://imgur.com/8x792Sx.gif'],

        'pout': ['https://imgur.com/8x792Sx.gif'],

        'shrug': ['https://imgur.com/8x792Sx.gif'],

        'sleepy': ['https://imgur.com/8x792Sx.gif'],

        'smug': ['https://imgur.com/8x792Sx.gif'],

        'thinking': ['https://imgur.com/8x792Sx.gif'],

        'triggered': ['https://imgur.com/8x792Sx.gif']
    }

    @commands.command(aliases="baka blush cry dance grin lewd pout shrug sleepy smug thinking triggered".split(" "))
    async def _reactions_(self, ctx):
        message = ctx.invoked_with
        titles = {
            'baka': f'{ctx.author.display_name} is saying {message}',

            'blush': f'{ctx.author.display_name} is {message}ing',

            'cry': f'{ctx.author.display_name} is {message}ing',

            'dance': f'{ctx.author.display_name} is dancing',

            'grin': f'{ctx.author.display_name} is {message}ning',

            'lewd': f'{ctx.author.display_name} thinks that this is too {message}',

            'pout': f'{ctx.author.display_name} is {message}ing',

            'shrug': f'{ctx.author.display_name} {message}ged',

            'sleepy': f'{ctx.author.display_name} is getting {message}',

            'smug': f'{ctx.author.display_name} is acting {message}',

            'thinking': f'{ctx.author.display_name} is {message} something',

            'triggered': f'{ctx.author.display_name} is {message}'
        }
        embed = discord.Embed(title=f"{titles[message]}",
                              color=ctx.guild.me.color)
        rand_link = random.choice(self.images[message])
        embed.set_image(url=rand_link)
        await ctx.send(embed=embed)
