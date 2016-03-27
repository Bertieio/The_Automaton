import requests, time, dateutil.parser

def getMods(user):
    response = requests.get("https://tmi.twitch.tv/group/user/" + user + "/chatters").json()
    mods = response["chatters"]["moderators"]
    return mods


def online(user):
    response = requests.get("https://api.Twitch.tv/kraken/streams/" + user).json()
    if response["stream"] is not None:
        return True
    else:
        return False


def getGame(user):
    online = online(user)
    if online == True:
        game = getGameOnline(user)
    else:
        game = getGameOffline(user)
    return game


def getGameOnline(user):
    response = requests.get("https://api.twitch.tv/kraken/streams/" + user).json()
    if response["stream"] is not None:
        return response["stream"]["game"]


def getGameOffline(user):
    response = requests.get("https://api.twitch.tv/kraken/channels/" + user).json()
    if response["game"] is not None:
        return ["game"]


def getChatters(user):
    response = requests.get("https://tmi.twitch.tv/group/user/" + user + "/chatters").json()
    chatters = response["chatters"]["moderators"] + response["chatters"]["staff"] + response["chatters"]["admins"] + response["chatters"]["global_mods"] + response["chatters"]["viewers"]
    return chatters


def Uptime(user):
    response = requests.get("https://api.twitch.tv/kraken/streams/" + user).json()
    startTime = response["stream"]["created_at"]
    uptime = str(dateutil.parser.parse(startTime))
    compTime = int(time.time()) - (int(time.mktime(datetime.datetime.strptime(Uptime, '%Y-%m-%d %H:%M:%S+00:00').timetuple())))
    formedTime = str(time.strftime('%H:%M:%S'))
    return formedTime
