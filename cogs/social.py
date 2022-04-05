import discord


class Social(discord.ext.commands.Cog, name='Social'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="profile")
    async def profile(self, ctx, member: discord.Member):
        embed = discord.Embed(title=member.name, color=ctx.guild.me.color)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @discord.ext.commands.command(name="avatar")
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(title=member.name, color=ctx.guild.me.color)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
