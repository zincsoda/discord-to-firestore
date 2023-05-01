import discord
import config
from pyfiglet import Figlet
import os
from termcolor import colored

client = discord.Client()
font_name = 'rev'

@client.event
async def on_ready():
    os.system('clear')
    print('We have logged in as {0.user}'.format(client))
    print('Waiting for input ...')
    
@client.event
async def on_message(message):
    my_testing_channel = client.get_channel(972379757247340574)
    my_dev_channel = client.get_channel(972378842494824488)
    if message.author == client.user:
        return

    if message.channel != my_testing_channel:
        return
    os.system('clear')
    f = Figlet(font=font_name, width=220)
    message = '{0.content}'.format(message)
    rendered = f.renderText(message)
    colored_message = colored(rendered, 'blue')
    print("\n")
    print(colored_message)
    print("\n\n\n")
    # print('Message from {0.author}: {0.content}'.format(message))
    # await my_dev_channel.send(message.content)

client.run(config.house_bot_token)