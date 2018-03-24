import asyncio
import requests
from discord.ext.commands import Bot
from datetime import datetime


TOKEN = 'Client Token'
HEADERS = {'TRN-Api-Key': 'key'}

client = Bot(command_prefix="!")


@client.command()
async def solo(user: str):
    """Display Lifetime Solo Stats \ !solo 'username'"""
    user = user.title()
    platform = 'pc'

    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, user), headers=HEADERS)
    player_data = r.json()
    try:
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Lifetime Solo Stats==")
        await client.say("Matches Played: " + player_data['stats']['p2']['matches']['value'] +
                         "  ||  Wins: " + player_data['stats']['p2']['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((player_data['stats']['p2']['top1']['valueInt'] /
                                                               player_data['stats']['p2']['matches'][
                                                                   'valueInt']) * 100) + "%")
        await client.say("Kills: " + player_data['stats']['p2']['kills']['value'] +
                         "  ||  KDR: " + player_data['stats']['p2']['kd']['value'] + "%")
    except KeyError as e:
        print('Error!\nDate: ', datetime.now())
        print(e)
        await  client.say("Username \"" + user + "\" not found, try again.")


@client.command()
async def solo_season(user: str):
    """Display Current Season Solo Stats \ !solo 'username'"""
    user = user.title()
    platform = 'pc'

    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, user), headers=HEADERS)
    player_data = r.json()
    try:
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Lifetime Solo Stats==")
        await client.say("Matches Played: " + player_data['stats']['curr_p2']['matches']['value'] +
                         "  ||  Wins: " + player_data['stats']['curr_p2']['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((player_data['stats']['curr_p2']['top1']['valueInt'] /
                                                               player_data['stats']['curr_p2']['matches'][
                                                                   'valueInt']) * 100) + "%")
        await client.say("Kills: " + player_data['stats']['curr_p2']['kills']['value'] +
                         "  ||  KDR: " + player_data['stats']['curr_p2']['kd']['value'] + "%")
    except KeyError as e:
        print('Error!\nDate: ', datetime.now())
        print(e)
        await  client.say("Username \"" + user + "\" not found, try again.")

@client.command()
async def duo(user: str):
    """Display Lifetime Due Stats \ !duo 'username'"""
    user = user.title()
    platform = 'pc'

    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, user), headers=HEADERS)
    player_data = r.json()
    try:
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Lifetime Duo Stats==")
        await client.say("Matches Played: " + player_data['stats']['p10']['matches']['value'] +
                         "  ||  Wins: " + player_data['stats']['p10']['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((player_data['stats']['p10']['top1']['valueInt'] /
                                                               player_data['stats']['p10']['matches'][
                                                                   'valueInt']) * 100) + "%")
        await client.say("Kills: " + player_data['stats']['p10']['kills']['value'] +
                         "  ||  KDR: " + player_data['stats']['p10']['kd']['value'] + "%")
    except KeyError as e:
        print('Error!\nDate: ', datetime.now())
        print(e)
        await  client.say("Username \"" + user + "\" not found, try again.")


@client.command()
async def duo_season(user: str):
    """Display Current Season Due Stats \ !duo 'username'"""
    user = user.title()
    platform = 'pc'

    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, user), headers=HEADERS)
    player_data = r.json()
    try:
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Lifetime Duo Stats==")
        await client.say("Matches Played: " + player_data['stats']['curr_p10']['matches']['value'] +
                         "  ||  Wins: " + player_data['stats']['curr_p10']['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((player_data['stats']['curr_p10']['top1']['valueInt'] /
                                                               player_data['stats']['curr_p10']['matches'][
                                                                   'valueInt']) * 100) + "%")
        await client.say("Kills: " + player_data['stats']['curr_p10']['kills']['value'] +
                         "  ||  KDR: " + player_data['stats']['curr_p10']['kd']['value'] + "%")
    except KeyError as e:
        print('Error!\nDate: ', datetime.now())
        print(e)
        await  client.say("Username \"" + user + "\" not found, try again.")

@client.command()
async def squad(user: str):
    """Display Lifetime Squad Stats \ !squad 'username'"""
    user = user.title()
    platform = 'pc'

    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, user), headers=HEADERS)
    player_data = r.json()
    try:
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Lifetime Squad Stats==")
        await client.say("Matches Played: " + player_data['stats']['p9']['matches']['value'] +
                         "  ||  Wins: " + player_data['stats']['p9']['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((player_data['stats']['p9']['top1']['valueInt'] /
                                                               player_data['stats']['p9']['matches'][
                                                                   'valueInt']) * 100) + "%")

        await client.say("Kills: " + player_data['stats']['p9']['kills']['value'] +
                         "  ||  KDR: " + player_data['stats']['p9']['kd']['value'] + "%")
    except KeyError as e:
        print('Error!\nDate: ', datetime.now())
        print(e)
        await  client.say("Username \"" + user + "\" not found, try again.")


@client.command()
async def squad_season(user: str):
    """Display Current Squad Stats \ !squad 'username'"""
    user = user.title()
    platform = 'pc'

    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, user), headers=HEADERS)
    player_data = r.json()
    try:
        await client.say("Account: " + user + "  Platform: " + player_data['platformNameLong'])
        await client.say("==Current Season Squad Stats==")
        await client.say("Matches Played: " + player_data['stats']['curr_p9']['matches']['value'] +
                         "  ||  Wins: " + player_data['stats']['curr_p9']['top1']['value'] +
                         "  ||  Win Percentage: " + "%.2f" % ((player_data['stats']['curr_p9']['top1']['valueInt'] /
                                                               player_data['stats']['curr_p9']['matches'][
                                                                   'valueInt']) * 100) + "%")

        await client.say("Kills: " + player_data['stats']['curr_p9']['kills']['value'] +
                         "  ||  KDR: " + player_data['stats']['curr_p9']['kd']['value'] + "%")
    except KeyError as e:
        print('Error!\nDate: ', datetime.now())
        print(e)
        await  client.say("Username \"" + user + "\" not found, try again.")


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


