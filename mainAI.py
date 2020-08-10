#noughts and crosses impossible
import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import random

try:
    handle = sql.connect("TrainData.db")
    cursor = handle.cursor()
    cursor.execute("CREATE TABLE RESULTS(TRAINID INT, ARRAY BLOB, WIN TEXT)")
    cursor.execute("CREATE TABLE XWIN(TRAINID INT, ARRAY BLOB, WIN TEXT)")
    cursor.execute("CREATE TABLE TIES(TRAINID INT, ARRAY BLOB, WIN TEXT)")
    cursor.execute("CREATE TABLE OWIN(TRAINID INT, ARRAY BLOB, WIN TEXT)")
    handle.commit()
    handle.close()
except:
    cont = True

def wins(win, array):
    handle = sql.connect("TrainData.db")
    cursor = handle.cursor()
    cursor.execute("INSERT INTO RESULTS VALUES(?,?,?)", ("1", str(array), str(win)))
    handle.commit()
    handle.close()
    topLeft.configure(state='disabled')
    topMid.configure(state='disabled')
    topRight.configure(state='disabled')
    midLeft.configure(state='disabled')
    midMid.configure(state='disabled')
    midRight.configure(state='disabled')
    botLeft.configure(state='disabled')
    botMid.configure(state='disabled')
    botRight.configure(state='disabled')
    message = "Result = "+win
    declarewin = tk.Label(game, text=message).grid(row=3, column=0)

def tl(gamearray, player, topLeft, countings):
    topLeft.configure(text = player)
    topLeft.configure(state='disabled')
    gamearray[0] = player
    win = testwin(gamearray)
    countings = countings+1
    if countings == 5:
        wins(win, gamearray)
    temp = ""
    for i in range(0, len(gamearray)):
        if gamearray[i] == " ":
            temp = True
    if temp == "":
        wins(win, gamearray)
    if win == "Tie":
        makemove(gamearray, win)
    else:
        wins(win, gamearray)
def tm(gamearray, player, topMid, countings):
    topMid.configure(text = player)
    topMid.configure(state='disabled')
    gamearray[1] = player
    win = testwin(gamearray)
    countings = countings+1
    if countings == 5:
        wins(win, gamearray)
    temp = ""
    for i in range(0, len(gamearray)):
        if gamearray[i] == " ":
            temp = True
    if temp == "":
        wins(win, gamearray)
    if win == "Tie":
        makemove(gamearray, win)
    else:
        wins(win, gamearray)
def tr(gamearray, player, topRight, countings):
    topRight.configure(text = player)
    topRight.configure(state='disabled')
    gamearray[2] = player
    win = testwin(gamearray)
    countings = countings+1
    if countings == 5:
        wins(win, gamearray)
    temp = ""
    for i in range(0, len(gamearray)):
        if gamearray[i] == " ":
            temp = True
    if temp == "":
        wins(win, gamearray)
    if win == "Tie":
        makemove(gamearray, win)
    else:
        wins(win, gamearray)
def ml(gamearray, player, midLeft, countings):
    midLeft.configure(text = player)
    midLeft.configure(state='disabled')
    gamearray[3] = player
    win = testwin(gamearray)
    countings = countings+1
    if countings == 5:
        wins(win, gamearray)
    temp = ""
    for i in range(0, len(gamearray)):
        if gamearray[i] == " ":
            temp = True
    if temp == "":
        wins(win, gamearray)
    if win == "Tie":
        makemove(gamearray, win)
    else:
        wins(win, gamearray)
def mm(gamearray, player, midMid, countings):
    midMid.configure(text = player)
    midMid.configure(state='disabled')
    gamearray[4] = player
    win = testwin(gamearray)
    countings = countings+1
    if countings == 5:
        wins(win, gamearray)
    temp = ""
    for i in range(0, len(gamearray)):
        if gamearray[i] == " ":
            temp = True
    if temp == "":
        wins(win, gamearray)
    if win == "Tie":
        makemove(gamearray, win)
    else:
        wins(win, gamearray)
