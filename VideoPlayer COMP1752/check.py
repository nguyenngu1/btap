import tkinter as tk
from tkinter import messagebox
import video_library as lib
playlist = []
class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Playlist")
        self.video_names = {key: lib.get_name(key) for key in lib.library.keys()}
        
      
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter number of videos")
        self.label.grid(row=0, column=0, padx=5, pady=5)
        
        self.entry = tk.Entry(self.master)
        self.entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.add_button = tk.Button(self.master, text="Add playlist", command=self.add_to_playlist)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)
        
        self.text_area = tk.Text(self.master, height=10, width=30)
        self.text_area.grid(row=1, columnspan=3, padx=5, pady=5)
        
        self.play_button = tk.Button(self.master, text="Play playlist", command=self.play_playlist)
        self.play_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.reset_button = tk.Button(self.master, text="Reset playlist", command=self.reset_playlist)
        self.reset_button.grid(row=2, column=1, padx=5, pady=5)
    
    def add_to_playlist(self):
        try:
            video_number = self.entry.get()
            video_name = self.video_names.get(video_number)
            self.entry.delete(0, tk.END)
            if video_name:
                playlist.append(video_name)
                self.update_playlist_display()
            else:
                messagebox.showerror("Error", "There is not a valid video number")
        except ValueError:
            messagebox.showerror("Error", "Please enter a video number")
    
    def update_playlist_display(self):
        self.text_area.delete('1.0', tk.END)
        for video_name in playlist:
            self.text_area.insert(tk.END, f"{video_name}\n")
    
    def play_playlist(self):
        for video_name in playlist:
            print(playlist)
            lib.increment_play_count(video_name)
            
    def get_play_count(key):
        try:
            item = lib[key]
            return item.play_count
        except KeyError:
            return -1
    def reset_playlist(self):
     playlist.clear()
     self.text_area.delete('1.0', tk.END)
    def increment_play_count(key):
        try: 
            item = lib[key]
            item.play_count += 1
            print(item.play_count)
        except KeyError:
            return
def main():
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
