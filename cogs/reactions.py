import discord
import random


class Reactions(discord.ext.commands.Cog, name='Reactions'):
    def __init__(self, bot):
        self.bot = bot

    images = {
        'baka': [
            'https://c.tenor.com/xHeSSmvJvQQAAAAC/vampire-kiss.gif',
            'https://c.tenor.com/roNlxBPyft4AAAAi/kiss-love.gif',
            'https://c.tenor.com/0uRmrUvyZFEAAAAM/vamp-vampire-bite.gif'
            'https://c.tenor.com/SCQI234MDZYAAAAM/iove-bite.gif'
            'https://c.tenor.com/N08gv10rlSEAAAAS/diabolik-lovers.gif'
        ],

        'blush': [
            'https://cdn.discordapp.com/attachments/581509910848864265/889613544553865236/bonk-anime.gif',
            'https://cdn.discordapp.com/attachments/581509910848864265/889613545023615016/psyduck-bonk.gif'
        ],

        'cry': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'dance': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'grin': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'lewd': [
            'https://cdn.weeb.sh/images/rJeB2aOP-.gif'
        ],

        'pout': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'shrug': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'sleepy': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'

        ],

        'smug': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'thinking': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'triggered': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ]
    }

    aliases_ = "baka blush cry dance grin lewd pout shrug sleepy smug thinking triggered".split(" ")

    @discord.ext.commands.command(name="_reactions_", aliases=aliases_)
    async def _reactions_(self, ctx):
        message = ctx.message.content
        for i in self.aliases_:
            if i in message:
                message = i
                break

        titles = {
            'baka': f'{ctx.author.name} is saying {message}',

            'blush': f'{ctx.author.name} is {message}ing',

            'cry': f'{ctx.author.name} is {message}ing',

            'dance': f'{ctx.author.name} is doing {message}',

            'grin': f'{ctx.author.name} is {message}ning',

            'lewd': f'{ctx.author.name} thinks that this is too {message}',

            'pout': f'{ctx.author.name} is {message}ing',

            'shrug': f'{ctx.author.name} {message}ged',

            'sleepy': f'{ctx.author.name} is getting {message}',

            'smug': f'{ctx.author.name} is acting {message}',

            'thinking': f'{ctx.author.name} is {message} something',

            'triggered': f'{ctx.author.name} is {message}'
        }

        embed = discord.Embed(title=f"{titles[message]}",
                              color=ctx.guild.me.color)
        rand_link = random.choice(self.images[message])
        # embed.set_image(url=rand_link)
        await ctx.send(embed=embed)