def mr(gamearray, player, midRight, countings):
    midRight.configure(text = player)
    midRight.configure(state='disabled')
    gamearray[5] = player
    win = testwin(gamearray)
    countings = countings+1
    if countings == 5:
        wins(win, gamearray)
    temp = ""
    for i in range(0, len(gamearray)):
        if gamearray[i] == " ":
            temp = True
    if temp == "":
        wins(win, gamearray)
    if win == "Tie":
        makemove(gamearray, win)
    else:
        wins(win, gamearray)
def bl(gamearray, player, botLeft, countings):
    botLeft.configure(text = player)
    botLeft.configure(state='disabled')
    gamearray[6] = player
    win = testwin(gamearray)
    countings = countings+1
    if countings == 5:
        wins(win, gamearray)
    temp = ""
    for i in range(0, len(gamearray)):
        if gamearray[i] == " ":
            temp = True
    if temp == "":
        wins(win, gamearray)
    if win == "Tie":
        makemove(gamearray, win)
    else:
        wins(win, gamearray)
def bm(gamearray, player, botMid, countings):
    botMid.configure(text = player)
    botMid.configure(state='disabled')
    gamearray[7] = player
    win = testwin(gamearray)
    countings = countings+1
    if countings == 5:
        wins(win, gamearray)
    temp = ""
    for i in range(0, len(gamearray)):
        if gamearray[i] == " ":
            temp = True
    if temp == "":
        wins(win, gamearray)
    if win == "Tie":
        makemove(gamearray, win)
    else:
        wins(win, gamearray)
def br(gamearray, player, botRight, countings):
    botRight.configure(text = player)
    botRight.configure(state='disabled')
    gamearray[8] = player
    win = testwin(gamearray)
    countings = countings+1
    if countings == 5:
        wins(win, gamearray)
    temp = ""
    for i in range(0, len(gamearray)):
        if gamearray[i] == " ":
            temp = True
    if temp == "":
        wins(win, gamearray)
    if win == "Tie":
        makemove(gamearray, win)
    else:
        wins(win, gamearray)

        
def createtraining(repeats):
    array = [" "]*9
    count = 0
    for x in range(0, repeats):
        norepeats = False
        count = count+1
        for x in range(1, 9):
            if x == 1 or x == 3 or x == 5 or x == 7 or x == 9:
                letter = "X"
            elif x == 2 or x == 4 or x == 6 or x == 7 or x == 8:
                letter = "O"
            integer = random.randint(0, 8)
            notbreak = False
            while array[integer] == "X" or array[integer] == "O" and notbreak == False:
                integer = random.randint(0, 8)
                bcount = 0
                for b in range(0, len(array)):
                    if array[b] == " ":
                        bcount = bcount+1
                if bcount == 0:
                    notbreak = True
                    break
            array[integer] = letter
            win = testwin(array)
            if win == "O" and norepeats == False:
                handle = sql.connect("TrainData.db")
                cursor = handle.cursor()
                print("O win")
                print(array)
                cursor.execute("INSERT INTO OWIN VALUES(?,?,?)", (int(count), str(array), str(win)))
                handle.commit()
                handle.close()
                norepeats = True
        if norepeats == False:
            win = testwin(array)
            if win == "O":
                handle = sql.connect("TrainData.db")
                cursor = handle.cursor()
                print("O win")
                print(array)
                cursor.execute("INSERT INTO OWIN VALUES(?,?,?)", (int(count), str(array), str(win)))
                handle.commit()
                handle.close()

def testwin(array):
    if array[0] == array[1] == array[2] and array[0] != " " and array[1] != " " and array[2] != " ":
        win = array[1]
    elif array[0] == array[3] == array[6] and array[0] != " " and array[3] != " " and array[6] != " ":
        win = array[3]
    elif array[0] == array[4] == array[8] and array[0] != " " and array[4] != " " and array[8] != " ":
        win = array[4]
    elif array[4] == array[3] == array[5] and array[4] != " " and array[3] != " " and array[5] != " ":
        win = array[3]
    elif array[5] == array[2] == array[8] and array[5] != " " and array[2] != " " and array[8] != " ":
        win = array[2]
    elif array[6] == array[7] == array[8] and array[6] != " " and array[7] != " " and array[8] != " ":
        win = array[7]
    elif array[1] == array[7] == array[4] and array[1] != " " and array[7] != " " and array[4] != " ":
        win = array[7]
    elif array[2] == array[4] == array[6] and array[2] != " " and array[4] != " " and array[6] != " ":
        win = array[4]
    try:
        if win == "O" or win == "X":
            cont = True
        else:
            win = "Tie"
    except:
        win = "Tie"
    return win

