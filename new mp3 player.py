# importing libraries
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import os

# creating the root window
root = Tk()
root.title('Mp3 player')
root.resizable(width=False, height=False)
root.geometry("500x300")
# initialize mixer
mixer.init()

songs = []
current_song = ""
paused= False

# create the listbox to contain songs
songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 9), width=80, height=15,selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

def addsongs():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                songs_list.delete(1, END)
                songs_list.insert(END,song)
     
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])

def play_music():  
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.set_volume(0.9)
    mixer.music.play()

def next_music():
    global current_song, paused

    try:
        songs_list.selection_set(songs.index(current_song) + 1)
        current_song = songs[songs_list.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused
        
    try:
        songs_list.selection_set(songs.index(current_song) - 1)
        current_song = songs[songs_list.curselection()[0]]
        play_music()
    except: 
        pass


# to pause the song
def pause_music():
    mixer.music.pause()


# to stop the  song
def stop_song():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)


# to resume the song

def unpause():
    mixer.music.unpause()


def loop_song():
    mixer.music.play(loops=-1)

def sound_down():
    #mixer.music.get_volume(+15)
    pass

def sound_up():
    #mixer.music.get_volume(-15)
    pass


#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)


# creating the button
sounddown_button=Button(text="🕩", bg='grey', borderwidth=0, command=sound_down, font=5)
pause_button = Button(text="⏸️", bg='green', borderwidth=0, command=pause_music, font=5)
soundup_button=Button(text="🕪", bg='grey', borderwidth=0 , command=sound_up, font=5)
back_button=Button(text="⏮️", bg='grey' , borderwidth=0 ,command=prev_music, font=5)
play_button = Button(text="▶️", bg='green', borderwidth=0, command=play_music, font=5)
next_button=Button(text="⏭️", bg='grey', borderwidth=0 ,command=next_music, font=5)
loop_button = Button(text="🔁", bg='darkblue', borderwidth=0, command=loop_song, font=5)
stop_button = Button(text="⏹️", bg='red', borderwidth=0, command=stop_song, font=5)
unpause_button = Button(text="⏯️", bg='green', borderwidth=0, command=unpause, font=5)

# grid the button
loop_button.grid(row=5, column=0, padx=9, pady=15)
sounddown_button.grid(row=5, column=1, padx=9, pady=15)
soundup_button.grid(row=5, column=2, padx=9, pady=15)
play_button.grid(row=5, column=3, padx=9, pady=15)
stop_button.grid(row=5, column=4, padx=9, pady=15)
back_button.grid(row=5, column=5, padx=9, pady=15)
next_button.grid(row=5, column=6, padx=9, pady=15)
pause_button.grid(row=5, column=7, padx=9, pady=15)
unpause_button.grid(row=5, column=8, padx=9, pady=15)

mainloop()

