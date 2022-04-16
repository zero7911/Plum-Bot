import discord
from discord.ext import commands
import random


class Reactions(commands.Cog, name='Reactions'):
    images = {
        'angry': ['https://i.imgur.com/C6JrEC2.gif'],

        'baka': ['https://i.imgur.com/dE1JCK4.gif'],

        'blush': ['https://i.imgur.com/wetBY43.gif'],

        'cry': ['https://i.imgur.com/kWXw2Cs.gif'],

        'dance': ['https://i.imgur.com/HZ078eu.gif'],

        'grin': ['https://i.imgur.com/OLsDzl3.gif'],

        'lewd': ['https://i.imgur.com/MJmRcKg.gif'],

        'pout': ['https://i.imgur.com/jFJ2VDs.gif'],

        'shrug': ['https://i.imgur.com/Y1HyFeV.gif'],

        'sleepy': ['https://i.imgur.com/VtfBVA1.gif'],

        'smug': ['https://i.imgur.com/4mQnZhf.gif'],

        'thinking': ['https://i.imgur.com/30eA2fU.gif'],

        'triggered': ['https://i.imgur.com/tB5KqeC.gif']
    }

    @commands.command(aliases="angry baka blush cry dance grin lewd pout shrug sleepy smug thinking "
                              "triggered".split(" "))
    async def _reactions_(self, ctx):
        message = ctx.invoked_with
        titles = {
            'angry': f'{ctx.author.display_name} is getting {message}',

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
