import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


player_choice_index = int(input("Let's play Rock Paper Scissors..."
      "choose your hand, 0-rock, 1-paper, 2-scissors! "
      "\nType the number \n"))

#print(choices)
#int_choice = int(player_choice_index)
#your_choice = choices[player_choice_index]
#print("your hand: " + your_choice)

random_choice_enemy_index = random.randint(0, 2)
#random_choice_enemy = choices[random_choice_enemy_index]
choices = [rock, paper, scissors]
print(f"Enemy chose: {random_choice_enemy_index} {choices[random_choice_enemy_index]}")
print(f"You chose: {player_choice_index} {choices[player_choice_index]}")

#compare the choices' indices, 2>1, 1>0, 0>2
if player_choice_index > 2:
    print("\nplease choose rock, paper, or scissors!")
elif ((player_choice_index == 2 and random_choice_enemy_index == 0) or
        (player_choice_index == 1 and random_choice_enemy_index == 2) or
        (player_choice_index == 0 and random_choice_enemy_index == 1)):
    print("You lose!")
elif ((player_choice_index == 2 and random_choice_enemy_index == 1) or
      (player_choice_index == 1 and random_choice_enemy_index == 0) or
      (player_choice_index == 0 and random_choice_enemy_index == 2)):
    print("You win!")
elif player_choice_index == random_choice_enemy_index:
    print("It's a tie!")




