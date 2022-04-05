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
                                           "stare tickle", inline=False)
        em.add_field(name="Reactions", value="`blush` `cry` `dance` `grin` `lewd` `pout` "
                                             "`punch` `shrug` `smug` `sleepy` `thinking` `triggered`",
                     inline=False)
        em.add_field(name="Social", value="`profile` `avatar`", inline=False)
        # em.add_field(name="Fun", value="8ball reverse")
        await ctx.send(embed=em)

    @help.command()
    async def profile(ctx):
        em = discord.Embed(title="info", description="Shows information for the user", color=ctx.guild.me.color)
        em.add_field(name="How To Use", value="p profile <member>")
        await ctx.send(embed=em)

# class CustomHelp(discord.ext.commands.Cog, name='Help'):
#     def __init__(self, bot):
#         self.bot = bot
#
#     @discord.ext.commands.command(name="help")
#     async def help(self, ctx):
#         em = discord.Embed(title="List of commands", description="Here is the list of commands!\n",
#                                                                  # "For more info on a specific command,"
#                                                                  # " use p help <command>",
#                            color=ctx.author.color)
#         em.add_field(name="Actions", value="bonk, kiss, poke")
#         em.add_field(name="Social", value="info")
#         # em.add_field(name="Fun", value="8ball reverse")
#         await ctx.send(embed=em)
#
#     @discord.ext.commands.command(name='help info', aliases=["help info"])
#     async def info(self, ctx):
#         em = discord.Embed(title="info", description="Shows information for the user", color=ctx.author.color)
#         em.add_field(name="How To Use", value="p info <member>")
#         await ctx.send(embed=em)
