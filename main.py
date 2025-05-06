import random
'''we will be assossiating the following number with stone , paper and scissors
stone = -1
paper = 0
scissors = 1'''

#to make computer choose a random number
computer = random.choice([-1, 0, 1])

# to get the users choice where st is for stone , p for paper and s for scissor
yourchoice = input("Enter your choice between st , p and s:")

#to convert users choice to number
choice_dict = { "st" : -1 , "p" : 0 , "s" : 1}

# to convert back user and computer choice from number to word
reverse_dict = { -1 : "stone ", 0: "paper" , 1 : "scissors"}

#to associate user choice wit correct number
you = choice_dict[yourchoice]


print(f"Your choise is :{reverse_dict[you]} \n Computer choice is :{reverse_dict[computer]}" )

# now put all the condition 

# if both user and computer get same
if(computer == you):
    print("Draw")

else:
    if(computer == -1 and you == 0 ):
        print("You win!")

    elif(computer == -1 and you == 1 ):
        print("You lose!")

    elif(computer == 0 and you == -1 ):
        print("You lose!")

    elif(computer == 0 and you == 1 ):
        print("You win!")

    elif(computer == 1 and you == -1 ):
        print("You win!")

    elif(computer == 1 and you == 0 ):
        print("You lose!")

    else:
        print("something went wrong")