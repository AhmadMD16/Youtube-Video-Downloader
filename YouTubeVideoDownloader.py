from pytube import YouTube
from tkinter import *
import tkinter as tk
from tkinter import messagebox

def download_video():
    video = YouTube(url.get())
    video = video.streams.get_highest_resolution()
    print(video.title)
    video.download(r'Directory')
    messagebox.showinfo("Success", "Video has been successfully downloaded")

master = tk.Tk()
master.geometry("450x100")
master.iconbitmap("YT.ico")
master.title("Youtube Video Downloader")
tk.Label(master, text="   URL:").grid(row=0)
url = tk.Entry(master)
url = Entry(master, width=60, borderwidth=5)
url.grid(row=0,column=0, columnspan=3, padx=10, pady=10)
url.grid(row=0, column=1)
tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=2, sticky=tk.W, pady=4)
tk.Button(master, text='Download', command=download_video).grid(row=4, column=3, sticky=tk.W, pady=4)

master.mainloop()

