import asyncio
import requests
import logging
import io
import configparser
from discord.ext.commands import Bot
from datetime import datetime

client = Bot(command_prefix="!")
# Load configuration file with API keys
Config = configparser.ConfigParser()
Config.read('tokens.ini')
# Bot Token
bot_token = Config.get('Tokens', 'bottoken')
TOKEN = bot_token
# Tracker Network
TRN_key = Config.get('Tokens', 'trn-api-key')
HEADERS = {'TRN-Api-Key': TRN_key}


async def pull_stats(user):
    """Pulls user's stats from tracker network"""
    user = user.title()
    platform = 'pc'
    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, user), headers=HEADERS)
    return r.json()


async def error_print(user):
    """Prints error when username is not found"""
    time = str(datetime.now())
    logging.error('Username Not Found or no stats for current season, Date: ' + str(time[:-7]))
    await  client.say("Username \"" + user + "\" not found, try again.")


@client.command()
async def solo(user: str):
    """Display Lifetime Solo Stats \ !solo 'username'"""
    player_data = await pull_stats(user)
    try:
        solo_L = player_data['stats']['p2']
        stats = io.StringIO()
        stats.write("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        stats.write("\n==Lifetime Solo Stats==")
        stats.write("\nMatches Played: " + solo_L['matches']['value'] +
                    "  ||  Wins: " + solo_L['top1']['value'] +
                    "  ||  Win Percentage: " + "%.2f" % ((solo_L['top1']['valueInt'] /
                                                          solo_L['matches']['valueInt']) * 100) + "%")
        stats.write("\nKills: " + solo_L['kills']['value'] +
                    "  ||  KDR: " + solo_L['kd']['value'] + "%")
        await client.say(stats.getvalue())
    except KeyError:
        await error_print(user)


@client.command()
async def solo_season(user: str):
    """Display Current Season Solo Stats \ !solo_season 'username'"""
    player_data = await pull_stats(user)
    try:
        solo_s = player_data['stats']['curr_p2']
        stats = io.StringIO()
        stats.write("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        stats.write("\n==Current Season Solo Stats==")
        stats.write("\nMatches Played: " + solo_s['matches']['value'] +
                    "  ||  Wins: " + solo_s['top1']['value'] +
                    "  ||  Win Percentage: " + "%.2f" % ((solo_s['top1']['valueInt'] /
                                                          solo_s['matches']['valueInt']) * 100) + "%")
        stats.write("\nKills: " + solo_s['kills']['value'] +
                    "  ||  KDR: " + solo_s['kd']['value'] + "%")
        await client.say(stats.getvalue())
    except KeyError:
        await error_print(user)


@client.command()
async def duo(user: str):
    """Display Lifetime Due Stats \ !duo 'username'"""
    player_data = await pull_stats(user)
    try:
        duo_lifetime = player_data['stats']['p10']
        stats = io.StringIO()
        stats.write("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        stats.write("\n==Lifetime Duo Stats==")
        stats.write("\nMatches Played: " + duo_lifetime['matches']['value'] +
                    "  ||  Wins: " + duo_lifetime['top1']['value'] +
                    "  ||  Win Percentage: " + "%.2f" % ((duo_lifetime['top1']['valueInt'] /
                                                          duo_lifetime['matches']['valueInt']) * 100) + "%")
        stats.write("\nKills: " + duo_lifetime['kills']['value'] +
                    "  ||  KDR: " + duo_lifetime['kd']['value'] + "%")
        await client.say(stats.getvalue())
    except KeyError:
        await error_print(user)


@client.command()
async def duo_season(user: str):
    """Display Current Season Due Stats \ !duo_season 'username'"""
    player_data = await pull_stats(user)
    try:
        duo_S = player_data['stats']['curr_p10']
        stats = io.StringIO()
        stats.write("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        stats.write("\n==Current Season Duo Stats==")
        stats.write("\nMatches Played: " + duo_S['matches']['value'] +
                    "  ||  Wins: " + duo_S['top1']['value'] +
                    "  ||  Win Percentage: " + "%.2f" % ((duo_S['top1']['valueInt'] /
                                                          duo_S['matches']['valueInt']) * 100) + "%")
        stats.write("\nKills: " + duo_S['kills']['value'] +
                    "  ||  KDR: " + duo_S['kd']['value'] + "%")
        await client.say(stats.getvalue())
    except KeyError:
        await error_print(user)


@client.command()
async def squad(user: str):
    """Display Lifetime Squad Stats \ !squad 'username'"""
    player_data = await pull_stats(user)
    try:
        squad_L = player_data['stats']['p9']
        stats = io.StringIO()
        stats.write("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        stats.write("\n==Lifetime Squad Stats==")
        stats.write("\nMatches Played: " + squad_L['matches']['value'] +
                    "  ||  Wins: " + squad_L['top1']['value'] +
                    "  ||  Win Percentage: " + "%.2f" % ((squad_L['top1']['valueInt'] /
                                                          squad_L['matches']['valueInt']) * 100) + "%")

        stats.write("\nKills: " + squad_L['kills']['value'] +
                    "  ||  KDR: " + squad_L['kd']['value'] + "%")
        await client.say(stats.getvalue())
    except KeyError:
        await error_print(user)


@client.command()
async def squad_season(user: str):
    """Display Current Squad Stats \ !squad_season 'username'"""
    player_data = await pull_stats(user)
    try:
        squad_S = player_data['stats']['curr_p9']
        stats = io.StringIO()
        stats.write("\nAccount: " + user + "  Platform: " + player_data['platformNameLong'])
        stats.write("\n==Current Season Squad Stats==")
        stats.write("\nMatches Played: " + squad_S['matches']['value'] +
                    "  ||  Wins: " + squad_S['top1']['value'] +
                    "  ||  Win Percentage: " + "%.2f" % ((squad_S['top1']['valueInt'] /
                                                          squad_S['matches']['valueInt']) * 100) + "%")

        stats.write("\nKills: " + squad_S['kills']['value'] +
                    "  ||  KDR: " + squad_S['kd']['value'] + "%")
        await client.say(stats.getvalue())
    except KeyError:
        await error_print(user)


@client.event
async def on_ready():
    await client.change_presence()
    print("Logged in as " + client.user.name)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
