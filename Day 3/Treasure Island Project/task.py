from importlib.metadata import pass_none

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
while True:
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    first_choice = input("choose your fate. each hand contains an item. "
                         "choose the hand with food to continue. left or right hand? ")
    if first_choice.lower() == "left" or first_choice == "LEFT HAND":
        second_choice = input("you are lucky. you chose the hand that has the potato"
                              "\nnow you can continue the adventyah. "
                              "there is now a fork on the road. choose your direction, left or right? ")
        if second_choice.lower() == "right":
           third_choice = input("wow. okay. you're lucky. now there is a more obvious fork in the road. "
                                "would you go into the forest or go by the seaside? choose forest or sea ")
           if third_choice.lower() == "sea" or third_choice == "seaside":
               fourth_choice = input("do you like to swim that much? you arent swimming in this game. "
                                     "next question: there is now a castle and you see the entrance. "
                                     "do you knock on the door or not? Y/N ")
               if fourth_choice.lower() == "y":
                   replay = input("you chose to knock on the door. a human with manners. "
                                  "the owners of the castle decide to let you live and give you treasure. "
                                  "you beat the game, congratulations. \nwould you like to play again? Y/N ")
                   if replay.lower() == "y":
                       print("hellye")
                   else:
                       break
               else:
                   replay = input("the owners of the castle decided to seal your fate because you lack manners. "
                                  "well, game over. \nwould you like to play again? Y/N ")
                   if replay.lower() == "y":
                       print("awyea")
                   else:
                       break
           else:
               replay = input("you chose the dim forest. you got eaten by wild animals. game over. "
                              "\nwould you like to play again? Y/N ")
               if replay.lower() == "y":
                   print("kk")
               else:
                   break
        else:
            replay = input("sorry you didn't make it to the cut, you chose left so now you have to leave the game world. game over :( \nwould you like to play again? Y/N ")
            if replay.lower() == "y":
                print("okay")
            else:
                break
    else:
        replay = input("sorry you didn't make it to the cut, the hand you chose contains rocks, so you have no food to survive henceforth. game over :(\nwould you like to play again? Y/N ")
        if replay.lower() == "y":
            print("let's goooo")
        else:
            break

