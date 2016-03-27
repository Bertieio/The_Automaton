import cfg, requests, time, dateutil.parser

def getMods():
    response = requests.get("https://tmi.twitch.tv/group/user/" + cfg.CHANNAME + "/chatters").json()
    mods = response["chatters"]["moderators"]
    return mods


def online():
    response = requests.get("https://api.Twitch.tv/kraken/streams/" + cfg.CHANNAME).json()
    if response["stream"] is not None:
        return True
    else:
        return False


def getGame():
    online = online()
    if online == True:
        game = getGameOnline()
    else:
        game = getGameOffline()
    return game


def getGameOnline():
    response = requests.get("https://api.twitch.tv/kraken/streams/" + cfg.CHANNAME).json()
    if response["stream"] is not None:
        return response["stream"]["game"]


def getGameOffline():
        response = requests.get("https://api.twitch.tv/kraken/channels/" + cfg.CHANNAME).json()
        if response["game"] is not None:
            return ["game"]


def Uptime():
    response = requests.get("https://api.twitch.tv/kraken/streams/" + cfg.CHANNAME).json()
    startTime = response["stream"]["created_at"]
    uptime = str(dateutil.parser.parse(startTime))
    compTime = int(time.time()) - (int(time.mktime(datetime.datetime.strptime(Uptime, '%Y-%m-%d %H:%M:%S+00:00').timetuple())))
    formedTime = str(time.strftime('%H:%M:%S'))
    return formedTime
