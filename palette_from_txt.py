########## Imports ##########
import pygame, sys

from pygame.locals import *
pygame.init()


########## Setup ##########
image = pygame.image.load("palette_from_image/palette.png") # change this to match where your image is at
image.set_colorkey((1,1,1))


########## RGB to HEX ##########
def rgb_to_hex(red, green, blue):
    return '{:02x}{:02x}{:02x}'.format(red, green, blue)


########## Run ##########
colors = []
true_colors = []
already_in = []

file = open("palette.txt", "w") # change this to ,atch where your palette txt file is

print(tuple(image.get_at((2,1))))
y = 0
for i in range(image.get_height()):
    x = 0
    for j in range(image.get_width()):
        colors.append(image.get_at((x, y)))
        x +=1
    y += 1

for color in colors:
    true_colors.append("FF" + rgb_to_hex(color[0], color[1], color[2]))

for color in true_colors:
    if color in already_in:
        continue
    else:
        file.write(color + "\n")
        already_in.append(color)

file.close()
pygame.quit()
sys.exit()
