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
    try:
            ext_list = ['.mp3', '.flac', '.aac']  # List used to check file extension
            root.root.directory = filedialog.askopenfilenames()
            for song in root.root.directory:
                name, ext = os.path.splitext(song)
                if ext in ext_list:
                    root.songs.append(song)
            for song in root.songs:
                song_name = os.path.basename(song)  # Get the filename
                root.directory_name = song.replace(song_name, "")  # Get path of filename
                root.songlist.insert(END, song_name)
            root.songlist.selection_set(0)
            root.currentsong = root.songs[root.songlist.curselection()[0]]
    except:
            pass
    
def play_music():
    try:
            if not root.paused:
                #  Plays concatenated path of file
                root.currentsong = root.directory_name + root.songlist.get(ACTIVE)
                mixer.music.load(root.currentsong)
                if root.ticked is True:  # Checked if loop button is on, then play the looped file
                    mixer.music.play(-1)
                else:
                    mixer.music.play()
            else:
                mixer.music.unpause()
                root.paused = False
    except:
            pass
 
def pause_music():
    global paused
    mixer.music.pause()
    paused = True

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
     
     pass

def sound_up():

    pass

def stop_song():
    mixer.music.stop

def loop_song():
    mixer.music.play(loops=-1)
    pass


organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='select folder', command=load_music)
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

# grid the button
sounddown_button.grid(row=0, column=1, padx=7, pady=10)
soundup_button.grid(row=0, column=2, padx=7, pady=10)
play_button.grid(row=0, column=3, padx=7, pady=10)
stop_button.grid(row=0, column=6, padx=7, pady=10)
back_button.grid(row=0, column=5, padx=7, pady=10)
next_button.grid(row=0, column=7, padx=7, pady=10)
loop_button.grid(row=0, column=0, padx=7, pady=10)
pause_button.grid(row=0, column=8, padx=7, pady=10)


root.mainloop()

