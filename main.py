from tkinter import *
from tkinter import messagebox

class App:
  def __init__(self):
    self.window = Tk()
    self.window.geometry('400x250+500+50')
    self.window.title('YT Downloader')
    self.window.resizable(0,0)

    # Variables

    self.entry_text = StringVar()

    # Frames

    self.frame_header = Label(self.window, bg="brown", height=6)
    self.frame_header.pack(fill=X)

    # Labels

    self.label_logo = Label(self.frame_header, text='Download your favorite songs! 🎶')
    self.label_logo.place(x=10, y=20)
    self.label_logo.config(font= ("Impact",20), foreground= "white", background="brown")

    self.label_link = Label(self.window, text="Enter a link:")
    self.label_link.config(font=("Tahoma", 15))
    self.label_link.place(x=150, y=120)

    # Entry

    self.entry_link = Entry(self.window, textvariable=self.entry_text, width=30)
    self.entry_link.config(font=("Arial",10))
    self.entry_link.place(x=90, y=165)

    # Button

    self.btn_download = Button(self.window, text='Download', command= lambda: self.download(self.entry_link.get()))
    self.btn_download.config(background="red", foreground="white", borderwidth=0, font="Arial 12 bold", pady=2, padx=2, )
    self.btn_download.place(x=155, y=200)

    self.window.mainloop()

  def saveMP3(self, file):
    import os
    
    base, ext = os.path.splitext(file)
    new_file = base + ".mp3"
    os.rename(file, new_file)

  def download(self, link):
    from pytube import YouTube
    from pathlib import Path
    downloads_path = str(Path.home() / "Downloads")
    
    youtube_object= YouTube(link)
    youtube_object= youtube_object.streams.get_audio_only()

    try:
      out_audio = youtube_object.download(output_path=downloads_path)
      self.saveMP3(out_audio)
      self.entry_text.set("")
      messagebox.showinfo("Info", "Download completed!")
    except:
      messagebox.showinfo("Info", "There's been an error downloading the audio")

if __name__ == '__main__':
  app = App()