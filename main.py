'''
Title: Pong
Author: SammygoodTunes
Version: 1.0
'''

import pygame, random, math

pygame.mixer.pre_init(44100, -16, 4, 1024)
pygame.init()

class Window:

	def __init__(self, width=750, height=500, fullscreen=False):
		self.width, self.height = width, height
		self.screen = pygame.display.set_mode([self.width, self.height])
		self.fullscreen=False
		self.clock = pygame.time.Clock()


	def set_fullscreen(self, fullscreen):
		self.fullscreen = fullscreen
		if self.fullscreen:
			self.screen = pygame.display.set_mode([self.width, self.height], pygame.FULLSCREEN)
		else:
			self.screen = pygame.display.set_mode([self.width, self.height])


	def get_width(self):
		return self.width


	def get_height(self):
		return self.height


	def get_fullscreen(self):
		return self.fullscreen


	def clear(self):
		self.screen.fill((0, 0, 0), (0, 0, self.width, self.height))


class Game:

	def __init__(self, end=False):
		self.end = end


	def exit(self):
		self.end = True


class Ball:

	def __init__(self, pos=(0, 0), speed=3, angle=0, adder=0.05):
		self.pos = pos
		self.width, self.height = 10, 10
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
		self.speed = speed
		self.adder = adder
		self.angle = angle
		self.max_angle = 2 * math.pi / 12
		self.velocity = (self.speed * math.cos(self.angle), self.speed * -math.sin(self.angle))

	def draw(self):
		pygame.draw.rect(win.screen, (255,255,255), self.rect)

	def update(self):
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)


	def set_pos(self, x, y):
		self.pos = (x, y)

	def set_speed(self, speed):
		self.speed = speed


	def set_angle(self, angle):
		self.angle = angle


	def set_velocity(self, velocity):
		self.velocity = velocity


	def invert_velocity_x(self, velocity):
		print("before",self.velocity)
		self.velocity = (-velocity[0], velocity[1])
		print("after",self.velocity)


	def invert_velocity_y(self, velocity):
		self.velocity = (velocity[0], -velocity[1])

	
	def get_pos(self):
		return self.pos


	def get_width(self):
		return self.width


	def get_height(self):
		return self.height


	def get_speed(self):
		return self.speed


	def get_adder(self):
		return self.adder


	def get_angle(self):
		return self.angle


	def get_max_angle(self):
		return self.max_angle


	def get_velocity(self):
		return self.velocity


class Player:

	def __init__(self, pos=(0, 0), speed=10, up=False, down=False):
		self.pos = pos
		self.width, self.height = 20, 75
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
		self.speed = speed
		self.score = 0
		self.up, self.down = up, down


	def draw(self):
		pygame.draw.rect(win.screen, (255,255,255), self.rect)


	def update(self):
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)


	def set_up(self, up):
		self.up = up

	
	def set_down(self, down):
		self.down = down

	
	def set_pos(self, x, y):
		self.pos = (x, y)


	def set_score(self, score):
		self.score = score


	def get_up(self):
		return self.up


	def get_down(self):
		return self.down

	
	def get_pos(self):
		return self.pos


	def get_score(self):
		return self.score


	def get_speed(self):
		return self.speed


	def get_width(self):
		return self.width


	def get_height(self):
		return self.height
	

class Enemy:

	def __init__(self, pos=(0, 0), speed=10):
		self.pos = pos
		self.width, self.height = 20, 75
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
		self.speed = speed
		self.score = 0

	
	def draw(self):
		pygame.draw.rect(win.screen, (255,255,255), self.rect)

	def update(self):
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)


	def set_pos(self, x, y):
		self.pos = (x, y)

	def set_score(self, score):
		self.score = score


	def get_pos(self):
		return self.pos


	def get_score(self):
		return self.score


	def get_speed(self):
		return self.speed


	def get_width(self):
		return self.width


	def get_height(self):
		return self.height


class Gui:
	def __init__(self):
		self.numbers = [pygame.image.load("src/"+str(i)+".png") for i in range(10)]


pygame.display.set_caption("Pong")

win = Window()
game, ball, player, enemy, gui = Game(), Ball((win.get_width() / 2, win.get_height() / 2), 3, 0, 0.005), Player((0, win.get_height()/2), 8, False, False), Enemy((win.get_width()-20, win.get_height()/2), 8), Gui()

#only used to store and restore original value
speed = ball.get_speed()

