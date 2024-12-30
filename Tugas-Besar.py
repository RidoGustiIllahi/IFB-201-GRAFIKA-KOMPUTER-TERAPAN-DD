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

def rotasi(points, center, angle):

    theta = np.radians(angle)

    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    rotation_matrix = np.array([
        [cos_theta, -sin_theta],
        [sin_theta, cos_theta]
    ])

    translated_points = np.array(points) - np.array(center)

    rotated_points = np.dot(translated_points, rotation_matrix.T)

    final_points = rotated_points + np.array(center)

    return final_points

def drawCircle(TitikTengah, radius, segments=360, color=(1.0, 1.0, 1.0)):
    x = TitikTengah[0]
    y = TitikTengah[1]
    glBegin(GL_POLYGON)
    glColor3f(*color)
    for i in range(segments):
        angle = 2.0 * np.pi * i / segments  
        x_offset = radius * np.cos(angle)
        y_offset = radius * np.sin(angle)
        glVertex2f(x + x_offset, y + y_offset)
    glEnd()

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
    
def drawOrang():
    TitikTengah = [187, -16]
    drawCircle(TitikTengah,14, 360, (0.0, 0.0, 1.0))

    Orang = [
        [183, -31],
        [197, -65],
        [213, -60],
        [199, -25],
        
        [183, -31],
        [176, -42],
        [179, -53],
        [188, -44],
        
        [176, -42],
        [179, -53],
        [162, -49],
        [162, -38],

        [199, -25],
        [204, -36],
        [213, -35],
        [218, -23],

        [213, -35],
        [218, -23],
        [228, -45],
        [221, -49],

        [173, -94],
        [182, -99],
        [200, -68],
        [192, -54],

        [199, -64],
        [207, -82],
        [217, -69],
        [213, -61],

        [217, -69],
        [207, -82],
        [236, -78],
        [236, -67]
    ]
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    for titik in Orang:
        glVertex2f(titik[0], titik[1])
    glEnd()

def drawKincir():
    TitikTengah = [325, -95]
    TitikTengah2 = refleksiSumbuY(TitikTengah)
    drawCircle(TitikTengah, 5, 360, (0.514, 0.361, 0.047))
    drawCircle(TitikTengah2, 5, 360, (0.514, 0.361, 0.047))

    Stick = [
        [324, -91],
        [326, -91],
        [326, -70],
        [324, -70]
    ]
    glBegin(GL_QUADS)
    glColor3f(0.514, 0.361, 0.047)
    for titik in Stick:
        glVertex2f(titik[0], titik[1])
    glEnd()

    Stick2 = []
    Stick2.extend(refleksiSumbuY(Stick))
    glBegin(GL_QUADS)
    glColor3f(0.514, 0.361, 0.047)
    for titik in Stick2:
        glVertex2f(titik[0], titik[1])
    glEnd()

    Baling =[
        [324, -70],
        [318, -80],
        [324, -90]
    ]
    Baling.extend(rotasi(Baling, [325, -70], 90))
    Baling.extend(rotasi(Baling, [325, -70], 180))
    Baling.extend(rotasi(Baling, [325, -70], 270))
    glBegin(GL_TRIANGLES)   
    glColor3f(1.0, 1.0, 0.0)
    for titik in Baling:
        glVertex2f(titik[0], titik[1])
    glEnd()    

    Baling2 = []
    Baling2.extend(refleksiSumbuY(Baling))
    glBegin(GL_TRIANGLES)   
    glColor3f(1.0, 1.0, 0.0)
    for titik in Baling2:
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
        drawOrang()
        drawKincir()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
