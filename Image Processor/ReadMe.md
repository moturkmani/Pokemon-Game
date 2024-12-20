# Pokemon Image Processor

A Python-based application to manage and process image files efficiently. This tool is designed for tasks such as renaming files, creating image variations, and generating silhouette versions of images. Built with a graphical user interface (GUI) powered by `tkinter`, the application simplifies image processing workflows.

---

## Features

1. **Remove Leading Numbers**
   - Renames files by removing leading numbers from filenames.
   
2. **Create Image Variations**
   - Generates black and not-black versions of each image in the folder.

3. **Generate Silhouettes**
   - Converts black images into silhouette versions.

4. **User-Friendly GUI**
   - Easily select and process image folders using buttons.

---

## Prerequisites

- Python 3.7 or higher
- Required libraries:
  - `tkinter`
  - `Pillow`

Install the dependencies using:
```bash
pip install pillow
```

---

## How to Use

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the script:
   ```bash
   python poke_img_processor.py
   ```

3. Select the desired option from the GUI menu:
   - **Name Change:** Remove leading numbers from filenames.
   - **Create Image Variation:** Generate black and not-black variations.
   - **Silhouette:** Create silhouette images from black variations.

4. Follow the prompts to select the folder containing the images.

---

## GUI Overview

- **Name Change**: Removes leading numbers from filenames.
- **Create Image Variation**: Adds variations of the selected images.
- **Silhouette**: Converts black variations into silhouette images.
- **Exit**: Closes the application.

---

## File Structure

- **poke_img_processor.py**: Main application script.

---

## Acknowledgments

- Built with love for simplifying image processing workflows.
- Powered by Python and `tkinter`.
- Shoutout to Slugiish_ for the image uploads on Reddit


