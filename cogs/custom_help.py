import discord
from discord.ext import commands


class CustomHelp(commands.Cog):
    @commands.group(invoke_without_command=True)
    async def help(self, ctx, x=None):
        if x is not None:
            await ctx.send('I do not know that command?!')
        else:
            em = discord.Embed(title="List of commands",
                               description="Here is the list of commands!\nFor more info on a specific command,"
                                           " use **p help <command>**",
                               color=ctx.guild.me.color)
            em.add_field(name="Actions",
                         value="`bite` `bonk` `cuddle` `hug` `kill` `kiss` `lick` `pat` `poke` `punch` `slap` "
                               "`spank` `stare` `tickle`",
                         inline=False)
            em.add_field(name="Reactions",
                         value="`baka` `blush` `cry` `dance` `grin` `lewd` `pout` `shrug` `sleepy` `smug` `thinking`"
                               " `triggered`",
                         inline=False)
            em.add_field(name="Social", value="`profile` `avatar`", inline=False)
            # em.add_field(name="Fun", value="8ball reverse")
            await ctx.send(embed=em)

    '''
        Social Commands Help Section
    '''
    @help.command()
    async def profile(self, ctx):
        em = discord.Embed(title="profile", description="Shows the profile of the mentioned user",
                           color=ctx.guild.me.color)
        em.add_field(name="How To Use", value=f"{ctx.prefix} profile <member>")
        await ctx.send(embed=em)

    @help.command()
    async def avatar(self, ctx):
        em = discord.Embed(title="avatar", description="Shows the avatar of the mentioned user",
                           color=ctx.guild.me.color)
        em.add_field(name="How To Use", value=f"{ctx.prefix} avatar <member>")
        await ctx.send(embed=em)

    '''
            Action Commands Help Section
    '''
    @help.command(aliases="bite bonk cuddle hug kill kiss lick pat poke punch slap spank stare tickle".split(" "))
    async def _actions_(self, ctx):
        message = ctx.invoked_with
        print(message)
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
        em.add_field(name="How To Use", value=f"{ctx.prefix} {message} <member>")
        await ctx.send(embed=em)

    '''
            Reaction Commands Help Section
    '''
    @help.command(aliases="baka blush cry dance grin lewd pout shrug sleepy smug thinking triggered".split(" "))
    async def _reactions_(self, ctx):
        titles = {
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
        em.add_field(name="How To Use", value=f"{ctx.prefix} {message}")
        await ctx.send(embed=em)
