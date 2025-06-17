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

import random
player_choice_index = input("Let's play Rock Paper Scissors..."
      "choose your hand, 0-rock, 1-paper, 2-scissors! "
      "\nType the number ")
choices = [rock, paper, scissors]
print(choices)
int_choice = int(player_choice_index)
your_choice = choices[int_choice]
print("your hand: " + your_choice)

random_choice_enemy_index = random.randint(0, 2)
random_choice_enemy = choices[random_choice_enemy_index]
print("enemy hand: " + random_choice_enemy)

#compare the choices' indices, 2>1, 1>0, 0>2
if ((int_choice == 2 and random_choice_enemy_index == 0) or
        (int_choice == 1 and random_choice_enemy_index == 2) or
        (int_choice == 0 and random_choice_enemy_index == 1)):
    print("You lose!")
elif ((int_choice == 2 and random_choice_enemy_index == 1) or
      (int_choice == 1 and random_choice_enemy_index == 0) or
      (int_choice == 0 and random_choice_enemy_index == 2)):
    print("You win!")
elif int_choice == random_choice_enemy_index:
    print("It's a tie!")
else:
    print("please choose rock, paper, or scissors!")



