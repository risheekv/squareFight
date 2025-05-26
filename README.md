# Square AI Game

![Square AI Game screen](https://raw.githubusercontent.com/techn0man1ac/simpleAIGame/main/imgs/screen0.png)

# Overview
This is a simple game developed using Pygame, where the red square (controlled by an AI) tries to escape from the black square (controlled by the player). The AI believes the player is an enemy and uses four commands - left, right, up, down - to flee from it.

# Video demonstration

https://youtube.com/shorts/unALV4uoLmQ

# Features
- Player control using the arrow keys
- AI-driven enemy movement using Ollama's Llama model
- Basic collision detection
- Simple and clear game loop with Pygame

# Requirements
- Python 3.x https://www.python.org/downloads/
- Pygame https://pypi.org/project/pygame/
- AI powered by Ollama's Python API https://github.com/ollama/ollama-python
- Meta Llama 3(large language model) https://github.com/meta-llama/llama3

# Game Mechanics

![Work job gif](https://raw.githubusercontent.com/techn0man1ac/simpleAIGame/main/imgs/gameMechanics.gif)

The player controls a black square using the arrow keys.
The red square (enemy) moves based on the AI model's response to the player's position.
If the player catches the enemy, a "Game Over" message is displayed, and the game exits after a short delay.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgements
- Developed by Serhii Trush
- Pygame - For the game library
- Ollama - For the AI model and API
- ChatGPT - For helping with code and documentation
