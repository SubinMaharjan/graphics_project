import pygame
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
class OBJ:
    def __init__(self, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.load_obj(filename)
    def load_obj(self,filename,swapyz=False):
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.group_index = [0]
        white = [0.8,0.8,0.8]
        black = [0.1,0.1,0.1]
        red = [0.5,0.0,0.1]
        blue = [0.11,0.13,0.61]
        steel_blue = [0.1,0.0,0.3]
        color = {0:white,7923:black,10137:black,12789:red,13122:black,13142:red,13289:black,13309:black,22069:black,27621:blue,28802:blue,29352:blue,31676:black,31714:blue,
        32895:blue,35561:blue,37220:black,37392:steel_blue,48318:blue}
        material = None
        mat = set()

        for line in open(filename, "r"):
            
            values = line.split()
            if not values: continue
            # start
            if len(values) ==1 : continue
            if (values[0] == '#' and values[1] == 'object'):
                grp_index = len(self.faces)-1
                self.group_index.append(grp_index)
            #end
            
            if values[0] == 'v':
                v = list(map(float, values[1:4]))
                v = [val/25 for val in v]
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = list(map(float, values[1:4]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] == 'vt':
                self.texcoords.append(list(map(float, values[1:3])))
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
                mat.add(material)

            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords, material))

        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)
        # print(self.group_index)

        for i,face in enumerate(self.faces):
            if i in color.keys():
                glColor3f(*color[i])
                
            vertices, normals, texture_coords, material = face
 
            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
                if texture_coords[i] > 0:
                    glTexCoord2fv(self.texcoords[texture_coords[i] - 1])
                # print(*(self.vertices[vertices[i] - 1]))
                glVertex3fv(self.vertices[vertices[i] - 1])

            glEnd()

        # print(mat)
        glDisable(GL_TEXTURE_2D)
        glEndList()