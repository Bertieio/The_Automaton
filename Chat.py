#!/usr/bin/env python3

import re, cfg, socket, UtilSPD, TwitchAPI

CHAT_RE_MESSAGE = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")


def exit(message, user):
    if message == "!exit" and user == cfg.CHANNAME.lower():
        quit()



def sendMessage(s, message):
    s.send('PRIVMSG {} :{} \r\n'.format(cfg.CHAN, message).encode())
    chatLog(message, cfg.NICK)

def chatters(message):
    if message == "!chatters":
        chatters = TwitchAPI.getChatters(cfg.CHANNAME)
        print(str(chatters))

def chatLog(msg, user):
    chatLog = cfg.ChatLog
    TD = UtilSPD.formatedTDSB()
    message = "{} {}: {}".format(TD, user, msg)
    print(message)
    with open(chatLog, 'a') as cLog:
        cLog.write(message+"\n")


def chat():
    s = socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            msg = CHAT_RE_MESSAGE.sub("", response).strip()
            user = re.search(r"\w+", response).group(0)
            chatLog(msg, user)
            exit(msg, user)
            #chatters(msg)
            if msg.lower() == "!test":
                sendMessage(s, "Hello")
