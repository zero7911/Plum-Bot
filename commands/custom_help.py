import discord
from discord.ext import commands


class CustomHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx, x=None):
        if x is not None:
            await ctx.send('I do not know that command?!')
        else:
            em = discord.Embed(title="List of commands",
                               description=f"Here is the list of commands!\nFor more info on a specific command,"
                                           f" use **{ctx.prefix}help <command name>**",
                               color=ctx.guild.me.color)
            em.add_field(name="Actions <Category>",
                         value="`bite` `bonk` `cuddle` `hug` `kill` `kiss` `lick` `pat` `poke` `punch` `slap` "
                               "`spank` `stare` `tickle`",
                         inline=False)
            em.add_field(name="Reactions <Category>",
                         value="`angry` `baka` `blush` `cry` `dance` `grin` `lewd` `pout` `shrug` `sleepy` `smug` "
                               "`thinking` `triggered`",
                         inline=False)
            em.add_field(name="Social <Category>", value="`profile` `avatar`", inline=False)
            em.add_field(name="AS Guides <Category>",
                         value="**basement <Sub Category>**\n"
                               "`b1` `b2` `b3` `b4` `b5` `b6` `b7` `b8` `b9`\n"
                               "**boss <Sub Category>**\n"
                               "`cali` `dasha` `dili` `drauga` `duroc` `faf` `ocy`\n"
                               "**items <Sub Category>**\n"
                               "`<Item Name>`\n"
                               "**tips <Sub Category>**\n"
                               "`armor` `aw` `newbie` `weapon`\n",
                         inline=False)
            await ctx.send(embed=em)

    '''
        Social Commands Help Section
    '''
    @help.command()
    async def profile(self, ctx):
        em = discord.Embed(title="profile", description="Shows the profile of the mentioned user",
                           color=ctx.guild.me.color)
        em.add_field(name="How To Use", value=f"{ctx.prefix}profile <member>")
        await ctx.send(embed=em)

    @help.command()
    async def avatar(self, ctx):
        em = discord.Embed(title="avatar", description="Shows the avatar of the mentioned user",
                           color=ctx.guild.me.color)
        em.add_field(name="How To Use", value=f"{ctx.prefix}avatar <member>")
        await ctx.send(embed=em)

    '''
            Action Commands Help Section
    '''
    @help.command(aliases="bite bonk cuddle hug kill kiss lick pat poke punch slap spank stare tickle".split(" "))
    async def _actions_(self, ctx):
        message = ctx.invoked_with
        titles = {
            'bite': f'Bites the mentioned user',

            'bonk': f'Bonk the mentioned user',

            'cuddle': f'Cuddles the mentioned user',

            'hug': f'Hugs the mentioned user',

            'kill': f'Kills the mentioned user',

            'kiss': f'Kisses the mentioned user',

            'lick': f'Licks the mentioned user',

            'pat': f'Pats the mentioned user',

            'poke': f'Pokes the mentioned user',

            'punch': f'Punches the mentioned user',

            'slap': f'Slaps the mentioned user',

            'spank': f'Spanks the mentioned user',

            'stare': f'Stares at the mentioned user',

            'tickle': f'Tickles the mentioned user'
        }

        em = discord.Embed(title=message.capitalize(), description=titles[message],
                           color=ctx.guild.me.color)
        em.add_field(name="How To Use", value=f"{ctx.prefix}{message} <member>")
        await ctx.send(embed=em)

    '''
            Reaction Commands Help Section
    '''
    @help.command(aliases="angry baka blush cry dance grin lewd pout shrug sleepy smug thinking triggered".split(" "))
    async def _reactions_(self, ctx):
        titles = {
            'angry': f'User gets angry',

            'baka': f'User says baka',

            'blush': f'User blushes',

            'cry': f'User cries',

            'dance': f'User dances',

            'grin': f'User grins',

            'lewd': f'User thinks that this is too lewd',

            'pout': f'User pouts',

            'shrug': f'User shrugs',

            'sleepy': f'User is getting sleepy',

            'smug': f'User acts smug',

            'thinking': f'User thinks',

            'triggered': f'User is triggered'
        }

        message = ctx.invoked_with
        em = discord.Embed(title=message.capitalize(), description=titles[message],
                           color=ctx.guild.me.color)
        em.add_field(name="How To Use", value=f"{ctx.prefix}{message}")
        await ctx.send(embed=em)

        '''
            AS Guides Help Section
        '''

    @help.command(aliases="basement boss items tips".split(" "))
    async def _guides_(self, ctx):
        titles = {
            'basement': f'Shows the basement floor guide',

            'boss': f'Shows the boss guide',

            'items': f'Shows information of the item',

            'tips': f'Shows tips about the various game stuff',
        }

        message = ctx.invoked_with
        em = discord.Embed(title=message.capitalize(), description=titles[message],
                           color=ctx.guild.me.color)
        if message == 'basement':
            em.add_field(name="Commands List",
                         value="`b1` `b2` `b3` `b4` `b5` `b6` `b7` `b8` `b9`",
                         inline=False)
            em.add_field(name="How To Use", value=f"{ctx.prefix}guide <command>")
        elif message == 'boss':
            em.add_field(name="Commands List",
                         value="`cali` `dili` `duroc` `ocy` `faf` `drauga` `dasha`",
                         inline=False)
            em.add_field(name="How To Use", value=f"{ctx.prefix}guide <command>")
        elif message == 'items':
            em.add_field(name="Commands List",
                         value="`<Item Name>`",
                         inline=False)
            em.add_field(name="How To Use", value=f"{ctx.prefix}find <Item Name>")
        elif message == 'tips':
            em.add_field(name="Commands List",
                         value="`armor` `aw` `newbie` `weapon`",
                         inline=False)
            em.add_field(name="How To Use", value=f"{ctx.prefix}guide <command>")
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(CustomHelp(bot))