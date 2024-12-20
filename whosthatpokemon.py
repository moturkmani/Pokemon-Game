import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class WhosThatPokemonGame:
    def __init__(self, root):
        self.root = root
        self.folder_path = None
        self.image_files = []
        self.asked_images = set()
        self.current_image_index = None
        self.current_image_black = None
        self.current_image_notblack = None
        self.current_image_name = None
        self.waiting_for_next_image = False

        # Set up GUI
        self.root.title("Who's That Pokémon?")
        self.center_window(600, 750)

        # Main Frame to remove extra spacing
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.canvas = tk.Canvas(self.main_frame, width=500, height=500, bg="white", highlightthickness=2, highlightbackground="black")
        self.canvas.pack(pady=20)

        self.name_label = tk.Label(self.main_frame, text="", font=("Arial", 24, "bold"), fg="black", bg="white")
        self.name_label.pack()

        self.open_folder_button = tk.Button(self.main_frame, text="Open Folder Location", command=self.open_folder)
        self.open_folder_button.pack()

        self.start_button = tk.Button(self.main_frame, text="Start Game", command=self.start_game, state=tk.DISABLED)
        self.start_button.pack()

        self.exit_button = tk.Button(self.main_frame, text="Exit Game", command=self.exit_game)
        self.restart_button = tk.Button(self.main_frame, text="Restart Game", command=self.restart_game)

        self.root.bind("<space>", self.handle_keypress)
        self.root.bind("<Return>", self.handle_keypress)

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def open_folder(self):
        self.folder_path = filedialog.askdirectory(title="Select Folder with Images")
        if self.folder_path:
            self.image_files = self.load_images()
            if self.image_files:
                self.start_button.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Error", "No valid image pairs found in the selected folder!")

    def load_images(self):
        # Load pairs of images (_black and _notblack)
        files = os.listdir(self.folder_path)
        black_images = [f for f in files if f.endswith("_black.png")]
        notblack_images = [f for f in files if f.endswith("_notblack.png")]
        
        image_pairs = []
        for black in black_images:
            counterpart = black.replace("_black", "_notblack")
            if counterpart in notblack_images:
                image_pairs.append((black, counterpart))

        return image_pairs

    def start_game(self):
        self.open_folder_button.pack_forget()
        self.start_button.pack_forget()
        self.restart_button.pack()
        self.exit_button.pack()
        self.next_image()

    def restart_game(self):
        self.asked_images.clear()
        self.start_game()

    def exit_game(self):
        self.root.quit()

    def next_image(self):
        if len(self.asked_images) == len(self.image_files):
            self.asked_images.clear()

        remaining_images = [i for i in range(len(self.image_files)) if i not in self.asked_images]
        if not remaining_images:
            messagebox.showinfo("Game Over", "No more images to display!")
            self.root.quit()

        self.current_image_index = random.choice(remaining_images)
        self.asked_images.add(self.current_image_index)

        black_image, notblack_image = self.image_files[self.current_image_index]
        
        self.current_image_black = self.resize_image(os.path.join(self.folder_path, black_image))
        self.current_image_notblack = self.resize_image(os.path.join(self.folder_path, notblack_image))
        
        self.current_image_name = black_image.replace("_black.png", "")

        self.canvas.delete("all")
        self.name_label.config(text="")
        self.canvas.create_image(250, 250, image=self.current_image_black)
        self.waiting_for_next_image = False

    def show_color_image(self):
        self.canvas.delete("all")

        # Use the already resized and processed `self.current_image_notblack`
        self.canvas.create_image(250, 250, image=self.current_image_notblack)
        self.name_label.config(text=self.current_image_name)

        # Keep a reference to avoid garbage collection
        self.current_image_notblack_tk = self.current_image_notblack
        self.waiting_for_next_image = True

    def handle_keypress(self, event):
        if self.waiting_for_next_image:
            self.next_image()
        else:
            self.show_color_image()

    def resize_image(self, image_path):
        image = Image.open(image_path)
        image.thumbnail((500, 500))
        return ImageTk.PhotoImage(image)

if __name__ == "__main__":
    root = tk.Tk()
    game = WhosThatPokemonGame(root)
    root.mainloop()