def makemove(gamearray, win):
    #move to make 3 or block a potential 3
    array = gamearray
    proirity = False
    proirityarr = []
    move = ""
    #top row X_X _XX XX_ - 0,1,2
    if array[0] == array[1] and array[0] != " " and array[1] != " " and array[2] == " ":
        if array[0] == "O":
            proirityarr.append("2")
            proirity = True
        else:
            move = "2"
    elif array[0] == array[2] and array[0] != " " and array[1] == " " and array[2] != " ":
        if array[0] == "O":
            proirityarr.append("1")
            proirity = True
        else:
            move = "1"
    elif array[1] == array[2] and array[0] == " " and array[1] != " " and array[2] != " ":
        if array[1] == "O":
            proirityarr.append("0")
            proirity = True
        else:
            move = "0"
    #middle row X_X _XX XX_ - 3,4,5
    elif array[3] == array[4] and array[5] == " " and array[4] != " " and array[3] != " ":
        if array[3] == "O":
            proirityarr.append("5")
            proirity = True
        else:
            move = "5"
    elif array[3] == array[5] and array[4] == " " and array[5] != " " and array[3] != " ":
        if array[3] == "O":
            proirityarr.append("4")
            proirity = True
        else:
            move = "4"
    elif array[4] == array[5] and array[3] == " " and array[4] != " " and array[5] != " ":
        if array[4] == "O":
            proirityarr.append("3")
            proirity = True
        else:
            move = "3"
    #bottom row X_X _XX XX_ - 6,7,8
    elif array[6] == array[7] and array[8] == " " and array[6] != " " and array[7] != " ":
        if array[6] == "O":
            proirityarr.append("8")
            proirity = True
        else:
            move = "8"
    elif array[7] == array[8] and array[6] == " " and array[7] != " " and array[8] != " ":
        if array[7] == "O":
            proirityarr.append("6")
            proirity = True
        else:
            move = "6"
    elif array[6] == array[8] and array[7] == " " and array[8] != " " and array[6] != " ":
        if array[6] == "O":
            proirityarr.append("7")
            proirity = True
        else:
            move = "7"
    #left column XX_ _XX X_X - 0,3,6
    elif array[0] == array[3] and array[6] == " " and array[0] != " " and array[3] != " ":
        if array[0] == "O":
            proirityarr.append("6")
            proirity = True
        else:
            move = "6"
    elif array[3] == array[6] and array[0] == " " and array[6] != " " and array[3] != " ":
        if array[3] == "O":
            proirityarr.append("0")
            proirity = True
        else:
            move = "0"
    elif array[0] == array[6] and array[3] == " " and array[0] != " " and array[6] != " ":
        if array[0] == "O":
            proirityarr.append("3")
            proirity = True
        else:
            move = "3"
    #middle column XX_ _XX X_X - 1,4,7
    elif array[1] == array[4] and array[7] == " " and array[1] != " " and array[4] != " ":
        if array[1] == "O":
            proirityarr.append("7")
            proirity = True
        else:
            move = "7"
    elif array[4] == array[7] and array[1] == " " and array[7] != " " and array[4] != " ":
        if array[4] == "O":
            proirityarr.append("1")
            proirity = True
        else:
            move = "1"
    elif array[1] == array[7] and array[4] == " " and array[1] != " " and array[7] != " ":
        if array[1] == "O":
            proirityarr.append("4")
            proirity = True
        else:
            move = "4"
    #right column XX_ _XX X_X - 2,5,8
    elif array[2] == array[5] and array[8] == " " and array[2] != " " and array[5] != " ":
        if array[2] == "O":
            proirityarr.append("8")
            proirity = True
        else:
            move = "8"
    elif array[5] == array[8] and array[2] == " " and array[8] != " " and array[5] != " ":
        if array[5] == "O":
            proirityarr.append("2")
            proirity = True
        else:
            move = "2"
    elif array[2] == array[8] and array[5] == " " and array[2] != " " and array[8] != " ":
        if array[2] == "O":
            proirityarr.append("5")
            proirity = True
        else:
            move = "5"
    #top-left, bottom-right diagonal XX_ X_X _XX - 0,4,8
    elif array[0] == array[4] and array[8] == " " and array[0] != " " and array[4] != " ":
        if array[0] == "O":
            proirityarr.append("8")
            proirity = True
        else:
            move = "8"
    elif array[4] == array[8] and array[0] == " " and array[8] != " " and array[4] != " ":
        if array[4] == "O":
            proirityarr.append("0")
            proirity = True
        else:
            move = "0"
    elif array[0] == array[8] and array[4] == " " and array[0] != " " and array[8] != " ":
        if array[0] == "O":
            proirityarr.append("4")
            proirity = True
        else:
            move = "4"
    #top-right, bottom-left diagonal XX_ X_X _XX - 2,4,6
    elif array[2] == array[4] and array[6] == " " and array[2] != " " and array[4] != " ":
        if array[2] == "O":
            proirityarr.append("6")
            proirity = True
        else:
            move = "6"
    elif array[4] == array[6] and array[2] == " " and array[6] != " " and array[4] != " ":
        if array[4] == "O":
            proirityarr.append("2")
            proirity = True
        else:
            move = "2"
    elif array[0] == array[8] and array[4] == " " and array[0] != " " and array[8] != " ":
        if array[0] == "O":
            proirityarr.append("4")
            proirity = True
        else:
            move = "4"
    else:
        #add learning off previous runs
        if array[4] == " ":
            move = 4
        else:
            handle = sql.connect("TrainData.db")
            cursor = handle.cursor()
            cursor.execute("SELECT ARRAY FROM RESULTS WHERE WIN = ? AND ARRAY != ?", (str(win), "''"))
            arrays = cursor.fetchall()
            handle.commit()
            handle.close()
            arrays = list(arrays)
            overallcounts = []
            for t in range(0, len(arrays)):
                arrays[t] = str(arrays[t])
                arrays[t] = arrays[t][2:len(arrays[t])-3]
                xpos = []
                opos = []
                counts = 0
                for u in range(0, len(arrays[t])):
                    if arrays[t][u] == "X":
                        xpos.append(u)
                    elif arrays[t][u] == "O":
                        opos.append(u)
                arraystr = str(array)
                for k in range(0, len(xpos)):
                    pos = xpos[k]
                    if arraystr[pos] == "X":
                        counts = counts+1
                for l in range(0, len(opos)):
                    pos = opos[l]
                    if arraystr[pos] == "O":
                        counts = counts+1
                overallcounts.append(counts)
            sortcounts = overallcounts
            overallcounts.sort()
            highest = overallcounts[len(overallcounts)-1]
            for t in range(0, len(arrays)):
                arrays[t] = str(arrays[t])
                xpos = []
                opos = []
                counts = 0
                for u in range(0, len(arrays[t])):
                    if arrays[t][u] == "X":
                        xpos.append(u)
                    elif arrays[t][u] == "O":
                        opos.append(u)
                arraystr = str(array)
                for k in range(0, len(xpos)):
                    pos = xpos[k]
                    if arraystr[pos] == "X":
                        counts = counts+1
                for l in range(0, len(opos)):
                    pos = opos[l]
                    if arraystr[pos] == "O":
                        counts = counts+1
                if counts == highest:
                    simarr = arrays[t]
            for d in range(0, len(simarr)):
                if simarr[d] == "O":
                    move = d
            if move == 2:
                move = "0"
            elif move == 7:
                move = "1"
            elif move == 12:
                move = "2"
            elif move == 17:
                move = "3"
            elif move == 22:
                move = "4"
            elif move == 27:
                move = "5"
            elif move == 32:
                move = "6"
            elif move == 37:
                move = "7"
            elif move == 42:
                move = "8"
    hold = True
    temp = ""
    for i in range(0, len(array)):
        if array[i] == " ":
            temp = True
    if temp == "":
        hold = False
        wins(win, array)
    if proirity == True:
        move = proirityarr[0]
    num = int(move)
    if num == 0:
        topLeft.configure(text = "O")
        topLeft.configure(state='disabled')
        array[num] = "O"
    elif num == 1:
        topMid.configure(text = "O")
        topMid.configure(state='disabled')
        array[num] = "O"
    elif num == 2:
        topRight.configure(text = "O")
        topRight.configure(state='disabled')
        array[num] = "O"
    elif num == 3:
        midLeft.configure(text = "O")
        midLeft.configure(state='disabled')
        array[num] = "O"
    elif num == 4:
        midMid.configure(text = "O")
        midMid.configure(state='disabled')
        array[num] = "O"
    elif num == 5:
        midRight.configure(text = "O")
        midRight.configure(state='disabled')
        array[num] = "O"
    elif num == 6:
        botLeft.configure(text = "O")
        botLeft.configure(state='disabled')
        array[num] = "O"
    elif num == 7:
        botMid.configure(text = "O")
        botMid.configure(state='disabled')
        array[num] = "O"
    elif num == 8:
        botRight.configure(text = "O")
        botRight.configure(state='disabled')
        array[num] = "O"
    array = gamearray
    win = testwin(array)
    if win == "Tie":
        cont = True
    else:
        wins(win, array)
    
