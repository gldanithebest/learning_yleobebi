import random
from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("rock paper scissors game")

user_score = 0
comp_score = 0


def rock():
    global user_choice
    global comp_choice
    user_choice='rock'
    comp_choice = random_comp_choice()
    result(user_choice,comp_choice)
def paper():
    global user_choice
    global comp_choice
    user_choice='paper'
    comp_choice = random_comp_choice()
    result(user_choice,comp_choice)
def scissors():
    global user_choice
    global comp_choice
    user_choice='scissors'
    comp_choice = random_comp_choice()
    result(user_choice,comp_choice)

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissors':2} 

    return rps[choice]


def random_comp_choice():
    return random.choice(['rock','paper','scissors'])

def result(user_choice,comp_choice):
    global user_score
    global comp_score
    user = choice_to_number(user_choice)
    comp = choice_to_number(comp_choice)
    if (user == comp):
        print('tie')
    elif((user-comp)%3==1):
        print('you win')
        user_score+=1
    else:
        print('comp wins')
        comp_score+=1

    text_area = Text(master = window, height = 12, width = 30, bg = "#FFFF99")
    text_area.grid(column = 0, row = 4)
    answer = f"Your Choice: {user_choice} \nComputer's Choice : {comp_choice} \n Your Score : {user_score} \n Computer Score : {comp_score} "
    text_area.insert(END,answer)




button1 = Button(text="       Rock       ",bg="skyblue",command=rock)
button1.grid(column=3,row=1)
button2 = Button(text="       Paper      ",bg="pink",command=paper)
button2.grid(column=3,row=2)
button3 = Button(text="      Scissors     ",bg="lightgreen",command=scissors)
button3.grid(column=3,row=3)



window.mainloop()