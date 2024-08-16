# Kitty Asteroid

**Kitty Asteroid** is an arcade-style game built with Pygame where players control a spaceship piloted by a cat. The goal is to avoid and destroy incoming meteors by shooting lasers while trying to achieve the highest possible score. The game ends if a meteor collides with the spaceship.

## Features

- **Ship Control**: Move the spaceship by following the mouse cursor.
- **Laser Shooting**: Shoot lasers by clicking the mouse to destroy meteors.
- **Meteor Spawning**: Randomly generated meteors that vary in size and speed.
- **Collision Detection**: Game ends if the spaceship collides with a meteor.
- **Score Tracking**: Keep track of your score, which is based on survival time.

## Installation

1. Ensure you have Python installed. If not, you can download it [here](https://www.python.org/downloads/).

2. Install the Pygame library if you don't have it already:

    ```bash
    pip install pygame
    ```

3. Clone the repository:

    ```bash
    git clone https://github.com/wagnergabe/kitty-asteroid.git
    ```

4. Navigate to the project directory:

    ```bash
    cd kitty-asteroid
    ```

5. Run the game:

    ```bash
    python main.py
    ```

## How to Play

- **Movement**: Control the spaceship using your mouse. The spaceship will follow the cursor's position.
- **Shooting**: Left-click to shoot lasers upwards to destroy meteors.
- **Objective**: Avoid getting hit by the meteors and survive as long as possible to increase your score.
- **Score**: The score is based on how long you can survive, with the time displayed on the screen.

## Game Mechanics

### Classes

- **`Ship`**: Controls the spaceship's movement, shooting mechanics, and collision detection.
- **`Laser`**: Manages laser movement, collision with meteors, and removal when off-screen.
- **`Meteor`**: Handles meteor spawning, random size, speed, rotation, and collision with lasers or the spaceship.
- **`Score`**: Displays the current score based on time survived.

### Sprite Groups

- **`spaceship_group`**: A single sprite group for the spaceship.
- **`laser_group`**: A group to manage all active lasers.
- **`meteor_group`**: A group to manage all incoming meteors.

## Assets

- **Graphics**: All images (ship, lasers, meteors, background) are located in the `./graphics` directory.
- **Font**: Custom font `subatomic.ttf` used for displaying the score.

## Development

Feel free to fork the repository and contribute to the development of the game. Any improvements or new features are welcome!

## License

This project is licensed under the MIT License.
