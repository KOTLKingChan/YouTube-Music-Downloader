import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from pytube import YouTube

class YouTubeDownloaderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YouTube Music Downloader")

        # Create widgets
        self.label_url = tk.Label(self.root, text="Enter YouTube URL:")
        #self.entry_url = tk.Entry(self.root, width=40)
        self.entry_url = tk.scrolledtext.ScrolledText(self.root, width=40, height=3)
        self.button_download = tk.Button(self.root, text="Download", command=self.download_video)
        self.label_status = tk.Label(self.root, text="")

        # Grid layout
        self.label_url.grid(row=0, column=0, padx=10, pady=10)
        self.entry_url.grid(row=0, column=1, padx=10, pady=10)
        self.button_download.grid(row=1, column=0, columnspan=2)
        self.label_status.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


    def download_video(self):
        urls = [url.strip() for url in self.entry_url.get("1.0",'end-1c').splitlines()]

        # Ask user for download location
        destination = filedialog.askdirectory(title="Select download location")
        if not destination:
            self.label_status.config(text="Download canceled.")
            return
        
        for url in urls:
            try:
                yt = YouTube(url)
                #media = yt.streams.get_highest_resolution().filter(only_audio=True)
                media = yt.streams.filter(only_audio=True).first()

                out_file = media.download(output_path=destination)

                # Rename the file
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                self.label_status.config(text=f"Downloaded: {new_file}")
                print(f"Downloaded: {new_file}")
            except Exception as e:
                self.label_status.config(text=f"Error downloading {url}: {str(e)}")
        
        self.label_status.config(text=f"Download completed.")
        print(f"Download completed")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = YouTubeDownloaderApp()
    app.run()
