import discord
from bg_tasks.events import Events
from bg_tasks.greetings import Greetings
from bg_tasks.error_handler import ErrorHandler
from cogs.social import Social
from cogs.actions import Actions
from cogs.reactions import Reactions
from cogs.guides import Guides
from cogs.custom_help import CustomHelp


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
    bot = Events(command_prefix="p ", intents=intents)

    # removing default help command
    bot.remove_command('help')

    # adding cogs
    bot.add_cog(Greetings(bot))
    bot.add_cog(Social(bot))
    bot.add_cog(Actions(bot))
    bot.add_cog(Reactions(bot))
    bot.add_cog(Guides(bot))
    bot.add_cog(CustomHelp(bot))
    bot.add_cog(ErrorHandler(bot))

    # bot initialized
    bot.run(token)


if __name__ == '__main__':
    main()
