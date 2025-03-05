from tkinter import *
from tkinter import messagebox

m = Tk()
m.title('Tic-Tac-Toe Game')   

# global variables
clicked = True  # True for X, False for O
count = 0  # Count the number of moves
buttons = []  # List to store buttons

# Disabled all buttons 
def buttons_disabled():
    b1.config(state= DISABLED)
    b2.config(state= DISABLED)
    b3.config(state= DISABLED)
    b4.config(state= DISABLED)
    b5.config(state= DISABLED)
    b6.config(state= DISABLED)
    b7.config(state= DISABLED)
    b8.config(state= DISABLED)
    b9.config(state= DISABLED)
    messagebox.showwarning("Tic Tac Toe", " Game Over! \n Select Reset for New Game  ")
       
# Checking Who Wins 
def check_Winner():
    global winner
    winner = False

    # Check if X Wins 
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" :
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !! X is the Winner " )
        buttons_disabled()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" :
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !! X is the Winner " )
        buttons_disabled()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" :
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !! X is the Winner " )
        buttons_disabled()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" :
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !! X is the Winner " )
        buttons_disabled()                

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" :
        b2["bg"] = "green"
        b5["bg"] = "green"
        b8["bg"] = "green"
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !!  X is the Winner  " )
        buttons_disabled() 

    elif b3["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" :
        b3["bg"] = "green"
        b5["bg"] = "green"
        b9["bg"] = "green"
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !!  X is the Winner  " )
        buttons_disabled() 

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" :
        b1["bg"] = "green"
        b5["bg"] = "green"
        b9["bg"] = "green"
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !!  X is the Winner  " )
        buttons_disabled()   

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" :
        b3["bg"] = "green"
        b5["bg"] = "green"
        b7["bg"] = "green"
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !!  X is the Winner  " )
        buttons_disabled() 

    # Check if O Wins 
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" :
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !! O is the Winner " )
        buttons_disabled()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" :
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !! O is the Winner " )
        buttons_disabled()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" :
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !! O is the Winner " )
        buttons_disabled()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" :
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !! O is the Winner " )
        buttons_disabled()                

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" :
        b2["bg"] = "green"
        b5["bg"] = "green"
        b8["bg"] = "green"
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !!  O is the Winner  " )
        buttons_disabled() 

    elif b3["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" :
        b3["bg"] = "green"
        b5["bg"] = "green"
        b9["bg"] = "green"
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !!  O is the Winner  " )
        buttons_disabled() 

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" :
        b1["bg"] = "green"
        b5["bg"] = "green"
        b9["bg"] = "green"
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !!  O is the Winner  " )
        buttons_disabled()   

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" :
        b3["bg"] = "green"
        b5["bg"] = "green"
        b7["bg"] = "green"
        winner = True
        messagebox.showinfo("Tic Tac Toe ", " Congratulation !!  O is the Winner  " )
        buttons_disabled() 
            
    else :
        if count == 9 and winner == False :
            messagebox.showinfo ("Tic Tac Toe", " Game is Tie, Try Again !! ")
            buttons_disabled()

# User click of button 
def b_click(b):
    global clicked, count
    b.config 
    if b["text"] == " " and clicked == True :  
        b["text"] = "X"
        clicked = False
        count += 1
        check_Winner()

    elif b["text"] == " " and clicked == False : 
        b["text"] = "O"
        clicked = True
        count += 1
        check_Winner()

    else :
        messagebox.showerror("Tic Tac Toe ", " Invalid Move ! \n Try Again")

# Game Reset
def reset_game():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked
    global count
    clicked = True
    count  = 0

    # Builds of Buttons
    b1 = Button(m , text =" ", font = ("Helvetica Bold", 20), height = 3, width=6, bg = "SystemButtonFace", command = lambda:b_click(b1) )
    b2 = Button(m , text =" ", font = ("Helvetica Bold", 20), height = 3, width=6, bg = "SystemButtonFace", command = lambda:b_click(b2) )
    b3 = Button(m , text =" ", font = ("Helvetica Bold", 20), height = 3, width=6, bg = "SystemButtonFace", command = lambda:b_click(b3) )

    b4 = Button(m , text =" ", font = ("Helvetica Bold", 20), height = 3, width=6, bg = "SystemButtonFace", command = lambda:b_click(b4) )
    b5 = Button(m , text =" ", font = ("Helvetica Bold", 20), height = 3, width=6, bg = "SystemButtonFace", command = lambda:b_click(b5) )
    b6 = Button(m , text =" ", font = ("Helvetica Bold", 20), height = 3, width=6, bg = "SystemButtonFace", command = lambda:b_click(b6) )

    b7 = Button(m , text =" ", font = ("Helvetica Bold", 20), height = 3, width=6, bg = "SystemButtonFace", command = lambda:b_click(b7) )
    b8 = Button(m , text =" ", font = ("Helvetica Bold", 20), height = 3, width=6, bg = "SystemButtonFace", command = lambda:b_click(b8) )
    b9 = Button(m , text =" ", font = ("Helvetica Bold", 20), height = 3, width=6, bg = "SystemButtonFace", command = lambda:b_click(b9) )

    # Grid buttons
    b1.grid(row= 0, column = 0 )
    b2.grid(row= 0, column = 1 )
    b3.grid(row= 0, column = 2 )

    b4.grid(row= 1, column = 0 )
    b5.grid(row= 1, column = 1 )
    b6.grid(row= 1, column = 2 )

    b7.grid(row= 2, column = 0 )
    b8.grid(row= 2, column = 1 )
    b9.grid(row= 2, column = 2 )

# Game Menu
game_menu = Menu(m)
m.config(menu = game_menu)

# Game option menu
options_menu = Menu(game_menu,tearoff= False)
game_menu.add_cascade(label=" Game Options ", menu = options_menu)

options_menu.add_command(label= "Reset ", command = reset_game)


reset_game()
m.mainloop()