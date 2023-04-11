#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


win = False
loss_cnt = 0
tie_cnt = 0


# In[3]:


print("Welcome to ROCK, PAPER, SCISSORS game!")


# In[4]:


while win == False:
    player_input = input("Enter your move: (r)ock (p)aper (s)cissors")
    match player_input:
        case "r"|"rock":
            player_choice = "ROCK"
        case "p"|"paper":
             player_choice = "PAPER"
        case "s"|"scissors":
             player_choice = "SCISSORS"
        case _:
            player_choice = "ERROR"
    print(player_choice," versus...")
    rps_action = ["ROCK", "PAPER", "SCISSORS"]
    opponent_choice = rps_action[random.randint(0,2)]
    print(opponent_choice)
    if(player_choice == opponent_choice):
        print("It is a tie!")
        tie_cnt += 1
    elif(player_choice == "ROCK"):
        if(opponent_choice == "SCISSORS"):
            print("You win!")
            win = True
        else:
            print("You lose!")
            loss_cnt += 1
    elif(player_choice == "PAPER"):
        if(opponent_choice == "ROCK"):
            print("You win!")
            win = True
        else:
            print("You lose!")
            loss_cnt += 1
    elif(player_choice == "SCISSORS"):
        if(opponent_choice == "PAPER"):
            print("You win!")
            win = True
        else:
            print("You lose!")
            loss_cnt += 1


# In[5]:


print("You have ",tie_cnt," ties and ",loss_cnt," losses before your first win.")

