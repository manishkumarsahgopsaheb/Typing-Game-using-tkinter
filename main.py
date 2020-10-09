from words import words


# this function is for animation for sliding the "welcome to Tying Speed Game"
def sliders():
    global count, sliderwords
    text = "welcome to Typing Speed Game"
    if count >= len(text):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(150, sliders)


def for_getting_time():
    global timer, score, miss
    if timer > 11:
        pass
    else:
        timerlabelcount.configure(fg='red')
    if timer > 0:
        timer -= 1
        timerlabelcount.configure(text=timer)
        timerlabelcount.after(1000, for_getting_time)
    else:
        gameinstructions.configure(text=f'Hit = {score} | Miss = {miss} | Total Score = {score - miss}')
        rr = messagebox.askretrycancel('Notification', 'Wanna Play Again!!!')
        if rr:
            score = 0
            miss = 0
            timer = 60
            timerlabelcount.configure(text=timer)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)


def startgame(event):
    global score, miss
    if timer == 60:
        for_getting_time()
    gameinstructions.configure(text='')
    startlabel.configure(text='')
    if wordentry.get() == wordlabel['text']:
        score += 1
        scorelabelcount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0, END)


from tkinter import *
import random
from tkinter import messagebox

##########################################

window = Tk()
window.geometry('800x600+400+100')
window.config(bg='black')
window.title('Typing Speed Game')
window.iconbitmap('logo.ico')

##########################################

score = 0
miss = 0
timer = 60
count = 0
sliderwords = ''

############################################

fontlabel = Label(window, text='Lets begin!!!', font='airal 25 italic bold', bg='black', fg='purple', width=40)
fontlabel.place(x=10, y=10)
sliders()

startlabel = Label(window, text="Lets begin!!!", font='airal 30 italic bold', bg='black', fg='green')
startlabel.place(x=275, y=50)

random.shuffle(words)

wordlabel = Label(window, text=words[0], font='airal 45 italic bold', bg='black', fg='green')
wordlabel.place(x=350, y=240)

scorelabel = Label(window, text='your Score:', font='arial 25 italic bold', bg='black', fg='red')
scorelabel.place(x=10, y=100)

scorelabelcount = Label(window, text=score, font='arial 25 italic bold', bg='black', fg='red')
scorelabelcount.place(x=150, y=180)

timerlabel = Label(window, text='Time Left', font='arial 25 italic bold', bg='black', fg='red')
timerlabel.place(x=600, y=100)

timerlabelcount = Label(window, text=timer, font='arial 25 italic bold', bg='black', fg='blue')
timerlabelcount.place(x=600, y=180)

gameinstructions = Label(window, text='Type the word and hit enter button', font='arial 25 italic bold', bg='black',
                         fg='green')
gameinstructions.place(x=150, y=500)

####################################
wordentry = Entry(window, font='airal 25 italic bold', bd=10, justify='center')
wordentry.place(x=250, y=330)
wordentry.focus_set()

######################################

window.bind('<Return>', startgame)

window.mainloop()
