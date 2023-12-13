# AI_GAME_GENERATION

## Abstract
The 2D Racing Game Development project aimed to create an engaging and entertaining racing game using the Pygame library in Python. The game features a player-controlled car navigating through a dynamically generated map, avoiding traffic, and reaching checkpoints. The project integrates various game development concepts, including sprite animation, collision detection, and user input handling.
Objectives
* Game Development: Create a 2D racing game with smooth gameplay and visually appealing graphics.
* Player Interaction: Implement responsive controls for the player to accelerate, decelerate, and steer the car.
* Dynamic Map Generation: Develop a system for generating random and diverse racing tracks for increased replayability.
* AI Traffic System: Integrate an AI-controlled traffic system with realistic movement patterns for added challenge.
* Checkpoint System: Implement a checkpoint system to track the player's progress and provide a sense of achievement.
* Scoring Mechanism: Design a scoring system based on the player's performance, including penalties for collisions.
 
## Technologies Used
* Python: The primary programming language for game development.
* Pygame Library: A cross-platform set of Python modules designed for writing video games.
* Git: Version control system for collaborative development and code management.
* PyCharm: Integrated Development Environment (IDE) used for coding and debugging.
Project Structure
The project is organized into several modules:

* 	Main Game Logic (main.py)

Initializes the game window, sets up the main game loop, and handles user input.
Manages the game state, including the player's car, AI traffic, checkpoints, and tracks.
Implements collision detection and scoring mechanisms.
*	Player (player.py)
 
Defines the player-controlled car class.
Handles player input for acceleration, steering, and deceleration.
Manages car movement, rotation, and collision responses.
*	Traffic (traffic.py)

Implements AI-controlled traffic cars with dynamic movement and turning behaviors.
Generates random road tiles for diverse track layouts.
Handles traffic-related logic such as turning, splitting, and crossing.
*	Camera (camera.py)

Manages the in-game camera to follow the player's car.
Sets the camera position based on the player's coordinates.
*	Tracks (tracks.py)

Creates and renders tire tracks left by the player's car.
*	Direction Indicator (direction.py)

Displays an arrow indicating the direction towards the next checkpoint.
*	Game Modes (gamemode.py)

Defines game modes such as the finish line, scoring, and penalties.
*	Loader (loader.py)

Loads images and resources used in the game.
*	Maps (maps.py)

Contains tilemaps for generating random tracks with different road tile types.
*	Timeout (timeout.py)

Manages the timeout alert displayed when the game timer reaches zero.
*	Bounds (bounds.py)

Implements an alert for displaying when the player is close to the track bounds.
*	Menu (menu.py)

Displays alerts and menus for the game.


Challenges Faced
Sprite Animation: Implementing smooth sprite animations for player and AI cars.
Dynamic Map Generation: Creating an algorithm for generating random yet playable tracks.
Collision Detection: Ensuring accurate collision detection for player traffic and player-checkpoint interactions.
AI Traffic Behavior: Developing realistic and challenging AI traffic movement patterns.
Game State Management: Handling different game states, including menus, gameplay, and alerts.

Future Enhancements
Multiplayer Mode: Introduce multiplayer functionality for competitive gameplay.
Advanced AI: Implement more sophisticated AI algorithms for traffic with adaptive behavior.
Upgrades and Power-Ups: Introduce upgrades and power-ups to enhance player capabilities.
Level Editor: Develop a level editor for users to create and share custom tracks.
Sound Effects and Music: Enhance the gaming experience with immersive audio elements.

1.	Game Initialization (main.py)
2.	
import pygame
from player import Player
from traffic import Traffic
from tracks import Tracks
from camera import Camera
from gamemode import GameMode

pygame.init()

# Initialize game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Racing Game")

# Create game objects
player = Player()
traffic = Traffic()
tracks = Tracks()
camera = Camera(screen_width, screen_height)
game_mode = GameMode()

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    player.update()
    traffic.update()
    tracks.update(player.position)
    camera.update(player)

    # Render game objects
    screen.fill((255, 255, 255))  # Clear screen
    tracks.render(screen, camera)
    player.render(screen, camera)
    traffic.render(screen, camera)

    pygame.display.flip()
    clock.tick(60)  # Set FPS

pygame.quit()

2. Player Class (player.py)
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.speed = 5
        self.position = [screen_width // 2, screen_height // 2]

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed
        self.rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * self.speed
        self.position = [self.rect.x, self.rect.y]

    def render(self, screen, camera):
        screen.blit(self.image, camera.apply(self))

3.	Traffic Class (traffic.py)
4.	import pygame

class Traffic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Initialization similar to Player class

    def update(self):
        pass


                   **Running Environment**
                   
![results](https://github.com/gurpreetsingh1111/AI_GAME_GENERATION/assets/84591513/904b2fa2-8f04-45b9-9196-54c2ea302cb0)




#**Conclusion**
The 2D Racing Game Development project successfully created an entertaining racing game with various features, including dynamic map generation, AI traffic, and scoring mechanisms. The project provided valuable insights into game development concepts, challenges, and opportunities for future enhancements. The game serves as a foundation for further improvements and additions to create a more polished and engaging gaming experience.
