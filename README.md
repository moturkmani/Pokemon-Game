<div align="center">

# ❓ Who's That Pokémon?

**A fun, interactive guessing game built with Python and Tkinter.** 🎮

Silhouettes flash on screen — hit a key to reveal the colored Pokémon underneath!

</div>

---

## ✨ Features

| | |
|---|---|
| 🖼️ **Image-Based Gameplay** | Displays silhouette (`_black`) images and their colored (`_notblack`) counterparts |
| ⌨️ **Keyboard Interaction** | Press **Space** or **Enter** to reveal the colored version of the silhouette |
| 🔗 **Automatic Image Pairing** | Automatically detects valid `_black` and `_notblack` image pairs from a folder |
| 🖱️ **User-Friendly GUI** | Simple interface for loading folders, starting the game, and interacting with the content |
| 🔁 **Restart and Exit Options** | Easily restart the game or exit via buttons |

---

## 🚀 Getting Started

### Prerequisites

- 🐍 Python 3.7 or higher
- Required libraries:
  - `tkinter`
  - `Pillow`

Install the dependencies:
```bash
pip install pillow
```

### Installation & Run

1. **Clone the repo**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Run it**
   ```bash
   python whosthatpokemon.py
   ```

3. **Select the folder** containing your image pairs 📁
   - Ensure the folder includes valid `_black` and `_notblack` image pairs

4. **Play!** 🎉
   - Use **Space** or **Enter** to reveal the colored image
   - Continue through the images until all have been displayed

---

## 🗂️ File Requirements

Images should be named as pairs:

| File | Description |
|---|---|
| `example_black.png` | 🕶️ Silhouette image |
| `example_notblack.png` | 🌈 Colored image |

> Place all images in a single folder before starting the game.

---

## 🖥️ GUI Overview

| Button | Description |
|---|---|
| 📂 **Open Folder Location** | Select the folder containing the Pokémon images |
| ▶️ **Start Game** | Begin the game with the selected images |
| 🔁 **Restart Game** | Reset the game and start over |
| 🚪 **Exit Game** | Close the application |

---

## 🙏 Acknowledgments

- Inspired by the **"Who's That Pokémon?"** segment from the Pokémon anime 📺
- Built for my TikTok live events and fans of interactive guessing games 🎥
- Visit **MoCards4Free.com** to see my live event schedules — join and win some cards for free! 🎁
