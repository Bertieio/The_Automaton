import TwitchAPI, UtilSPD, cfg
'''
INSERT
INTO ViewersXP(  `Name` ,  `CurrentXP` ,  `LifetimeXP` )
VALUES (
 'steampunk_devil', 15, 15
) ON DUPLICATE
KEY UPDATE `CurrentXP` = `CurrentXP` + 15, `LifetimeXP` = `LifetimeXP` + 15
'''
def currency():
    if TwitchAPI.online(cfg.CHANNAME) == True:
        sleep(cfg.TimeBetweenPaymentsOnline)
