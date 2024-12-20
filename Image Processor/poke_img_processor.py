import os
import shutil
from tkinter import Tk, filedialog, messagebox, Button, Frame
from PIL import Image

def remove_leading_numbers_from_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                new_name = ' '.join(filename.split(' ')[1:]) if ' ' in filename else filename
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
        messagebox.showinfo("Success", "All files have been renamed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def create_image_variations(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if not os.path.isfile(file_path):
                continue
            name, ext = os.path.splitext(filename)
            if not ext:
                continue
            black_name = f"{name}_black{ext}"
            notblack_name = f"{name}_notblack{ext}"
            black_path = os.path.join(folder_path, black_name)
            notblack_path = os.path.join(folder_path, notblack_name)
            os.rename(file_path, black_path)
            shutil.copy(black_path, notblack_path)
        messagebox.showinfo("Success", "Images processed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def create_silhouette(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if not os.path.isfile(file_path) or '_black' not in filename:
                continue
            with Image.open(file_path) as img:
                img = img.convert("RGBA")
                silhouette = Image.new("RGBA", img.size, (255, 255, 255, 255))
                for y in range(img.height):
                    for x in range(img.width):
                        r, g, b, a = img.getpixel((x, y))
                        if a > 0:
                            silhouette.putpixel((x, y), (0, 0, 0, 255))
                silhouette.save(file_path)
        messagebox.showinfo("Success", "Silhouettes created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_folder_and_process(process_function):
    folder_path = filedialog.askdirectory(title="Select Folder with Images")
    if folder_path:
        process_function(folder_path)
    main_menu()

def main_menu():
    for widget in root.winfo_children():
        widget.destroy()
    Button(root, text="Name Change", command=lambda: select_folder_and_process(remove_leading_numbers_from_files), width=30, height=2, bg="lightblue", fg="black").pack(pady=10)
    Button(root, text="Create Image Variation", command=lambda: select_folder_and_process(create_image_variations), width=30, height=2, bg="lightgreen", fg="black").pack(pady=10)
    Button(root, text="Silhouette", command=lambda: select_folder_and_process(create_silhouette), width=30, height=2, bg="lightcoral", fg="black").pack(pady=10)
    Button(root, text="Exit", command=root.destroy, width=30, height=2, bg="gray", fg="white").pack(pady=10)

if __name__ == "__main__":
    root = Tk()
    root.title("Pokemon Image Processor")
    root.geometry("400x300")
    root.resizable(False, False)

    # Center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 400
    window_height = 300
    position_top = (screen_height // 2) - (window_height // 2)
    position_right = (screen_width // 2) - (window_width // 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    main_menu()
    root.mainloop()
