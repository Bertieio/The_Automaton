import cfg, requests, time

def getMods():
    response = requests.get("https://tmi.twitch.tv/group/user/" + cfg.CHANNAME + "/chatters").json()
    mods = response["chatters"]["moderators"]
    return mods


def getGameOnline():
    response = requests.get("https://api.twitch.tv/kraken/streams/" + cfg.CHANNAME).json()
    if response["stream"] is not None:
        return response["stream"]["game"]
    else:
        return getGameOffline();


def getGameOffline():
        response = requests.get("https://api.twitch.tv/kraken/channels/" + cfg.CHANNAME).json()
        if response["game"] is not None:
            return ["game"]

def Uptime
