import discord
import random


class Actions(discord.ext.commands.Cog, name='Actions'):
    def __init__(self, bot):
        self.bot = bot

    images = {
        'bite': [
            'https://c.tenor.com/xHeSSmvJvQQAAAAC/vampire-kiss.gif',
            'https://c.tenor.com/roNlxBPyft4AAAAi/kiss-love.gif',
            'https://c.tenor.com/0uRmrUvyZFEAAAAM/vamp-vampire-bite.gif'
            'https://c.tenor.com/SCQI234MDZYAAAAM/iove-bite.gif'
            'https://c.tenor.com/N08gv10rlSEAAAAS/diabolik-lovers.gif'
        ],

        'bonk': [
            'https://cdn.discordapp.com/attachments/581509910848864265/889613544553865236/bonk-anime.gif',
            'https://cdn.discordapp.com/attachments/581509910848864265/889613545023615016/psyduck-bonk.gif'
        ],

        'cuddle': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'hug': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'kill': [
            'https://imgur.com/jngyAfB.gif'
        ],

        'kiss': [
            'https://cdn.weeb.sh/images/rJeB2aOP-.gif'
        ],

        'lick': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'nom': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'pat': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'poke': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'

        ],

        'punch': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'

        ],

        'slap': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'spank': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'stare': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ],

        'tickle': [
            'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
            'https://data.yuibot.app/reactions/poke/jsidoajd.gif'
        ]
    }

    aliases_ = "bite bonk cuddle hug kill kiss lick nom pat poke punch slap spank stare tickle".split(" ")

    @discord.ext.commands.command(name="_actions_", aliases=aliases_)
    async def _actions_(self, ctx, member: discord.Member):
        titles = {
            'bite': f'{ctx.author.name} is biting {member.name}! Hope the teeth are alright!',

            'bonk': f'{ctx.author.name} bonked {member.name}! Can I do it too?',

            'cuddle': f'{ctx.author.name} is cuddling with {member.name}! Lets not disturb them',

            'hug': f'{ctx.author.name} hugged {member.name}! I want a hug too',

            'kill': f'{ctx.author.name} killed {member.name}! No Mercy!',

            'kiss': f'{ctx.author.name} kissed {member.name}! Go get a room, you lovebirds!',

            'lick': f'{ctx.author.name} licked {member.name}! Make sure to take a bath later',

            'nom': f'{ctx.author.name} noms {member.name}! Yummie!',

            'pat': f'{ctx.author.name} pats {member.name}! There,there',

            'poke': f'{ctx.author.name} wants {member.name}\'s attention!',

            'punch': f'{ctx.author.name} punched {member.name}! That must have hurt',

            'slap': f'{ctx.author.name} slapped {member.name}! You deserved it maybe?',

            'spank': f'{ctx.author.name} spanked {member.name}! Naughty',

            'stare': f'{ctx.author.name} is staring at {member.name}! Not in a bad way, right?',

            'tickle': f'{ctx.author.name} tickled {member.name}! Seems fun'
        }

        if member.name == ctx.guild.me.name:
            embed = discord.Embed(title=f"{ctx.me.name} bonked {ctx.author.name}!", color=ctx.guild.me.color)
            rand_link = random.choice(self.images['bonk'])
            embed.set_image(url=rand_link)
            await ctx.send(random.choice(["You cannot do that to me!", "Do it to someone else!",
                                          "Keep dreaming!", 'Fuck off!', 'Naughty kids need to be punished!']),
                           embed=embed)
        else:
            message = ctx.message.content
            for i in self.aliases_:
                if i in message:
                    message = i
                    break

            embed = discord.Embed(title=f"{titles[message]}", color=ctx.guild.me.color)
            # rand_link = random.choice(self.images[message])
            # embed.set_image(url=rand_link)
            await ctx.send(embed=embed)
