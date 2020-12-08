import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from TextureLoader import loadskybox, drawskybox
from PIL import Image

 
# IMPORT OBJECT LOADER
from loader import *

def skybox_render(tx,ty,zpos,rx,ry):
    glPushMatrix()
    # glTranslate(tx/20., ty/20., - zpos)
    glTranslate(0., 0 , - zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)
    drawskybox(500)
    glPopMatrix()


def object_render(obj,tx,ty,zpos,rx,ry):
    
    glPushMatrix()
    # glTranslate(tx/20., ty/20., - zpos)
    # gluLookAt(0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)
    glTranslate(tx/20.,(ty/20.)-3,-zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)
    glCallList(obj.gl_list)
    glPopMatrix()


def main(): 
    pygame.init()
    viewport = (800,600)

    srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    
    glClearColor(0.25, 0.25, 0.25, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    
    glLightfv(GL_LIGHT0, GL_POSITION,  (-80, 500, 200, 1.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.3, 0.3, 0.3, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.35, 0.35, 0.35, 1.0))

    glMaterialfv(GL_FRONT, GL_AMBIENT,[0.1745, 0.0, 0.1, 0.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE,[0.1, 0.0, 0.6, 0.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR,[0.7, 0.6, 0.8, 0.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 80)
    
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)           

    # LOAD OBJECT AFTER PYGAME INIT

    obj = OBJ("Audi.obj", swapyz=True)
    loadskybox()
    
    
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    width, height = viewport
    gluPerspective(90.0, width/float(height), 1, 500)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10.0, 10.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)
    
    rx, ry = (0,0)
    tx, ty = (0,0)
    rox,roy = (0,0)

    zpos = 5
    rotate_object = move = False
    rotate_skybox = False
    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    tx += -2
                if e.key == pygame.K_RIGHT:
                    tx += 2
                if e.key == pygame.K_UP:
                    ty += 2
                if e.key == pygame.K_DOWN:
                    ty += -2
                if e.key == pygame.K_d:
                    rx += 30
                if e.key == pygame.K_a:
                    rx += -30
                if e.key == pygame.K_w:
                    ry += 30
                if e.key == pygame.K_s:
                    ry += -30
                if e.key == pygame.K_r:
                    main()
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 4: zpos = max(1, zpos-1)
                elif e.button == 5: zpos += 1
                elif e.button == 1: rotate_object = True
                elif e.button == 3: rotate_skybox = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1: rotate_object = False
                elif e.button == 3: rotate_skybox = False
            elif e.type == MOUSEMOTION:
                i, j = e.rel
                if rotate_object:
                    rx += i
                    ry += j
                if rotate_skybox:
                    rox += i
                    roy += j
                if move:
                    tx += i
                    ty -= j
        

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        # RENDER OBJECT
        skybox_render(tx,ty,zpos,rox,roy)
        # glTranslate(tx/20., ty/20., - zpos)
        # glRotate(ry, 1, 0, 0)
        # glRotate(rx, 0, 1, 0)
        object_render(obj,tx,ty,zpos,rx,ry)
        
        pygame.display.flip()

main()