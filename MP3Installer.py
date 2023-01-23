import tkinter as tk
import youtube_dl
from tkinter import filedialog

class App:
    def __init__(self, master):
        self.master = master
        self.initUI()

    def initUI(self):
        self.master.configure(bg='black')
        self.master.title("Made by JavaUpdated")

        self.label = tk.Label(self.master, text="Welcome to Youtube MP3 Download:", fg='white', bg='black')
        self.label.pack()

        self.entry = tk.Entry(self.master, fg='white', bg='black')
        self.entry.pack()

        self.folder_button = tk.Button(self.master, text="Set Folder", command=self.selectFolder, fg='white', bg='black')
        self.folder_button.pack()

        self.download_button = tk.Button(self.master, text="Install!", command=self.download, fg='white', bg='black')
        self.download_button.pack()

        # Set default folder path
        self.folder_path = 'C:\\Users\\toddynho\\Desktop\\PenDriveBackup'

    def selectFolder(self):
        self.folder_path = filedialog.askdirectory()

    def download(self):
        ydl_opts = {
            'outtmpl': self.folder_path + '/%(title)s.mp3',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'default_search': 'hi'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([self.entry.get()])
            except Exception as e:
                print(e)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
