'''
Simulating a nightmare I had.
'''
from random import randint, random

def mode():
    easy = {"Regret Points":-1, "Enemy Probability": 0.25, "Number Of Rooms": 10, "Luck": 0.75}
    nightmare = {"Regret Points": 5, "Enemy Probability": 0.75, "Number Of Rooms": 20, "Luck": 0.25}
    sandbox = {}
    answer = "In my restless dreams, I see that town. Silent Hill."
    while answer not in (1,2,3):
        answer = int(input("Choose the game mode:\n1 - Easy\n2 - Nightmare\n3 - Player's Choice\nI choose: "))
        if answer == 1:
            way = easy
        elif answer == 2:
            way = nightmare
        elif answer == 3:
            Regret_Points = int(input("How many 'Regret Points'? "))
            Enemy_Prob = float(input("What's the 'Enemy Probability' (0 - 100%)? "))/100
            Number_of_Doors = int(input("How many rooms to pass by? "))
            Luck = float(input("How lucky is your character (0 - 100%)? "))/100
            way = dict(zip(["Regret Points", "Enemy Probability", "Number Of Rooms", "Luck"], [Regret_Points, Enemy_Prob, Number_of_Doors, Luck]))
            
        else:
            print("It ain't a option.") 
    print()       
    return way

def doors_system(rooms, enemy_prob):
    #The following will be true:
    #'_' represents a empty room, '*' represents a room with a enemy inside.
    site = ["S"]
    for i in range(rooms):
        room = []
        for d in range(3):
            if random() <= enemy_prob:
                room.append("*")
            else:
                room.append("_")
        site.append(room)
    return site

def the_escapist(room_position, luck):
    #just a bunch of messages to be displayed
    despair_message = ["You are running out of options. The room behind is also blocked.\n", "There isn't much left to do. You are trapped here.\n", 
                       "A hard problem requires a hard solution.\n", "This can't be the way you are dying.\n"]
    celebrate_message = ["Maybe you should order a pizza to celebrate it.\n", "That's your lucky day.\n", "You can't count on that forever...\n",
                         "For once, you were faster than that thing.\n"]
    print(despair_message[randint(0,3)])
    answer = input("Do you want to try to escape from this one (y/n)? ").lower()
    if answer[0] == "y":
        if random() <= luck:
            print(celebrate_message[randint(0,3)])
            luck *= 0.97
            return room_position, luck
        else:
            print("You have been caught.\n")
            return "Dead", luck
    else:
        print("You should at least have tried...\n")
        return "Dead", luck
    
def game_system(site, regret_points, luck):
    realtime_position = 0
    room_position = 0
    answer_list = []
    while realtime_position != len(site):
        answer = int(input("Which door do you want to choose (1,2,3)? ")) - 1
        if answer not in (0,1,2):
            answer = randint(0,2)
            print(f"You didn't give a good answer, so we chose {answer + 1} for you.\n")
        answer_list.append(answer)
        realtime_position = answer
        room_position += 1
        #if the player enter a empty room.
        if site[room_position][realtime_position] == "_":
            print("The room is empty, you are entering.\n")
        #if the player enter a room with a enemy inside and...
        elif site[room_position][realtime_position] == "*":
            site[room_position][realtime_position] = "D"
            print("There is a enemy inside. Things are getting weird here.\n")
            #the room behind him is occupied by another enemy.
            if len(answer_list) > 1:
                if site[room_position][answer_list[-2]] == "D" or site[room_position][answer_list[-2]] == "*":
                    room_position, luck = the_escapist(room_position, luck)
                    if room_position == "Dead":
                        return "Dead"
                #the room behind him is empty and...
                elif site[room_position][answer_list[-2]] == "_":
                    #the player has regret points
                    if regret_points != 0:
                        print("Maybe, it's a good idea to get back, but you can test your luck...\n")
                        answer = int(input("What do you want to do?\n1 - Get back\n2 - Try to pass by him\n3 - Surrender to the enemy\nI choose: "))
                        if answer == 1:
                            print("There is no shame in being alive.\n")
                            room_position -= 1
                            regret_points -= 1
                        elif answer == 2:
                            if random() <= luck:
                                print("I think you are alive.\n")
                                room_position += 1
                            else:
                                print("You have been caught.\n")
                                return "Dead"
                    #the player has no regret points
                    elif regret_points == 0:
                        room_position, luck = the_escapist(room_position, luck)
                        if room_position == "Dead":
                            return "Dead"
            else:
                room_position, luck = the_escapist(room_position, luck)
                if room_position == "Dead":
                    return "Dead"
        #if the player try to enter a room that he already knows that there is a enemy.
        elif site[room_position][realtime_position] == "D":
            print("Are you insane? Don't try it again. The enemy still there.\n")
            room_position -= 1
        if room_position == len(site) - 1:
            print("Finally, the last room.\n")
            print("I think you are alive. You are free to go.")
            return "Free"
        else:
            print(f"There still some rooms to be. You are at the {room_position}/{len(site)-1} room.")

def main():
    way = mode()
    info = doors_system(way["Number Of Rooms"], way["Enemy Probability"])
    game_result = game_system(info, way["Regret Points"], way["Luck"])
    if game_result == "Free":
        print("Well done. You can follow your dreams now.")
    elif game_result == "Dead":
        print("The darkness of the afterlife is all that awaits you now. May you find more peace in that world than you found in this one.")
main()
