import discord
from discord.ext import commands

intents = Intents.all()
client = commands.Bot(command_prefix = '!', intents = intents)

token = ''
if __name__ == '__main__':
client.run(token)