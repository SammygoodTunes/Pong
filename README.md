# Pong
Replica of the original Pong game

Explanation:
===================

First released in 1972 by Atari Inc. for the Arcade System, Pong is a very simple game consisting of two paddles and a ball.


You take control of the one of the two paddles, both opposite each other on the two sides of the screen. 


The aim is to hit the ball back at the opponent, by moving your paddle on the verticle axis. The opponent will equally send the ball back towards you if it collides with its paddle.


Here are the set of features:

1- If the ball goes too far off your side, your opponent will gain one point (right digit).


2- If the ball goes too far off your opponent's side, you'll gain one point (left digit).


3- The speed of the ball increases by .005 for every paddle hit, making it more difficult to hit it back towards each other the longer the ball doesn't fall too far off a side.


Controls:
===================

[Up/Down Arrow Keys] -> Move your paddle


[F11] -> Fullscreen


The two numbers above correspond to the player's points (left) and the opponent's points (right).


Installation information:
===================

A "requirements" text file is provided within the repository.


To install the necessary library(ies) to run the script:

1- Open CMD or GitBash


2- Change the current directory to the project path (cd path\\to\\project)


3- Install the library(ies) for the "requirements.txt" file (pip install -r requirements.txt)


Development information:
===================

Developed by: SammygoodTunes


Library(ies) used: Pygame 2.0.1