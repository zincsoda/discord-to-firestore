import discord
import config
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
client = discord.Client()

# initializations 
cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
ref = db.collection('Quotes')
docs = ref.stream()
for doc in docs:
    main_doc = doc
    break
doc_ref = db.collection('Quotes').document(main_doc.id)

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
    message = '{0.content}'.format(message)
    #print(message)
    doc_ref.set({ 'quotes':message, })


client.run(config.house_bot_token)
