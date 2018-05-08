import csv

# make sure script doesn't execute, put code into block
if __name__ == '__main__':

    # open 'soccer_players' csv file
    with open('soccer_players.csv') as csvfile:

        # put csv file into variable
        player_info = csv.DictReader(csvfile)

        # create three soccer teams
        raptors = []
        sharks = []
        dragons = []

        # create two lists of players (experienced and non-experienced)
        experienced = []
        non_experienced = []

        for players in player_info.reader:
            if players[2] == 'YES':
                experienced.append(players)
            elif players[2] == 'NO':
                non_experienced.append(players)

        # split players evenly into the three soccer teams (6 players, 3 experienced and 3 non-experienced)
        for x in range(0,3):
            raptors.append(experienced[x])
            raptors.append(non_experienced[x])

        for x in range(3,6):
            sharks.append(experienced[x])
            sharks.append(non_experienced[x])

        for x in range(6,9):
            dragons.append(experienced[x])
            dragons.append(non_experienced[x])

        players = ''
        for items in raptors:
            for i in range(len(items)):
                players += items[i]
                players += ', ' # separate player info by commas
            players += '\n'
        
        # create text file named teams.txt to holds all three teams and players
        with open('team.txt', 'a') as file:
            file.write('Raptors \n')
            file.write(players+'\n')

        players = ''
        for items in sharks:
            for i in range(len(items)):
                players += items[i]
                players += ', ' # separate player info by commas
            players += '\n'

        # create text file named teams.txt to holds all three teams and players
        with open('team.txt', 'a') as file:
            file.write('Sharks \n')
            file.write(players+'\n')

        players = ''
        for items in dragons:
            for i in range(len(items)):
                players += items[i]
                players += ', ' # separate player info by commas
            players += '\n'

        # create text file named teams.txt to holds all three teams and players
        with open('team.txt', 'a') as file:
            file.write('Dragons \n')
            file.write(players+'\n')


        
        



        