def main():
	while not game.end:
		win.clear()
		player.draw()
		enemy.draw()
		ball.draw()

		player.update()
		enemy.update()
		ball.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player.set_up(True)

				if event.key == pygame.K_DOWN:
					player.set_down(True)

				if event.key == pygame.K_F11:
					if win.get_fullscreen():
						win.set_fullscreen(False)
					else:
						win.set_fullscreen(True)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					player.set_up(False)

				if event.key == pygame.K_DOWN:
					player.set_down(False)


		#move ball
		ball.set_pos(ball.get_pos()[0] + ball.get_velocity()[0] * ball.get_speed(), ball.get_pos()[1] + ball.get_velocity()[1] * ball.get_speed())

		#move enemy
		if ball.get_pos()[0] > win.get_width() / 2:
			if ball.get_pos()[1] > enemy.get_pos()[1] + (enemy.get_height() / 2) + (enemy.get_height() / 4):
				enemy.set_pos(enemy.get_pos()[0], enemy.get_pos()[1] + enemy.get_speed())
			elif ball.get_pos()[1] < enemy.get_pos()[1] + (enemy.get_height() / 2) - (enemy.get_height() / 4):
				enemy.set_pos(enemy.get_pos()[0], enemy.get_pos()[1] - enemy.get_speed())

		#enemy bounds
		if enemy.get_pos()[1] > win.get_height() - enemy.get_height():
			enemy.set_pos(enemy.get_pos()[0], win.get_height() - enemy.get_height())
		elif enemy.get_pos()[1] < 0:
			enemy.set_pos(enemy.get_pos()[0], 0)


		#player paddle collision
		if ball.get_pos()[0] > player.get_pos()[0] and ball.get_pos()[0] < player.get_pos()[0] + player.get_width() + ball.get_speed():
			if ball.get_pos()[1] > player.get_pos()[1] - ball.get_speed() - 8 and ball.get_pos()[1] < player.get_pos()[1] + player.get_height() + ball.get_speed():
				ball.set_angle(((player.get_pos()[1] + (player.get_height() / 2) - ball.get_pos()[1]) / (player.get_height() / 2)) * ball.get_max_angle())
				ball.set_velocity((ball.get_speed() * math.cos(ball.get_angle()), ball.get_speed() * -math.sin(ball.get_angle())))
				ball.set_pos(player.get_pos()[0] + player.get_width() + ball.get_speed(), ball.get_pos()[1])
				ball.set_speed(ball.get_speed() + ball.get_adder())
				pygame.mixer.Channel(0).play(pygame.mixer.Sound('src/paddle.wav'))
				print(ball.get_velocity())

		#enemy paddle collision
		if ball.get_pos()[0] > enemy.get_pos()[0] and ball.get_pos()[0] < enemy.get_pos()[0] + enemy.get_width() + ball.get_speed():
			if ball.get_pos()[1] > enemy.get_pos()[1] - ball.get_speed() - 8 and ball.get_pos()[1] < enemy.get_pos()[1] + enemy.get_height() + ball.get_speed():
				ball.set_angle(((enemy.get_pos()[1] + (enemy.get_height() / 2) - ball.get_pos()[1]) / (enemy.get_height() / 2)) * ball.get_max_angle())
				ball.set_velocity((ball.get_speed() * math.cos(ball.get_angle()), ball.get_speed() * -math.sin(ball.get_angle())))
				ball.invert_velocity_x(ball.get_velocity())
				ball.set_pos(enemy.get_pos()[0] - ball.get_speed(), ball.get_pos()[1])
				ball.set_speed(ball.get_speed() + ball.get_adder())
				pygame.mixer.Channel(0).play(pygame.mixer.Sound('src/paddle.wav'))


		#top wall collision
		if ball.get_pos()[1] < 0:
			ball.set_pos(ball.get_pos()[0], 0)
			ball.invert_velocity_y(ball.get_velocity())
			pygame.mixer.Channel(0).play(pygame.mixer.Sound('src/hit.wav'))

		#bottom wall collision
		if ball.get_pos()[1] > win.get_height() - ball.get_height():
			ball.set_pos(ball.get_pos()[0], win.get_height() - ball.get_height())
			ball.invert_velocity_y(ball.get_velocity())
			pygame.mixer.Channel(0).play(pygame.mixer.Sound('src/hit.wav'))


		#lose
		if ball.get_pos()[0] < -8:
			ball.set_pos(win.get_width() / 2, win.get_height() / 2)
			ball.set_speed(speed)
			ball.set_angle(random.randint(45, 50))
			ball.set_velocity((ball.get_speed() * math.cos(ball.get_angle()), ball.get_speed() * -math.sin(ball.get_angle())))
			enemy.set_score(enemy.get_score() + 1)
			pygame.mixer.Channel(0).play(pygame.mixer.Sound('src/lose.wav'))

		#win
		if ball.get_pos()[0] > win.get_width() + 8:
			ball.set_pos(win.get_width() / 2, win.get_height() / 2)
			ball.set_speed(speed)
			ball.set_angle(random.randint(45, 50))
			ball.set_velocity((ball.get_speed() * math.cos(ball.get_angle()), ball.get_speed() * -math.sin(ball.get_angle())))
			player.set_score(player.get_score() + 1)
			pygame.mixer.Channel(0).play(pygame.mixer.Sound('src/win.wav'))


		#player up movement
		if player.get_up():
			if player.get_pos()[1] <= 0:
				player.set_pos(player.get_pos()[0], 0)
			else:
				player.set_pos(player.get_pos()[0], player.get_pos()[1] - player.get_speed())

		#player down movement
		if player.get_down():
			if player.get_pos()[1] >= win.get_height() - player.get_height():
				player.set_pos(player.get_pos()[0], win.get_height() - player.get_height())
			else:
				player.set_pos(player.get_pos()[0], player.get_pos()[1] + player.get_speed())


		#display score
		for i in range(len(str(player.score))):
			w = win.get_width() / 2 - 32 + (i * 13)
			h = 10
			for j in range(10):
				if str(player.score)[i] == str(j):
					win.screen.blit(gui.numbers[j], (w, h, 32, 32))

		for i in range(len(str(enemy.score))):
			w = win.get_width() / 2 + 32 + (i * 13)
			h = 10
			for j in range(10):
				if str(enemy.score)[i] == str(j):
					win.screen.blit(gui.numbers[j], (w, h, 32, 32))


		win.clock.tick(60)
		pygame.display.flip()
	pygame.quit()


if __name__ == '__main__':
	main()