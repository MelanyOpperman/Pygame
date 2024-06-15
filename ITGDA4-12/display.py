#Importing needed libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cube import Cube
from pyramid import Pyramid
from prism import Prism

#Initializing Pygame
pygame.init()

#Setting up display
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

#Setting up perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

#Initializing objects
cube = Cube()
pyramid = Pyramid()
prism = Prism()
objects = [cube, pyramid, prism]
current_object = 0

#Variables to track mouse movement and button state
dragging = False
prev_mouse_pos = (0, 0)

#Function to draw the current object
def draw_current_object():
    global objects, current_object
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clearing the screen and depth buffer
    objects[current_object].draw()  # Drawing the current object
    pygame.display.flip()  # Updating the display

#Function to rotate the object
def rotate_obj(axis, angle):
    glRotatef(angle, *axis)

#Function to scale the object
def scale_obj(scale_factor):
    glScalef(scale_factor, scale_factor, scale_factor)

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the quit event is triggered, then it will exit
            pygame.quit()
            quit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Right mouse button down
            dragging = True
            prev_mouse_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:  # Right mouse button up
            dragging = False
        elif event.type == pygame.KEYDOWN:  # Key down event
            if event.key == pygame.K_RETURN:  # Switching object on Enter press
                current_object = (current_object + 1) % len(objects)
            elif event.key == pygame.K_i:  # Translating object on x-axis positive
                glTranslatef(0.1, 0, 0)
            elif event.key == pygame.K_k:  # Translating object on x-axis negative
                glTranslatef(-0.1, 0, 0)
            elif event.key == pygame.K_j:  # Translating object on y-axis positive
                glTranslatef(0, 0.1, 0)
            elif event.key == pygame.K_l:  # Translating object on y-axis negative
                glTranslatef(0, -0.1, 0)
            elif event.key == pygame.K_u:  # Translating object on z-axis positive
                glTranslatef(0, 0, 0.1)
            elif event.key == pygame.K_o:  # Translating object on z-axis negative
                glTranslatef(0, 0, -0.1)
            elif event.key == pygame.K_UP:  # Rotating object on x-axis positive
                rotate_obj((1, 0, 0), 1)
            elif event.key == pygame.K_DOWN:  # Rotating object on x-axis negative
                rotate_obj((1, 0, 0), -1)
            elif event.key == pygame.K_LEFT:  # Rotating object on y-axis positive
                rotate_obj((0, 1, 0), 1)
            elif event.key == pygame.K_RIGHT:  # Rotating object on y-axis negative
                rotate_obj((0, 1, 0), -1)
            elif event.key == pygame.K_PAGEUP:  # Rotating object on z-axis positive
                rotate_obj((0, 0, 1), 1)
            elif event.key == pygame.K_PAGEDOWN:  # Rotating object on z-axis negative
                rotate_obj((0, 0, 1), -1)
            elif event.key == pygame.K_1:  # Scaling object down
                scale_obj(0.9)
            elif event.key == pygame.K_2:  # Scaling object up
                scale_obj(1.1)
            elif event.key == pygame.K_3:  # Scaling object down
                scale_obj(0.9)
            elif event.key == pygame.K_4:  # Scaling object up
                scale_obj(1.1)
            elif event.key == pygame.K_5:  # Scaling object down
                scale_obj(0.9)
            elif event.key == pygame.K_6:  # Scaling object up
                scale_obj(1.1)

    if dragging:
        # Getting the current mouse position and calculate movement since last frame
        cur_mouse_pos = pygame.mouse.get_pos()
        dx, dy = cur_mouse_pos[0] - prev_mouse_pos[0], cur_mouse_pos[1] - prev_mouse_pos[1]
        # Updating perspective based on mouse movement
        glRotatef(0.5 * dx, 0, 1, 0)
        glRotatef(0.5 * dy, 1, 0, 0)
        prev_mouse_pos = cur_mouse_pos

    draw_current_object()  # Drawing the current object
    pygame.time.wait(10)  # Waiting for 10 milliseconds to control the frame rate
