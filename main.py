# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	# initialize to start the game
	pygame.init()

	# Create groups to avoid manually calling methods
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	

	# Groups put into containers
	Player.containers = (updateable,drawable)
	Asteroid.containers = (asteroids,updateable,drawable)
	AsteroidField.containers = (updateable)
	asteroid_field = AsteroidField()

	# Generates the window
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	# Create time object used to help control FPS
	time = pygame.time.Clock()
	dt = 0



	# Set game loop condition
	while True:
		# Check if the user has closed the window and exit the game loop. Allows function
		# to close generated window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		# Each update action of player
		updateable.update(dt)

		screen.fill("black")

		# Draw player
		for object in drawable:
			object.draw(screen)

		# Method to refresh screen
		pygame.display.flip()

		# Return and set delta since .tick() was last called
		dt = time.tick(60)/1000

if __name__ == "__main__":
	main()
