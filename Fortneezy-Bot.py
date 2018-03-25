import asyncio
import requests
from discord.ext.commands import Bot
from datetime import datetime


TOKEN = 'Client Token'
HEADERS = {'TRN-Api-Key': 'key'}

client = Bot(command_prefix="!")


async def pull_stats(user):
    """Pulls user's stats from tracker network"""
    user = user.title()
    platform = 'pc'
    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, user), headers=HEADERS)
    return r.json()


async def error_print(error, user):
    """Prints error when username is not found"""
    print('Error!\nDate: ', datetime.now())
    print("KeyError:", error)
    await  client.say("Username \"" + user + "\" not found, try again.")


@client.command()
async def solo(user: str):
    """Display Lifetime Solo Stats \ !solo 'username'"""
    player_data = await pull_stats(user)
    try:
        solo_L = player_data['stats']['p2']
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Lifetime Solo Stats==")
        await client.say("Matches Played: " + solo_L['matches']['value'] +
                         "  ||  Wins: " + solo_L['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((solo_L['top1']['valueInt'] /
                                                               solo_L['matches']['valueInt']) * 100) + "%")
        await client.say("Kills: " + solo_L['kills']['value'] +
                         "  ||  KDR: " + solo_L['kd']['value'] + "%")
    except KeyError as e:
        await error_print(e, user)


@client.command()
async def solo_season(user: str):
    """Display Current Season Solo Stats \ !solo 'username'"""
    player_data = await pull_stats(user)
    try:
        solo_s = player_data['stats']['curr_p2']
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Lifetime Solo Stats==")
        await client.say("Matches Played: " + solo_s['matches']['value'] +
                         "  ||  Wins: " + solo_s['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((solo_s['top1']['valueInt'] /
                                                               solo_s['matches'][
                                                                   'valueInt']) * 100) + "%")
        await client.say("Kills: " + solo_s['kills']['value'] +
                         "  ||  KDR: " + solo_s['kd']['value'] + "%")
    except KeyError as e:
        await error_print()


@client.command()
async def duo(user: str):
    """Display Lifetime Due Stats \ !duo 'username'"""
    player_data = await pull_stats(user)
    try:
        duo_lifetime = player_data['stats']['p10']
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Lifetime Duo Stats==")
        await client.say("Matches Played: " + duo_lifetime['matches']['value'] +
                         "  ||  Wins: " + duo_lifetime['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((duo_lifetime['top1']['valueInt'] /
                                                               duo_lifetime['matches'][
                                                                   'valueInt']) * 100) + "%")
        await client.say("Kills: " + duo_lifetime['kills']['value'] +
                         "  ||  KDR: " + duo_lifetime['kd']['value'] + "%")
    except KeyError as e:
        await error_print(e, user)


@client.command()
async def duo_season(user: str):
    """Display Current Season Due Stats \ !duo 'username'"""
    player_data = await pull_stats(user)
    try:
        duo_S = player_data['stats']['curr_p10']
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Lifetime Duo Stats==")
        await client.say("Matches Played: " + duo_S['matches']['value'] +
                         "  ||  Wins: " + duo_S['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f"
                         % ((duo_S['top1']['valueInt'] / duo_S['matches']['valueInt']) * 100) + "%")
        await client.say("Kills: " + duo_S['kills']['value'] +
                         "  ||  KDR: " + duo_S['kd']['value'] + "%")
    except KeyError as e:
        await error_print(e, user)


@client.command()
async def squad(user: str):
    """Display Lifetime Squad Stats \ !squad 'username'"""
    player_data = await pull_stats(user)
    try:
        squad_L = player_data['stats']['p9']
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Lifetime Squad Stats==")
        await client.say("Matches Played: " + squad_L['matches']['value'] +
                         "  ||  Wins: " + squad_L['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((squad_L['top1']['valueInt'] /
                                                               squad_L['matches'][
                                                                   'valueInt']) * 100) + "%")

        await client.say("Kills: " + squad_L['kills']['value'] +
                         "  ||  KDR: " + squad_L['kd']['value'] + "%")
    except KeyError as e:
        await error_print(e, user)


@client.command()
async def squad_season(user: str):
    """Display Current Squad Stats \ !squad 'username'"""
    player_data = await pull_stats(user)
    try:
        squad_S = player_data['stats']['curr_p9']
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Current Season Squad Stats==")
        await client.say("Matches Played: " + squad_S['matches']['value'] +
                         "  ||  Wins: " + squad_S['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((squad_S['top1']['valueInt'] /
                                                               squad_S['matches'][
                                                                   'valueInt']) * 100) + "%")

        await client.say("Kills: " + squad_S['kills']['value'] +
                         "  ||  KDR: " + squad_S['kd']['value'] + "%")
    except KeyError as e:
        await error_print(e, user)


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


