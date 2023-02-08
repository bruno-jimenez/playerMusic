from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title("Mp3")
root.resizable(width=False, height=False)
root.geometry("195x516")

# Add Image
#play_img = PhotoImage(file = "playerMusic\icons\play.png")
  
# Create button and image
#play_button= Button(root, image =play_img, borderwidth = 0, width=5, height=3)
#play_button.grid(row=3, column=5)

# grid 

racine_button=Button(root, text="1-0", bg='red' , width=5, height=3, border=2, font=10,command=lambda: button_squareroot())
racine_button.grid(row=1, column=0)

modulo_button=Button(root, text="1-1", bg='red' , width=5, height=3, border=2, font=10,command=lambda:  button_click("//"))
modulo_button.grid(row=1, column=1)

carré_button=Button(root, text="1-2", bg='red' , width=5, height=3, border=2, font=10,command=lambda: button_square())
carré_button.grid(row=1, column=2)

seven_button=Button(root, text="2-0", bg='red', width=5, height=3, border=2, font=10,command=lambda: button_click("7"))
seven_button.grid(row=2, column=0)

eight_button=Button(root, text="2-1", bg='red', width=5, height=3, border=2, font=10,command=lambda: button_click("8"))
eight_button.grid(row=2, column=1)

nine_button=Button(root, text="2-2", bg='red', width=5, height=3, border=2, font=10,command=lambda: button_click("9"))
nine_button.grid(row=2, column=2)

four_button=Button(root, text="3-0", bg='red', width=5, height=3, border=2, font=10,command=lambda: button_click("4"))
four_button.grid(row=3, column=0)

five_button=Button(root, text="3-1", bg='red', width=5, height=3, border=2, font=10,command=lambda: button_click("5"))
five_button.grid(row=3, column=1)

six_button=Button(root, text="3-2", bg='red', width=5, height=3, border=2, font=10,command=lambda: button_click("6"))
six_button.grid(row=3, column=2)


sounddown_button=Button(root, text="4-0", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("1"))
sounddown_button.grid(row=4, column=0)

mute_button=Button(root, text="4-1", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("2"))
mute_button.grid(row=4, column=1)

soundup_button=Button(root, text="4-2", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("3"))
soundup_button.grid(row=4, column=2)


back_button=Button(root, text="5-0", bg='blue' , width=5, height=3, border=2, font=10,command=lambda: button_clear())
back_button.grid(row=5, column=0)

pause_button=Button(root, text="5-1", bg='cyan', width=5, height=3, border=2, font=10,command=lambda: button_click("0"))
pause_button.grid(row=5, column=1)

next_button=Button(root, text="5-2", bg='blue', width=5, height=3, border=2, font=10,command=lambda: button_click("."))
next_button.grid(row=5, column=2)


loop_button=Button(root, text="6-0", bg='grey' , width=5, height=3, border=2, font=10,command=lambda: button_clear())
loop_button.grid(row=6, column=0)

stop_button=Button(root, text="6-1", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("0"))
stop_button.grid(row=6, column=1)

playlist_button=Button(root, text="6-2", bg='grey', width=5, height=3, border=2, font=10,command=lambda: button_click("."))
playlist_button.grid(row=6, column=2)


root.mainloop()

