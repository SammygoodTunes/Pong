# Pong
Replica of the original Pong game

## Explanation:

First released in 1972 by Atari Inc. for the Arcade System, Pong is a very simple game consisting of two paddles and a ball.


You take control of one of the two paddles, both opposite each other on the two sides of the screen. 


The aim is to hit the ball back at the opponent, by moving your paddle on the verticle axis. The opponent will equally send the ball back towards you if it collides with its paddle.


Here are the set of features:

- If the ball goes too far off your side, your opponent will gain one point (right digit).


- If the ball goes too far off your opponent's side, you'll gain one point (left digit).


- The speed of the ball increases by .005 for every paddle hit, making it more difficult to hit it back towards each other the longer the ball doesn't fall too far off a side.


## Controls:

- [**Up/Down Arrow Keys**] -> Move your paddle


- [**Space**] -> Enable 2-player mode


- [**Keypad 8/2**] -> Move second paddle, when 2-player mode is enabled


- [**F11**] -> Fullscreen


- [**Escape**] -> Pause game


The two numbers above correspond to the player's points (left) and the opponent's points (right).


## Installation information:

A "requirements" text file is provided within the repository.

### To install the necessary library(ies) to run the script:

1- Open CMD/Git Bash/Terminal

2- Change the current directory to the project path (cd path\\to\\project)

3- Install the library(ies) from the "requirements.txt" file:
  ```
  pip install -r requirements.txt
  ```

### To install the game without necessary libraries:

1- Locate the installation file "Pong-X.X-Installer.exe"

2- Launch the installation file and follow the steps within the UI of the installer

3- The installation file should have extracted all the necessary resources including the EXE file, that you can run without needing Python or any of the libraries used during development


## Development information:

Developed by: SammygoodTunes

Library(ies) used: Pygame 2.0.1
