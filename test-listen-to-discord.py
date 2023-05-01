import discord
import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    my_testing_channel = client.get_channel(972379757247340574)
    my_dev_channel = client.get_channel(972378842494824488)
    if message.author == client.user:
        return

    if message.channel != my_testing_channel:
        return

    print('Message from {0.author}: {0.content}'.format(message))
    await my_dev_channel.send(message.content)

client.run(config.house_bot_token)