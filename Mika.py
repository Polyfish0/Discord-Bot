from discord import Game
from discord.ext.commands import Bot
import time
import configparser
import os

TOKEN = 'NDE4NTEzODcwNTM0MjEzNjM1.DvkTYQ.kMo7yw9aWc8noPWXPJnQPMD_bAQ - Not valid anymore'

BOT_PREFIX = '!'

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Super Smash Bros Ultimate"))
    print("Logged in as " + client.user.name)

#@client.event
#async def on_message(message):
#    if message.author.name != "Deutscher Kaiser":
#        if message.author.name == "Mika":

@client.command()
async def compile():
    await client.say("Ich kann sachen Compelieren...")
    time.sleep(5)
    await client.say("Bald")

def startup():
    config = configparser.ConfigParser()
    if not os.path.exists("config.ini"):
        create_conf(configparser=config, bool=False)
    else:
        config.read("config.ini")
        if config.has_section('bot'):
            if config.has_option('bot', 'token'):
                if config.has_option('bot', 'prefix'):
                    bot_prefix = str(config.get('bot', 'prefix'))
                    token = str(config.get('bot', 'token'))
                else:
                    create_conf(configparser=config, bool=True)
            else:
                create_conf(configparser=config, bool=True)
        else:
            create_conf(configparser=config, bool=True)

def create_conf(configparser, bool):
    if bool == False:
        configparser["bot"] = {'prefix': '!', 'token': '{AddBotTokenHere}'}
        configparser.write(open('config.ini', 'w'))
    else:
        local_prefix = configparser.get('bot', 'prefix')
        local_token = configparser.get('bot', 'token')
        configparser["bot"] = {'prefix': local_prefix, 'token': local_token}
        configparser.write(open('config.ini', 'w'))

startup()
#client.run(TOKEN)
