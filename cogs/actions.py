import discord
from discord.ext import commands
import random


class Actions(commands.Cog, name='Actions'):
    images = {
        'bite': ['https://i.imgur.com/I7X0elG.gif', 'https://i.imgur.com/R4MnNFV.gif',
                 'https://i.imgur.com/bPwDUHm.gif', 'https://i.imgur.com/PlFkJLs.gif'],

        'bonk': ['https://imgur.com/fMKi7qt.gif', 'https://imgur.com/KVmzsHN.gif'],

        'cuddle': ['https://i.imgur.com/M9zsvwY.gif', 'https://i.imgur.com/TgdAOue.gif'],

        'hug': ['https://i.imgur.com/zgmiytH.gif', 'https://i.imgur.com/1XBLGY8.gif',
                'https://i.imgur.com/fY6IC7S.gif'],

        'kill': ['https://i.imgur.com/jngyAfB.gif', 'https://i.imgur.com/61J6yKl.gif'],

        'kiss': ['https://i.imgur.com/TK60yrE.gif', 'https://i.imgur.com/GZDBsQy.gif',
                 'https://i.imgur.com/yZPvWue.gif', 'https://i.imgur.com/seXxTtE.gif'],

        'lick': ['https://i.imgur.com/RsntR8D.gif', 'https://i.imgur.com/HM9batK.gif'],

        'pat': ['https://i.imgur.com/u9nW2LJ.gif', 'https://i.imgur.com/3DQpvRJ.gif',
                'https://i.imgur.com/KF8U2Ns.gif'],

        'poke': ['https://i.imgur.com/4SYxNdG.gif', 'https://i.imgur.com/OZGE0hw.gif',
                 'https://i.imgur.com/AEHLnYT.gif'],

        'punch': ['https://i.imgur.com/vih3fdY.gif'],

        'slap': ['https://i.imgur.com/6w9bIGY.gif', 'https://i.imgur.com/VnhDXNH.gif',
                 'https://i.imgur.com/Kg4U3dB.gif', 'https://i.imgur.com/kyfpHKA.gif'],

        'spank': ['https://i.imgur.com/M4jp80S.gif', 'https://i.imgur.com/lu4BQpY.gif',
                  'https://i.imgur.com/8Z6Dojf.gif'],

        'stare': ['https://i.imgur.com/OFTkCzQ.gif', 'https://i.imgur.com/FuPPIki.gif',
                  'https://i.imgur.com/lO39jMJ.gif'],

        'tickle': ['https://i.imgur.com/9KSwMw5.gif', 'https://i.imgur.com/gAkIsB4.gif',
                   'https://i.imgur.com/S6btHFi.gif']
    }

    @commands.command(aliases="bite bonk cuddle hug kill kiss lick pat poke punch slap spank stare tickle".split(" "))
    async def _actions_(self, ctx, member: discord.Member):
        titles = {
            'bite': f'{ctx.author.display_name} is biting {member.display_name}!',

            'bonk': f'{ctx.author.display_name} bonked {member.display_name}!',

            'cuddle': f'{ctx.author.display_name} is cuddling with {member.display_name}!',

            'hug': f'{ctx.author.display_name} hugged {member.display_name}!',

            'kill': f'{ctx.author.display_name} killed {member.display_name}!',

            'kiss': f'{ctx.author.display_name} kissed {member.display_name}!',

            'lick': f'{ctx.author.display_name} licked {member.display_name}!',

            'pat': f'{ctx.author.display_name} pats {member.display_name}!',

            'poke': f'{ctx.author.display_name} wants {member.display_name}\'s attention!',

            'punch': f'{ctx.author.display_name} punched {member.display_name}!',

            'slap': f'{ctx.author.display_name} slapped {member.display_name}!',

            'spank': f'{ctx.author.display_name} spanked {member.display_name}!',

            'stare': f'{ctx.author.display_name} is staring at {member.display_name}!',

            'tickle': f'{ctx.author.display_name} tickled {member.display_name}!'
        }

        if member.display_name == ctx.guild.me.display_name:
            rand_link = random.choice(['bonk', 'kill', 'punch', 'spank'])
            embed = discord.Embed(title=f"{ctx.me.display_name} {rand_link}ed {ctx.author.display_name}!",
                                  color=ctx.guild.me.color)
            rand_link = random.choice(self.images[rand_link])
            embed.set_image(url=rand_link)
            await ctx.send(random.choice(["You cannot do that to me!", "Do it to someone else!",
                                          "Keep dreaming!", 'Don\'t touch me!', 'Naughty kids need to be punished!']),
                           embed=embed)
        elif member.display_name == ctx.author.display_name:
            await ctx.send("Do it to someone else. Baka!")
        elif (member.id == 605027605539717130) and (ctx.author.id != 760391406837170198):
            await ctx.send("Stay away from my boss!")
        else:
            message = ctx.invoked_with
            embed = discord.Embed(title=f"{titles[message]}", color=ctx.guild.me.color)
            rand_link = random.choice(self.images[message])
            embed.set_image(url=rand_link)
            await ctx.send(embed=embed)
