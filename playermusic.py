from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title("Mp3")
root.resizable(width=False, height=False)
root.geometry("400x200")

menubar = Menu(root)
root.config(menu=menubar)

song = []
current_song = ""
paused= False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song, paused

    if not paused:
        mixer.load(os.path.join(root.directory, current_song))
    else:
        mixer.music.unpause()
        paused = False

def pause_music():
    global paused
    mixer.music.pause()
    paused = True

def next_music():
    global current_song, paused

    try:
        songlist.selection_clear(0,  END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused
        
    try:
        songlist.selection_clear(0,  END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except: 
        pass
        

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='select folder', command=load_music)
menubar.add_cascade(label='Organise', menu=organise_menu )

songlist = Listbox(root, bg="black", fg="white", width=100, height=10)
songlist.pack()


control_frame = Frame(root)
control_frame.pack()
# button creation 

sounddown_button=Button(control_frame, text="🔉", bg='grey', borderwidth=0,)
pause_button=Button(control_frame, text="⏸️", bg='grey', borderwidth=0 ,command=pause_music)
soundup_button=Button(control_frame, text="🔊", bg='grey', borderwidth=0 ,)
back_button=Button(control_frame, text="⏮️", bg='blue' , borderwidth=0 ,command=prev_music)
play_button=Button(control_frame, text="▶️", bg='cyan', borderwidth=0 ,command=play_music)
next_button=Button(control_frame, text="⏭️", bg='blue', borderwidth=0 ,command=next_music)
loop_button=Button(control_frame, text="🔁", bg='grey' , borderwidth=0 ,)
stop_button=Button(control_frame, text="⏹️", bg='grey', borderwidth=0 ,)


# grid the button
sounddown_button.grid(row=0, column=1, padx=10, pady=10)
soundup_button.grid(row=0, column=2, padx=10, pady=10)
play_button.grid(row=0, column=3, padx=10, pady=10)
stop_button.grid(row=0, column=6, padx=10, pady=10)
back_button.grid(row=0, column=5, padx=10, pady=10)
next_button.grid(row=0, column=7, padx=10, pady=10)
loop_button.grid(row=0, column=0, padx=10, pady=10)
pause_button.grid(row=0, column=4, padx=10, pady=10)

root.mainloop()

