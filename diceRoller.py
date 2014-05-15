import random #Random for dice
import time #Imported time for

roll=0  #Used in tie with global variable

def roll(): #Roll for dice
    print("rolling.....")
    global roll = random.randint(1, 6) #Error with the equals sign
    

def show_dice(roll):    #Takes roll number and prints it as a dice
    if roll == 1:
        print(S1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)


s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

roll() #Runs roll function
time.sleep(1)
show_dice(roll) #Runs show_dice function


