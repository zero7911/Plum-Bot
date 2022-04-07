import discord


def custom_help(bot):
    @bot.group(invoke_without_command=True)
    async def help(ctx):
        em = discord.Embed(title="List of commands", description="Here is the list of commands!\n"
                                                                 "For more info on a specific command,"
                                                                 " use **p help <command>**",
                           color=ctx.guild.me.color)
        em.add_field(name="Actions", value="`bite` `bonk` `cuddle` `hug` `kill` `kiss` "
                                           "`lick` `nom` `pat` `poke` `punch` `slap` `spank` "
                                           "`stare` `tickle`", inline=False)
        em.add_field(name="Reactions", value="`baka` `blush` `cry` `dance` `grin` `lewd` `pout` "
                                             "`shrug` `sleepy` `smug` `thinking` `triggered`",
                     inline=False)
        em.add_field(name="Social", value="`profile` `avatar`", inline=False)
        # em.add_field(name="Fun", value="8ball reverse")
        await ctx.send(embed=em)

    '''
        Social Commands Help Section
    '''
    @help.command()
    async def profile(ctx):
        em = discord.Embed(title="profile", description="Shows the profile of the mentioned user",
                           color=ctx.guild.me.color)
        em.add_field(name="How To Use", value="p profile <member>")
        await ctx.send(embed=em)

    @help.command()
    async def avatar(ctx):
        em = discord.Embed(title="avatar", description="Shows the avatar of the mentioned user",
                           color=ctx.guild.me.color)
        em.add_field(name="How To Use", value="p avatar <member>")
        await ctx.send(embed=em)

    '''
            Action Commands Help Section
    '''
    aliases_a = "bite bonk cuddle hug kill kiss lick nom pat poke punch slap spank stare tickle".split(" ")

    @help.command(aliases=aliases_a)
    async def _actions_(ctx):
        message = ctx.message.content
        for i in aliases_a:
            if i in message:
                message = i
                break

        titles = {
            'bite': f'Bites the mentioned user',

            'bonk': f'Bonk the mentioned user',

            'cuddle': f'Cuddles the mentioned user',

            'hug': f'Hugs the mentioned user',

            'kill': f'Kills the mentioned user',

            'kiss': f'Kisses the mentioned user',

            'lick': f'Licks the mentioned user',

            'nom': f'Noms the mentioned user',

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
        em.add_field(name="How To Use", value=f"p {message} <member>")
        await ctx.send(embed=em)

    '''
            Reaction Commands Help Section
    '''
    aliases_r = "baka blush cry dance grin lewd pout shrug sleepy smug thinking triggered".split(" ")

    @help.command(aliases=aliases_r)
    async def _reactions_(ctx):
        message = ctx.message.content
        for i in aliases_r:
            if i in message:
                message = i
                break

        titles = {
            'baka': f'User says {message}',

            'blush': f'User blushes',

            'cry': f'User cries',

            'dance': f'User dances',

            'grin': f'User grins',

            'lewd': f'User thinks that this is too {message}',

            'pout': f'User pouts',

            'shrug': f'User shrugs',

            'sleepy': f'User is getting {message}',

            'smug': f'User acts {message}',

            'thinking': f'User thinks',

            'triggered': f'User is {message}'
        }

        em = discord.Embed(title=message.capitalize(), description=titles[message],
                           color=ctx.guild.me.color)
        em.add_field(name="How To Use", value=f"p {message}")
        await ctx.send(embed=em)
