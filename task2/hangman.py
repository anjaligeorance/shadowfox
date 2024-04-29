import tkinter
from tkinter.ttk import *
import random

window = tkinter.Tk()
window.title("Hangman Game")

l1 = tkinter.Label(window, text="Choose position-", font=("arial bold", 10))
l1.grid(column=0, row=0)

combo = Combobox(window)
combo['values'] = ("Word Decider", "Guesser")
combo.current(0)
combo.grid(column=1, row=0)

canvas = tkinter.Canvas(window, width=200, height=200, bg="white")
canvas.grid(column=0, row=3)  # Create canvas once

def clicked():
    global entry
    
    if combo.get() == 'Word Decider':
        l2 = tkinter.Label(window, text="Enter the word/sentence", font=("arial bold", 10))
        l2.grid(column=0, row=1)
        entry = tkinter.Entry(window)
        entry.grid(column=1, row=1)
        bt1 = Button(window, text="Click", command=lambda: decideclick(entry.get()))
        bt1.grid(column=2, row=1)

    else:
        set=['apple','orange','banana','kiwi','cucumber','onion','carrot','tomato']
        guess_word=random.choice(set)
        decideclick(guess_word)

def decideclick(text):
    global word
    word = text
    guess()

def create():
    canvas.create_line(45, 0, 45, 120)  # vertical line
    canvas.create_line(0, 120, 90, 120, width=2)  # horizontal line
    canvas.create_line(45, 20, 90, 20, width=2)
    canvas.create_line(45, 50, 70, 20, width=2)
    canvas.create_line(90, 40, 90, 20, width=2)

def guess():
    game_won = False  # Flag to indicate if the game is won
    
    def check_guess(entry_widget, i):
        nonlocal game_won  # Use nonlocal to modify the flag in the outer scope
        entry_text = entry_widget.get()
        if entry_text == word:
            l6 = tkinter.Label(window, text="Your guess was correct", font=("arial bold", 10))
            l6.grid(column=4, row=8+i)
            l7 = tkinter.Label(window, text="YOU WON THE GAME!!!", font=("arial bold", 10))
            l7.grid(column=2, row=3)
            game_won = True  # Set the flag to indicate game is won
        else:
            l7 = tkinter.Label(window, text="Your guess was incorrect, YOU LOSE A CHANCE", font=("arial bold", 10))
            l7.grid(column=4, row=8+i)
            draw_hangman(i)
            if i < 5:  # If it's not the last guess, create a new entry box
                create_entry_box(i + 1)
    
    def create_entry_box(i):
        l4 = tkinter.Label(window, text=f"(Guess {i+1} - Guess a letter)", font=("arial bold", 10))
        l4.grid(column=1, row=8+i)
        entry1 = tkinter.Entry(window)
        entry1.grid(column=2, row=8+i)
        bt2 = Button(window, text="GUESS", command=lambda entry_widget=entry1, index=i: check_guess(entry_widget, index))
        bt2.grid(column=3, row=8+i)
    
    # Start the loop with the first guess
    create_entry_box(0)



def draw_hangman(step):
    create()
    if step == 0:
        # Head
        canvas.create_oval(75, 35, 95, 55, width=2)  
    elif step == 1:
        # Body
        canvas.create_line(85, 55, 85, 80, width=2)  
    elif step == 2:
        # Left arm
        canvas.create_line(80, 60, 70, 55, width=2)   
    elif step == 3:
        # Right arm
        canvas.create_line(90, 60, 100, 55, width=2)  
    elif step == 4:
        # Left leg
        canvas.create_line(85, 80, 75, 95, width=2)   
    elif step == 5:
        # Right leg
        canvas.create_line(85, 80, 95, 95, width=2)
        l7 = tkinter.Label(window, text="YOU ARE HANGED!! YOU LOSE THE GAME", font=("arial bold", 10))
        l7.grid(column=2, row=3)





bt = Button(window, text="Enter", command=clicked)
bt.grid(column=2, row=0)

window.mainloop()
