# Automated Dino Game with Eye Blink Detection

This project is an automatic Dino game that uses eye blinking to make the Dino jump. It leverages the built-in Dino game from Google Chrome and utilizes Python for detecting eye blinks using the webcam.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Overview

The Automated Dino Game detects eye blinks through your webcam and makes the Dino jump in the Chrome Dino game. This project uses Python and several libraries, including OpenCV, PyAutoGUI, and MediaPipe, to achieve this functionality.

## Features

- **Eye Blink Detection**: Uses the webcam to detect eye blinks and triggers a jump in the Dino game.
- **Real-time Processing**: Processes video frames in real-time to detect eye blinks.
- **Simple Setup**: Easy to set up and run with minimal dependencies.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux systems.
- **Hands-Free Control**: Allows users to play the game without using the keyboard or mouse, providing an innovative and accessible way to interact with the game.
- **Lightweight**: Designed to be lightweight with minimal resource consumption.
- **Customization**: Easily configurable thresholds for blink detection to suit different users' needs.
- **Visual Feedback**: Provides visual feedback through the webcam feed, showing detected facial landmarks and blink status.
- **Open Source**: The project is open-source, allowing users to contribute and customize the functionality as needed.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system. You can download it from [here](https://www.python.org/downloads/).
- Google Chrome installed to play the built-in Dino game.
- Webcam to capture real-time video feed.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/dpshah23/AutoMatic-Dyno-Game-Using-Eye-Blinking.git
   cd automated-dino-game
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS and Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Open the Google Chrome Dino game by typing `chrome://dino` in the address bar.

2. Run the Python script:
   ```sh
   python main.py
   ```

3. Allow the webcam access if prompted. The script will start capturing video from your webcam.

4. When you blink your eyes, the Dino will jump in the game.

