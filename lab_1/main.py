from tkinter import *
from dataclasses import dataclass
from typing import *
from enum import Enum
from action import Action
from drawing_commands import *
from moving_commands import *
from changing_commands import *
from app_context import AppContext
import uuid
import logging

logging.basicConfig(format="%(asctime)s %(filename)s:%(lineno)s %(name)s::%(funcName)s: %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
LOGGER = logging.getLogger("main")
    
APP_CONTEXT = AppContext()

class ActionType(Enum):
    PENCIL = Action(create_line, on_line_drawing, line_drawing_complete )
    MOVE = Action(move_line, on_line_moving, line_moving_complete)
    CHANGE = Action(change_line, on_line_changing, line_changing_complete)
    
def keyPressHandler(event):
    print(event.char, 'код =', event.keycode)


def mouseButton1PressHandler(event):
    if event.widget is APP_CONTEXT.canvas:
        if APP_CONTEXT.current_action:
           APP_CONTEXT.current_action.value.on_mouse_click(event, APP_CONTEXT)

def mouseButton1ReleaseHandler(event):
    if event.widget is APP_CONTEXT.canvas:
        if event.state == 256:
            if APP_CONTEXT.current_action:
                APP_CONTEXT.current_action.value.on_mouse_release(event, APP_CONTEXT) 

def mouseMotionHandler(event):
    if event.widget is APP_CONTEXT.canvas:
        if event.state == 256:
            if APP_CONTEXT.current_action:
                APP_CONTEXT.current_action.value.on_mouse_move(event, APP_CONTEXT)

def actvate_mode(current_action: ActionType, cursor_type: str):
    APP_CONTEXT.canvas.config(cursor = cursor_type)
    APP_CONTEXT.current_action = current_action

if __name__=="__main__":
    tk = Tk()
    tk.resizable(0,0)
    
    APP_CONTEXT.canvas = Canvas(tk, bg = 'white', cursor = 'arrow')
    pencil_img = PhotoImage(file = r"pencil.png")
    move_img = PhotoImage(file = r"move.png")
    change_img = PhotoImage(file = r"regular.png")

    button_create = Button(image=pencil_img, width=100, height=100, command=lambda:actvate_mode(ActionType.PENCIL, "pencil"))
    # button_create['command'] = lambda: APP_CONTEXT.current_mode = Actions.PENCIL


    button_move = Button(image=move_img, width=100, height=100, command=lambda:actvate_mode(ActionType.MOVE, "fleur"))
    # button_create['command'] = lambda: APP_CONTEXT.current_mode = Actions.MOVE 

    button_change = Button(image=change_img, width=100, height=100, command=lambda:actvate_mode(ActionType.CHANGE , "sizing"))

    APP_CONTEXT.canvas["width"] = 600
    APP_CONTEXT.canvas["height"] = 600

    APP_CONTEXT.canvas.bind("<KeyPress>", keyPressHandler)
    APP_CONTEXT.canvas.bind("<Motion>", mouseMotionHandler)
    APP_CONTEXT.canvas.bind("<Button-1>", mouseButton1PressHandler)
    APP_CONTEXT.canvas.bind("<ButtonRelease>", mouseButton1ReleaseHandler)

    APP_CONTEXT.canvas.pack()
    button_change.pack(side=LEFT)    
    button_create.pack(side=LEFT)
    button_move.pack(side=LEFT)
    
    

    tk.mainloop()
