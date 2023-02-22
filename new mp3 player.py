#importing libraries 
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import os

#creating the root window 
root=Tk()
root.title('Mp3 player')
root.resizable(width=False, height=False)
root.geometry("500x300")
#initialize mixer 
mixer.init()

#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15), width=50, height=10,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=7)

#add many songs to the playlist of python mp3 player
def addsongs():
    #to open a file  
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for s in temp_song:
        s=s.replace("./","")
        songs_list.insert(END,s)
     
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])

def play_music():
    song=songs_list.get(ACTIVE)
    song=f'./{song}'
    mixer.music.load(song)
    mixer.music.play()
    
#to pause the song 
def pause_music():
    mixer.music.pause()

#to stop the  song 
def stop_song():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song

def unpause():
    mixer.music.unpause()

def loop_song():
    mixer.music.play(loops=-1)
#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)


# creating the button
#sounddown_button=Button(text="🕩", bg='grey', borderwidth=0, command=sound_down, font=5)
pause_button=Button(text="⏸️", bg='green', borderwidth=0 ,command=pause_music, font=5)
#soundup_button=Button(text="🕪", bg='grey', borderwidth=0 , command=sound_up, font=5)
#back_button=Button(text="⏮️", bg='grey' , borderwidth=0 ,command=prev_music, font=5)
play_button=Button(text="▶️", bg='green', borderwidth=0 ,command=play_music, font=5)
#next_button=Button(text="⏭️", bg='grey', borderwidth=0 ,command=next_music, font=5)
loop_button=Button(text="🔁", bg='darkblue' , borderwidth=0 ,command=loop_song, font=5)
stop_button=Button(text="⏹️", bg='red', borderwidth=0 , command=stop_song, font=5)
unpause_button=Button(text="⏯️", bg='green', borderwidth=0, command=unpause, font=5 )

# grid the button
#sounddown_button.grid(row=0, column=1,)
#soundup_button.grid(row=0, column=2,)
play_button.grid(row=5, column=1,)
stop_button.grid(row=5, column=2,)
#back_button.grid(row=0, column=5,)
#next_button.grid(row=0, column=7,)
loop_button.grid(row=5, column=0,)
pause_button.grid(row=5, column=3,)
unpause_button.grid(row=5, column=4,)

mainloop()
