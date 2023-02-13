from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title("Mp3")
root.resizable(width=False, height=False)
root.geometry("500x300")

menubar = Menu(root)
root.config(menu=menubar)

song = []
current_song = ""
paused= False

mixer.init()

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            song.append(song)

    for song in song:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = song[songlist.curselection()[0]]

def play_music():
    global current_song, paused

    if not paused:
        mixer.music.load(os.path.join(root.directory, current_song))
    else:
        mixer.music.unpause()
        paused = False
 

def pause_music():
    global paused
    mixer.music.pause()



def next_music():
    global current_song, paused

    try:
        songlist.selection_clear(0,  END)
        songlist.selection_set(song.index(current_song) + 1)
        current_song = song[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused
        
    try:
        songlist.selection_clear(0,  END)
        songlist.selection_set(song.index(current_song) - 1)
        current_song = song[songlist.curselection()[0]]
        play_music()
    except: 
        pass

def sound_down():
    mixer.music.set_volume(volume=+10)
    pass

def sound_up():
    mixer.music.set_volume(volume=+10)
    pass

def stop_song():
    mixer.music.stop

def loop_song():
    mixer.music.play(loops=-1)
    pass

def unpause():      
    mixer.music.unpause()

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='select folder', command= load_music)
menubar.add_cascade(label='Add music', menu=organise_menu )

songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()


control_frame = Frame(root)
control_frame.pack()
# button creation 

sounddown_button=Button(control_frame, text="🕩", bg='grey', borderwidth=0, command=sound_down, font=5)
pause_button=Button(control_frame, text="⏸️", bg='green', borderwidth=0 ,command=pause_music, font=5)
soundup_button=Button(control_frame, text="🕪", bg='grey', borderwidth=0 , command=sound_up, font=5)
back_button=Button(control_frame, text="⏮️", bg='grey' , borderwidth=0 ,command=prev_music, font=5)
play_button=Button(control_frame, text="▶️", bg='green', borderwidth=0 ,command=play_music, font=5)
next_button=Button(control_frame, text="⏭️", bg='grey', borderwidth=0 ,command=next_music, font=5)
loop_button=Button(control_frame, text="🔁", bg='darkblue' , borderwidth=0 , command=loop_song, font=5)
stop_button=Button(control_frame, text="⏹️", bg='red', borderwidth=0 , command=stop_song, font=5)
unpause_button=Button(control_frame, text="⏯️", bg='green', borderwidth=0, command=unpause, font=5 )

# grid the button
sounddown_button.grid(row=0, column=1, padx=7, pady=10)
soundup_button.grid(row=0, column=2, padx=7, pady=10)
play_button.grid(row=0, column=3, padx=7, pady=10)
stop_button.grid(row=0, column=6, padx=7, pady=10)
back_button.grid(row=0, column=5, padx=7, pady=10)
next_button.grid(row=0, column=7, padx=7, pady=10)
loop_button.grid(row=0, column=0, padx=7, pady=10)
pause_button.grid(row=0, column=8, padx=7, pady=10)
unpause_button.grid(row=0, column=9, padx=7, pady=10)

root.mainloop()

