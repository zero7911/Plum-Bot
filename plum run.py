import discord
from clients.custom_bot_client import CustomBotClient
from cogs.greetings import Greetings
from cogs.command_err_handler import CommandErrHandler
from cogs.social import Social
from cogs.actions import Actions
from cogs.reactions import Reactions
from cogs.guides import Guides
# from cogs.custom_help import CustomHelp
import cogs.custom_help as ch


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
    bot = CustomBotClient(command_prefix='p ', intents=intents)

    # removin default help command
    bot.remove_command('help')
    # calling cogs
    ch.custom_help(bot)
    bot.add_cog(Greetings(bot))
    bot.add_cog(Social(bot))
    bot.add_cog(Actions(bot))
    bot.add_cog(Reactions(bot))
    bot.add_cog(Guides(bot))
    # bot.add_cog(CustomHelp(bot))
    bot.add_cog(CommandErrHandler(bot))

    # bot initialized
    bot.run(token)


if __name__ == '__main__':
    main()
