from OpenGL.GL import *
from OpenGL import *
from PIL import Image
    
def load_texture(path, texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    # Set the texture wrapping parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    # Set texture filtering parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    # load image
    image = Image.open(path)
    # image = image.transpose(Image.FLIP_LEFT_RIGHT)
    img_data = image.convert("RGBA").tobytes()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return texture


skybox = [0]*6

def loadskybox():
  skybox[0] = load_texture("skybox/front.png",1)
  skybox[1] = load_texture("skybox/right.png",2)
  skybox[2] = load_texture("skybox/left.png",3)
  skybox[3] = load_texture("skybox/back.png",4)
  skybox[4] =   load_texture("skybox/top.png",5)
  skybox[5] = load_texture("skybox/bottom.png",6)

def drawskybox(size):
    b1 = glIsEnabled(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D,skybox[3])

    glColor3f(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3f(size/2,size/2,size/2)
    glTexCoord2f(1,0)
    glVertex3f(-size/2,size/2,size/2)
    glTexCoord2f(1,1)
    glVertex3f(-size/2,-size/2,size/2)
    glTexCoord2f(0,1)
    glVertex3f(size/2,-size/2,size/2)
    glEnd()

    glBindTexture(GL_TEXTURE_2D,skybox[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3f(-size/2,size/2,size/2)
    glTexCoord2f(1,0)
    glVertex3f(-size/2,size/2,-size/2)
    glTexCoord2f(1,1)
    glVertex3f(-size/2,-size/2,-size/2)
    glTexCoord2f(0,1)
    glVertex3f(-size/2,-size/2,size/2)
    glEnd()

    glBindTexture(GL_TEXTURE_2D,skybox[0])
    glBegin(GL_QUADS)
    glTexCoord2f(1,0)
    glVertex3f(size/2,size/2,-size/2)
    glTexCoord2f(0,0)
    glVertex3f(-size/2,size/2,-size/2)
    glTexCoord2f(0,1)
    glVertex3f(-size/2,-size/2,-size/2)
    glTexCoord2f(1,1)
    glVertex3f(size/2,-size/2,-size/2)
    glEnd()

    glBindTexture(GL_TEXTURE_2D,skybox[1])
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3f(size/2,size/2,-size/2)
    glTexCoord2f(1,0)
    glVertex3f(size/2,size/2,size/2)
    glTexCoord2f(1,1)
    glVertex3f(size/2,-size/2,size/2)
    glTexCoord2f(0,1)
    glVertex3f(size/2,-size/2,-size/2)
    glEnd()

    glBindTexture(GL_TEXTURE_2D,skybox[4])   
    glBegin(GL_QUADS)
    glTexCoord2f(1,0)
    glVertex3f(size/2,size/2,size/2)
    glTexCoord2f(0,0)
    glVertex3f(-size/2,size/2,size/2)
    glTexCoord2f(0,1)
    glVertex3f(-size/2,size/2,-size/2)
    glTexCoord2f(1,1)
    glVertex3f(size/2,size/2,-size/2)
    glEnd()

    glBindTexture(GL_TEXTURE_2D,skybox[5])      
    glBegin(GL_QUADS)
    glTexCoord2f(1,1)
    glVertex3f(size/2,-size/2,size/2)
    glTexCoord2f(0,1)
    glVertex3f(-size/2,-size/2,size/2)
    glTexCoord2f(0,0)
    glVertex3f(-size/2,-size/2,-size/2)
    glTexCoord2f(1,0)
    glVertex3f(size/2,-size/2,-size/2)
    glEnd()
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    if not b1: 
        glDisable(GL_TEXTURE_2D)



