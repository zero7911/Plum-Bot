import discord


def custom_help(bot):
    @bot.group(invoke_without_command=True)
    async def help(ctx):
        em = discord.Embed(title="List of commands", description="Here is the list of commands!\n"
                                                                 "For more info on a specific command,"
                                                                 " use **p help <command>**",
                           color=ctx.guild.me.color)
        em.add_field(name="Actions", value="`bite` `bonk` `cuddle` `hug` `kill` `kiss` "
                                           "`lick` `nom` `poke` `pat` `slap` `spank` "
                                           "`stare` `tickle`", inline=False)
        em.add_field(name="Reactions", value="`baka` `blush` `cry` `dance` `grin` `lewd` `pout` "
                                             "`punch` `shrug` `sleepy` `smug` `thinking` `triggered`",
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



    '''
            Reaction Commands Help Section
    '''