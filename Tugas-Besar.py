import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

def drawJalan():
    Jalan = [
        [10, 360],
        [-10, 360],
        [-180, -360],
        [180, -360]
    ]
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    for titik in Jalan:
        glVertex2f(titik[0], titik[1])
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(720, 720, "2D Object Transformation", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-360, 360, -360, 360)
    glMatrixMode(GL_MODELVIEW)

    while not glfw.window_should_close(window):
        glClearColor(0.133, 0.694, 0.298, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        drawJalan()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
