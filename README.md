# Snake

Snake game in Python

<img src="images/snake_1.png" width="400">

## Purpose

The purpose of this project is create a version of the game Snake in Python

## Background

Snake is a video game concept in which the player moves around a line (the snake) which grows in length

## Gameplay

The player controls the snake's head on a screen by using up, down, left, and right arrow keys. At the start of the game, the head of the snake is centered in the screen. A piece of purple food is randomly placed on the screen. The player moves the snake to the food to grow the snake in length. When a piece of food is consumed, the snake's body increases by 1 block, and the score is increased. 

As the snake's head moves forward, its body follows. The player loses when the snake runs into the screen border or itself.

## Built With

* [Python](https://www.python.org/) 3.7
* [Pygame](https://www.pygame.org/) 2.0.1

## Usage

### Install Requirements

* Install pygame
```
$ pip install pygame 2.0.1
```

### Run Script

* Run snake.py to run the game

```
$ python snake.py
```

A pygame window with the title ‘SNAKE’ should pop up. The snake starts as a green block of size 1. Press the up, down, left, or right arrow key to begin moving the snake. Once the snake is moving, it cannot be stopped. Direct the snake to the purple block, which is the food. 

### Virtual Env
```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python3 snake.py
```

## Author

**Laura Kocubinski** [laurakoco](https://github.com/laurakoco)

## Acknowledgments

* Boston University MET Master of Science Computer Science Program
* MET CS 521 Information Structures in Python

## References

[1] https://www.edureka.co/blog/snake-game-with-pygame/