# 0-1-2
# 3-4-5
# 6-7-8
countings = 0
gamearray = [" "]*9
game = tk.Tk()
game.title("Noughts and Crosses - impossible")
game.geometry("")
app = Frame(game)
app.grid()
player = "X"
#Top Row
topLeft = Button(app, text = "-", font = "Ariel 20 bold", activebackground="green", command= lambda: tl(gamearray, player, topLeft, countings))
topLeft.grid(row = 0, column = 0, ipadx=20, ipady=18, padx=10, pady=10)
topMid = Button(app, text = "-", font = "Ariel 20 bold", activebackground="green", command= lambda: tm(gamearray, player, topMid, countings))
topMid.grid(row = 0, column = 1, ipadx=20, ipady=18, padx=10, pady=10)
topRight = Button(app, text = "-", font = "Ariel 20 bold", activebackground="green", command= lambda: tr(gamearray, player, topRight, countings))
topRight.grid(row = 0, column = 2, ipadx=20, ipady=18, padx=10, pady=10)
#Middle Row
midLeft = Button(app, text = "-", font = "Ariel 20 bold", activebackground="red", command= lambda: ml(gamearray, player, midLeft, countings))
midLeft.grid(row = 1, column = 0, ipadx=20, ipady=18, padx=10, pady=10)
midMid = Button(app, text = "-", font = "Ariel 20 bold", activebackground="red", command= lambda: mm(gamearray, player, midMid, countings))
midMid.grid(row = 1, column = 1, ipadx=20, ipady=18, padx=10, pady=10)
midRight = Button(app, text = "-", font = "Ariel 20 bold", activebackground="red", command= lambda: mr(gamearray, player, midRight, countings))
midRight.grid(row = 1, column = 2, ipadx=20, ipady=18, padx=10, pady=10)
#Bottom Row
botLeft = Button(app, text = "-", font = "Ariel 20 bold", activebackground="blue", command= lambda: bl(gamearray, player, botLeft, countings))
botLeft.grid(row = 2, column = 0, ipadx=20, ipady=18, padx=10, pady=10)
botMid = Button(app, text = "-", font = "Ariel 20 bold", activebackground="blue", command= lambda: bm(gamearray, player, botMid, countings))
botMid.grid(row = 2, column = 1, ipadx=20, ipady=18, padx=10, pady=10)
botRight = Button(app, text = "-", font = "Ariel 20 bold", activebackground="blue", command= lambda: br(gamearray, player, botRight, countings))
botRight.grid(row = 2, column = 2, ipadx=20, ipady=18, padx=10, pady=10)
game.mainloop()

#createtraining(1000000000)
