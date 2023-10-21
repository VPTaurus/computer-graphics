import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Initialize Pygame
pygame.init()

# Set the window size and create a window
width, height = 800, 600
display = (width, height)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Set up the initial camera position
glTranslatef(0.0, 0.0, -5)

# Set up the perspective projection
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glFrustum(-1, 1, -1, 1, 1, 50.0)
glMatrixMode(GL_MODELVIEW)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the letter "P" and "M" using lines
    glColor(1.0, 1.0, 1.0)

    # Draw "P"
    glBegin(GL_LINES)
    glVertex3f(-3.0, 2.5, 0.0)
    glVertex3f(-3.0, -2.5, 0.0)

    glVertex3f(-3.0, 2.5, 0.0)
    glVertex3f(-1.0, 2.5, 0.0)

    glVertex3f(-1.0, 2.5, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)

    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(-2.0, 0.0, 0.0)

    glVertex3f(-2.0, 0.0, 0.0)
    glVertex3f(-2.0, -2.5, 0.0)

    glVertex3f(-2.0, -2.5, 0.0)
    glVertex3f(-3.0, -2.5, 0.0)
    glEnd()
    # Draw "P inner"
    glBegin(GL_LINES)
    glVertex3f(-2.5, 2.0, 0.0)
    glVertex3f(-1.5, 2.0, 0.0)

    glVertex3f(-1.5, 2.0, 0.0)
    glVertex3f(-1.5, 0.5, 0.0)

    glVertex3f(-1.5, 0.5, 0.0)
    glVertex3f(-2.5, 0.5, 0.0)

    glVertex3f(-2.5, 0.5, 0.0)
    glVertex3f(-2.5, 2.0, 0.0)

    glEnd()

    # Draw "M"
    glBegin(GL_LINES)
    glVertex3f(0.5, 2.5, 0.0)
    glVertex3f(0.0, -2.5, 0.0)

    glVertex3f(0.5, 2.5, 0.0)
    glVertex3f(1.0, 2.5, 0.0)
    
    glVertex3f(1.0, 2.5, 0.0)
    glVertex3f(1.5, -0.4, 0.0)
    
    glVertex3f(1.5, -0.4, 0.0)
    glVertex3f(2.0, 2.5, 0.0)

    glVertex3f(2.0, 2.5, 0.0)
    glVertex3f(2.5, 2.5, 0.0)

    glVertex3f(2.5, 2.5, 0.0)
    glVertex3f(3.0, -2.5, 0.0)
    
    glVertex3f(3.0, -2.5, 0.0)
    glVertex3f(2.5, -2.5, 0.0)

    glVertex3f(2.5, -2.5, 0.0)
    glVertex3f(2.2, 0.5, 0.0)

    glVertex3f(2.2, 0.5, 0.0)
    glVertex3f(1.5, -2.0, 0.0)

    glVertex3f(1.5, -2.0, 0.0)
    glVertex3f(0.8, 0.5, 0.0)

    glVertex3f(0.8, 0.5, 0.0)
    glVertex3f(0.5, -2.5, 0.0)

    glVertex3f(0.5, -2.5, 0.0)
    glVertex3f(0.0, -2.5, 0.0)
    glEnd()
    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)
