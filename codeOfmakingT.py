from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def DrawLine(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def ddaDashed(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    xIncre = 4 * (dx / float(steps))
    yIncre = dy / float(steps)
    x = x1
    y = y1
    for i in range(int(steps / 4)):
        DrawLine(round(x), round(y))
        x += xIncre
        y += yIncre



def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    xInc = dx / float(steps)
    yInc = dy / float(steps)
    x = x1
    y = y1
    for i in range(steps):
        DrawLine(round(x), round(y))
        x += xInc
        y += yInc

def DrawtheT():
    ddaDashed(110, 310, 210, 310)
    dda(160, 310, 160, 210)


def iterate():
    glViewport(0,0,600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500,0.0,1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    DrawtheT()
    glFlush()
    iterate()
    glColor3f(1.0, 0.5, 0.3)


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"DDA")


glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()