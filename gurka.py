import random as rnd
class game:
    def __init__(self,players: list):
        self.players=players
def getPlayers():
    pass #WIP

print("""
╔════════════════════════════════════════════════╗
║ ######   ##     ## ########  ##    ##    ###   ║
║##    ##  ##     ## ##     ## ##   ##    ## ##  ║
║##        ##     ## ##     ## ##  ##    ##   ## ║
║##   #### ##     ## ########  #####    ##     ##║
║##    ##  ##     ## ##   ##   ##  ##   #########║
║##    ##  ##     ## ##    ##  ##   ##  ##     ##║
║ ######    #######  ##     ## ##    ## ##     ##║
╚════════════════════════════════════════════════╝
            S to start, X to exit""")
while True:
    choose=input("")
    if choose=="S":
        getPlayers()
    elif choose=="X":
        exit()
    else:
        print("ERROR: please choose from the list given")
        continue