from tkinter import *
from tkinter import HORIZONTAL
import numpy as np
from math import cos, sin, pi

alpha = 0
beta = 0

z = 100

def onScale1(val):
    z = scale_z.get()
    alpha1 = scale_alpha.get()
    beta1 = scale_beta.get()
    rotate = get_rotation_array(alpha1, beta1, z)

    some_bottom = BOTTOM.dot(rotate)
    some_top = TOP.dot(rotate)
    some_roof = ROOF.dot(rotate)

    some_bottom = normalize(some_bottom)
    some_top = normalize(some_top)
    some_roof = normalize(some_roof)
    draw_house(canvas, some_bottom, some_top, some_roof)
    

def onScale2(val):
    z = scale_z.get()
    alpha1 = scale_alpha.get()
    beta1 = scale_beta.get()
    rotate = get_rotation_array(alpha1, beta1, z)

    some_bottom = BOTTOM.dot(rotate)
    some_top = TOP.dot(rotate)
    some_roof = ROOF.dot(rotate)

    some_bottom = normalize(some_bottom)
    some_top = normalize(some_top)
    some_roof = normalize(some_roof)
    draw_house(canvas, some_bottom, some_top, some_roof)

def onScale3(val):
    z = scale_z.get()
    alpha1 = scale_alpha.get()
    beta1 = scale_beta.get()
    rotate = get_rotation_array(alpha1, beta1, z)

    some_bottom = BOTTOM.dot(rotate)
    some_top = TOP.dot(rotate)
    some_roof = ROOF.dot(rotate)

    some_bottom = normalize(some_bottom)
    some_top = normalize(some_top)
    some_roof = normalize(some_roof)
    draw_house(canvas, some_bottom, some_top, some_roof)


tk = Tk()
tk.resizable(0,0)
canvas = Canvas(tk, bg = 'white', cursor = 'arrow')

scale_alpha = Scale(from_=-180, to=180, command=onScale1, orient=HORIZONTAL)
scale_beta = Scale(from_=-180, to=180, command=onScale2, orient=HORIZONTAL)
scale_z = Scale(from_=180, to=500, command=onScale3, orient=HORIZONTAL)




BOTTOM = np.array([[0,0,0,1], #a
          [100,0,0,1], #b
          [100,0,100,1], #c
          [0,0,100,1]]) #d
TOP = np.array([[0,100,0,1], #e
       [100,100,0,1], #f
       [100,100,100,1], #g
       [0,100,100,1]]) #h

ROOF = np.array([[50, -50, 0,1], #i
        [50, -50, 100,1]]) #e

def draw_house(canvas, bottom, top, roof):
    canvas.delete("all")
    #bottom
    canvas.create_line(bottom[0][0]+250, bottom[0][1]+250, bottom[1][0]+250, bottom[1][1]+250) #AB
    canvas.create_line(bottom[0][0]+250, bottom[0][1]+250, bottom[3][0]+250, bottom[3][1]+250) #AD
    canvas.create_line(bottom[1][0]+250, bottom[1][1]+250, bottom[2][0]+250, bottom[2][1]+250) #BC
    canvas.create_line(bottom[2][0]+250, bottom[2][1]+250, bottom[3][0]+250, bottom[3][1]+250) #DC
    #top-bottom connection
    canvas.create_line(bottom[0][0]+250, bottom[0][1]+250, top[0][0]+250, top[0][1]+250) #AE
    canvas.create_line(bottom[3][0]+250, bottom[3][1]+250, top[3][0]+250, top[3][1]+250) #DH
    canvas.create_line(bottom[1][0]+250, bottom[1][1]+250, top[1][0]+250, top[1][1]+250) #BF
    canvas.create_line(bottom[2][0]+250, bottom[2][1]+250, top[2][0]+250, top[2][1]+250) #CG
    #TOP
    canvas.create_line(top[0][0]+250, top[0][1]+250, top[1][0]+250, top[1][1]+250) 
    canvas.create_line(top[0][0]+250, top[0][1]+250, top[3][0]+250, top[3][1]+250) #
    canvas.create_line(top[1][0]+250, top[1][1]+250, top[2][0]+250, top[2][1]+250) #
    canvas.create_line(top[2][0]+250, top[2][1]+250, top[3][0]+250, top[3][1]+250) #
    #roof
    canvas.create_line(bottom[1][0]+250, bottom[1][1]+250, roof[0][0]+250, roof[0][1]+250)
    canvas.create_line(bottom[0][0]+250, bottom[0][1]+250, roof[0][0]+250, roof[0][1]+250)
    
    canvas.create_line(roof[1][0]+250, roof[1][1]+250, roof[0][0]+250, roof[0][1]+250) #JI

    canvas.create_line(roof[1][0]+250, roof[1][1]+250, bottom[2][0]+250, bottom[2][1]+250)
    canvas.create_line(roof[1][0]+250, roof[1][1]+250, bottom[3][0]+250, bottom[3][1]+250)



def normalize(some_array):
    for i in range(len(some_array)):
        div = some_array[i][3]
        for j in range(len(some_array[i])):
            some_array[i][j] /= div
    return some_array


def get_rotation_array(alpha, beta, z):
    alpha = (alpha * pi) /180 #f
    beta = (beta * pi) / 180 #t
    cos_a = cos(alpha)
    cos_b = cos(beta)
    sin_a = sin(alpha)
    sin_b = sin(beta)
    rotate_array = np.array([[cos_a, sin_a*sin_b,0, sin_a*cos_b/z],
                            [0,cos_b,0, -sin_b/z],
                            [sin_a, - cos_a*sin_b,0, -cos_a*cos_b/z],
                            [0,0,0, 1]])
    return rotate_array



if __name__ == "__main__":


    canvas["width"] = 500
    canvas["height"] = 500
    label_alpha = Label(text="alpha")
    label_beta = Label(text="beta")
    label_z = Label(text="z")
    
    #draw_house(canvas, BOTTOM, TOP, ROOF)

    canvas.pack()
    label_alpha.pack()
    scale_alpha.pack()
    label_beta.pack()
    scale_beta.pack()
    label_z.pack()
    scale_z.pack()


    print(BOTTOM)

    tk.mainloop()