import random
from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("rock paper scissors game")

user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissors':2}
    return rps[choice]

def number_to_choice(number):
    rps = {0:'rock', 1:'paper',2:'scissors'}
    return rps[number]

def random_comp_choice():
    return random.choice(['rock','paper','scissors'])

def result(user_choice,comp_choice):
    global user_score
    global comp_choice
    user = choice_to_number(user_choice)
    comp = choice_to_number(comp_choice)
    if (user == comp):
        print('tie')
    elif((user-comp)%3=1):
        print('you win')
        user_score+=1
    else:
        print('comp wins')
        comp_score+=1

    text_area = Text(master = window, height = 12, width = 30, bg = "#FFFF99")
    text_area.grid(column = 0, row = 4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=user_choice,cc=comp_choice,u=user_score,c=comp_score)
    text_area.insert(END,answer)


def rock():
    global user_choice
    global comp_choice
    user_choice='rock'