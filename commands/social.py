import discord
from discord.ext import commands


class Social(commands.Cog, name='Social'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="profile")
    async def profile(self, ctx, member: discord.Member):
        embed = discord.Embed(title=member.display_name, color=ctx.guild.me.color)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.display_name}")
        await ctx.send(embed=embed)

    @commands.command(name="avatar")
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(title=member.name, color=ctx.guild.me.color)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.display_name}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Social(bot))
