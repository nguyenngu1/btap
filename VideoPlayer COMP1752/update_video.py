import tkinter as tk
from tkinter import messagebox
import video_library as lib

class UpdateRatingWidget:
    def __init__(self, master):
        self.master = master
        self.master.title("Update Video Rating")
        
        self.label_video_number = tk.Label(self.master, text="Enter video number:")
        self.label_video_number.grid(row=0, column=0, padx=5, pady=5)
        
        self.entry_video_number = tk.Entry(self.master)
        self.entry_video_number.grid(row=0, column=1, padx=5, pady=5)
        
        self.label_new_rating = tk.Label(self.master, text="Enter new rating:")
        self.label_new_rating.grid(row=1, column=0, padx=5, pady=5)
        
        self.entry_new_rating = tk.Entry(self.master)
        self.entry_new_rating.grid(row=1, column=1, padx=5, pady=5)
        
        self.update_button = tk.Button(self.master, text="Update Rating", command=self.update_rating)
        self.update_button.grid(row=2, columnspan=2, padx=5, pady=5)

    def update_rating(self):
            video_number = str(self.entry_video_number.get())
            new_rating = int(self.entry_new_rating.get())
            if 1<= int(new_rating) <= 5:
               result = lib.set_rating(video_number, new_rating)
               messagebox.showinfo("Success", "Rating updated successfully.")
            else:
                messagebox.showerror("Error", "only 1 to 5.")
                
    


def update_video_rating(video_number, new_rating):
    try:
        video_name = lib.get_name(video_number)
        if video_name:
            lib.update_rating(video_number, new_rating)
            play_count = lib.get_play_count(video_name)
            return f"Video Name: {video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}"
        else:
            return "Error: Invalid video number."
    except KeyError:
        return "Error: Invalid video number."

def main():
    root = tk.Tk()
    app = UpdateRatingWidget(root)
    root.mainloop()

if __name__ == "__main__":
    main()
