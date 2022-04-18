import discord
from discord.ext import commands
import os
# from bg_tasks.events import Events
# from bg_tasks.greetings import Greetings
# from bg_tasks.error_handler import ErrorHandler
# from commands.social import Social
# from commands.actions import Actions
# from commands.reactions import Reactions
# from commands.guides import Guides
# from commands.custom_help import CustomHelp


from os import getenv
from dotenv import load_dotenv


def main():
    """
    main function
    :return:
    """
    load_dotenv()
    token = getenv('P_TOKEN')
    intents = discord.Intents.default()
    intents.members = True

    # bot initialize
    bot = commands.Bot(command_prefix="p", intents=intents)

    # removing default help command
    bot.remove_command('help')

    for i in ['commands', 'bg_tasks', 'utility']:
        for file in os.listdir(i):
            if file.endswith('.py'):
                bot.load_extension(f'{i}.{file[:-3]}')

    # bot initialized
    bot.run(token)


if __name__ == '__main__':
    main()
