import re, cfg, socket

CHAT_RE_MESSAGE = re.compile(r"^:\w+!\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
