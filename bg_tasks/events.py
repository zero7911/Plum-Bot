import discord
from discord.ext import commands


class Events(commands.Bot):
    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')
        await self.change_presence(activity=discord.Game('p help'))
        print(f'Connected Guilds{self.guilds}')
