# Who's That Pokémon?

A fun and interactive game that challenges players to guess Pokémon silhouettes! Built using Python and `tkinter`, this game displays silhouettes of Pokémon images, allowing players to reveal the color version by pressing a key.

---

## Features

1. **Image-Based Gameplay**:
   - Displays silhouette (_black) images and their colored (_notblack) counterparts.

2. **Keyboard Interaction**:
   - Press **Space** or **Enter** to reveal the colored version of the silhouette.

3. **Automatic Image Pairing**:
   - Automatically detects valid `_black` and `_notblack` image pairs from a folder.

4. **User-Friendly GUI**:
   - Simple interface for loading folders, starting the game, and interacting with the content.

5. **Restart and Exit Options**:
   - Easily restart the game or exit via buttons.

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
   python whosthatpokemon.py
   ```

3. Select the folder containing image pairs:
   - Ensure the folder includes valid `_black` and `_notblack` image pairs.

4. Follow the prompts:
   - Use **Space** or **Enter** to reveal the colored image.
   - Continue through the images until all have been displayed.

---

## File Requirements

- Images should be named as pairs:
  - `example_black.png` (silhouette image)
  - `example_notblack.png` (colored image)

- Place all images in a single folder before starting the game.

---

## GUI Overview

- **Open Folder Location**: Select the folder containing the Pokémon images.
- **Start Game**: Begin the game with the selected images.
- **Restart Game**: Reset the game and start over.
- **Exit Game**: Close the application.

---

## Acknowledgments

- Inspired by the "Who's That Pokémon?" game from the Pokémon anime.
- Built for my tiktok live events and fans of interactive guessing games.
- MoCards4Free.com to see my live event schedules to join and win some cards for free :)

