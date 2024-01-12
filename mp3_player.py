from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer #Pygame is a set of Python modules designed for writing video games
# pip install pygame     to install pygame in command prompt
import os
from PIL import ImageTk, Image   #for resizing images      pip install Pillow


windows = Tk()
windows.title('MP3 Media Player')
windows.geometry('925x675+290+85')
windows.configure(bg='#FEC540')
windows.resizable(False,False) #this is to make the window not resizable



mixer.init()  #to load the audio files
def open_folder():
    path= filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        # print(songs)
        for song in songs:
            if song.endswith('.mp3'):
                playlist.insert(END,song)
                
def play_song():
    music_name=playlist.get(ACTIVE)
    # print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music_title.config(text=music_name[0:-4])



#to change mp3 logo at the title of the app
mp3_logo=PhotoImage(file='music_title_logo.png')
windows.iconphoto(False, mp3_logo)

Top=PhotoImage(file='MP3_top.png')
Label(windows, image=Top, bg='#FEC540').pack()

#logo
Logo=PhotoImage(file='Mp3_media_logo.png')
Label(windows, image=Logo, bg='#FEC540').place(x=62, y=110)

#buttons
play=PhotoImage(file='Play.png')
Button(windows, image=play,bg='#FEC540',bd=0, command=play_song).place(x=100, y=400)

stop=PhotoImage(file='Stop.png')
Button(windows, image=stop,bg='#FEC540',bd=0, command=mixer.music.stop).place(x=30, y=500)

resume=PhotoImage(file='Resume.png')
Button(windows, image=resume,bg='#FEC540',bd=0, command=mixer.music.unpause).place(x=115, y=500)

pause=PhotoImage(file='Pause.png')
Button(windows, image=pause,bg='#FEC540',bd=0, command=mixer.music.pause).place(x=200, y=500)

# label to display title of selected music 
music_title = Label(windows, text='', font=('arial', 15), fg='white', bg='#FEC540')
music_title.place(x=310, y=300, anchor='center')

# music menu corner 
menu= PhotoImage(file='menu.png')
Label(windows, image=menu,bg='#FEC540').pack(padx=10, pady=50, side=RIGHT)

music_frame= Frame(windows, bd=2, relief=RIDGE)
music_frame.place(x=500, y=350, width=400, height=200)

Button(windows, text='Open folder', width=10, height=1, font=('arial', 10, 'bold'), fg='white', bg='#21b3de', command=open_folder).place(x=500, y=320)


# scroll bar 
scroll= Scrollbar(music_frame)
playlist= Listbox(music_frame, width=100, font=('arial',10), bg='#333333', fg='grey', selectbackground='lightblue', cursor='hand2', bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)



windows.mainloop()