import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex3f(0.0, 1.0, 0.0)
    gl.glVertex3f(-1.0, -1.0, 0.0)
    gl.glVertex3f(1.0, -1.0, 0.0)
    gl.glEnd()
    glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_RGBA | glut.GLUT_DOUBLE | glut.GLUT_DEPTH)
glut.glutInitWindowSize(640, 480)
glut.glutCreateWindow(b'OpenGL Window')
glut.glutDisplayFunc(display)
glut.glutMainLoop()
