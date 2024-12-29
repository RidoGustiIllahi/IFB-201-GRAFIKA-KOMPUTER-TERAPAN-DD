import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def refleksiSumbuY(objek):
    matrixA = np.array(objek)
    matrixB = np.array([
        [-1, 0],
        [0, 1]
    ])

    return (matrixA @ matrixB).tolist()

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

    GarisPinggir = [
        [8, 360],
        [6, 360],
        [160, -360],
        [140, -360],
        [-8, 360],
        [-6, 360],
        [-160, -360],
        [-140, -360]
    ]
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    for titik in GarisPinggir:
        glVertex2f(titik[0], titik[1])
    glEnd()

    GarisTengah = [
        [15, -260],
        [-15, -260],
        [-18, -360],
        [18, -360],
        [9, 60],
        [-9, 60],
        [-12, -60],
        [12, -60],
        [3, 280],
        [-3, 280],
        [-6, 200],
        [6, 200]
    ]
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    for titik in GarisTengah:
        glVertex2f(titik[0], titik[1])
    glEnd()

def drawPohon():
    PohonDaun = [
        [280, -220],
        [240, -160],
        [200, -220],
        [280, -190],
        [240, -140],
        [200, -190],
        
        [160, 50],
        [140, 80],
        [120, 50],
        [160, 60],
        [140, 90],
        [120, 60],
        
        [75, 280],
        [60, 300],
        [45, 280],
        [75, 290],
        [60, 305],
        [45, 290],
    ]
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)
    for titik in PohonDaun:
        glVertex2f(titik[0], titik[1])
    glEnd()

    PohonBatang = [
        [250, -220],
        [230, -220],
        [230, -260],
        [250, -260],

        [145, 30],
        [135, 30],
        [135, 50],
        [145, 50],
        
        [65, 280],
        [55, 280],
        [55, 270],
        [65, 270]
    ]
    glBegin(GL_QUADS)
    glColor3f(0.5882, 0.3882, 0.2784)
    for titik in PohonBatang:
        glVertex2f(titik[0], titik[1])
    glEnd()

    PohonDaunRefleksi = refleksiSumbuY(PohonDaun)
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)
    for titik in PohonDaunRefleksi:
        glVertex2f(titik[0], titik[1])
    glEnd()

    PohonBatangRefleksi = refleksiSumbuY(PohonBatang)
    glBegin(GL_QUADS)
    glColor3f(0.5882, 0.3882, 0.2784)
    for titik in PohonBatangRefleksi:
        glVertex2f(titik[0], titik[1])
    glEnd()

def drawMobil():
    MobilBody = [
        [-10, 360],
        [10, 360],
        [10, 354],
        [-10, 354],
        
        [-12, 354],
        [12, 354],
        [12, 345],
        [-12, 345],

        [-11, 345],
        [-9, 345],
        [-9, 341],
        [-11, 341],
        
        [11, 345],
        [9, 345],
        [9, 341],
        [11, 341],

        [-14, 352],
        [-12, 352],
        [-12, 350],
        [-14, 350],
        
        [14, 352],
        [12, 352],
        [12, 350],
        [14, 350],
    ]
    glBegin(GL_QUADS)
    glColor3f(0.502, 0.0, 0.0)
    for titik in MobilBody:
        glVertex2f(titik[0], titik[1])
    glEnd()

    MobilKaca =[
        [-8, 358],
        [8, 358],
        [8, 355],
        [-8, 355],

        [-10,349],
        [-8,349],
        [-8,348],
        [-10,348],
        
        [10,349],
        [8,349],
        [8,348],
        [10,348],

        [-5, 347],
        [5, 347],
        [5, 346],
        [-5, 346]
    ]
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    for titik in MobilKaca:
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
        drawPohon()
        drawMobil()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
