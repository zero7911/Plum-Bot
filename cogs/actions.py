import discord
import random


class Actions(discord.ext.commands.Cog, name='Actions'):
    def __init__(self, bot):
        self.bot = bot

    bonk_images = [
        'https://cdn.discordapp.com/attachments/581509910848864265/889613544553865236/bonk-anime.gif',
        'https://cdn.discordapp.com/attachments/581509910848864265/889613545023615016/psyduck-bonk.gif']

    poke_images = [
        'https://data.yuibot.app/reactions/poke/ansiodjas.gif',
        'https://data.yuibot.app/reactions/poke/jsidoajd.gif']

    kiss_images = ['https://cdn.weeb.sh/images/rJeB2aOP-.gif']

    @discord.ext.commands.command(name="bonk")
    async def bonk(self, ctx, member: discord.Member):
        embed = discord.Embed(description=f"{ctx.author.name} bonked {member.name}", color=ctx.guild.me.color)
        rand_link = random.choice(self.bonk_images)
        embed.set_image(url=rand_link)
        await ctx.send(f"{member.mention}", embed=embed)

    @discord.ext.commands.command(name="kiss")
    async def kiss(self, ctx, member: discord.Member):
        embed = discord.Embed(description=f"{ctx.author.name} kissed {member.name}", color=ctx.guild.me.color)
        rand_link = random.choice(self.kiss_images)
        embed.set_image(url=rand_link)
        await ctx.send(f"{member.mention}", embed=embed)

    @discord.ext.commands.command(name="poke")
    async def poke(self, ctx, member: discord.Member):
        embed = discord.Embed(description=f"{ctx.author.name} poked {member.name}!Poke Poke!",
                              color=ctx.guild.me.color)
        rand_link = random.choice(self.poke_images)
        embed.set_image(url=rand_link)
        await ctx.send(f"{member.mention}", embed=embed)
