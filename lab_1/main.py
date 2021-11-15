from tkinter import *
from dataclasses import dataclass
from typing import *
from enum import Enum
from action import Action
from drawing_commands import *
from moving_commands import *
from changing_commands import *
from delete_command import *
from app_context import AppContext
from mirror_command import *
from focus_commands import *
import uuid
import logging

logging.basicConfig(format="%(asctime)s %(filename)s:%(lineno)s %(name)s::%(funcName)s: %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
LOGGER = logging.getLogger("main")
    
APP_CONTEXT = AppContext()


     

class ActionType(Enum):
    SELECT = Action(add_to_selection, None, None)
    PENCIL = Action(create_line, on_line_drawing, line_drawing_complete )
    MOVE = Action(move_line, on_line_moving, line_moving_complete)
    CHANGE = Action(start_change_line, on_line_changing, line_changing_complete)
    DELETE = Action(delete_line, None, None)
    FOCUS = Action(focus_on_line, None, release_focus)
    MIRROR = Action(mirror_line, None, None)
    
def keyPressHandler(event):
    print(event.char, 'код =', event.keycode)


def mouseButton1PressHandler(event):
    if event.widget is APP_CONTEXT.canvas:
        if APP_CONTEXT.current_action and APP_CONTEXT.current_action.value.on_mouse_click:
           APP_CONTEXT.current_action.value.on_mouse_click(event, APP_CONTEXT)

def mouseButton1ReleaseHandler(event):
    if event.widget is APP_CONTEXT.canvas:
        if event.state == 256:
            if APP_CONTEXT.current_action and APP_CONTEXT.current_action.value.on_mouse_release:
                APP_CONTEXT.current_action.value.on_mouse_release(event, APP_CONTEXT)
                
def mouseMotionHandler(event):
    if event.widget is APP_CONTEXT.canvas:
        if event.state == 256:
            if APP_CONTEXT.current_action and APP_CONTEXT.current_action.value.on_mouse_move:
                APP_CONTEXT.current_action.value.on_mouse_move(event, APP_CONTEXT)
        APP_CONTEXT.status_bar.config(text=f"X: {event.x - APP_CONTEXT.canvas.winfo_width() / 2}, Y: {-(event.y - APP_CONTEXT.canvas.winfo_height()/ 2)}")

def shiftPressHandler(event):
    if APP_CONTEXT.current_action == ActionType.SELECT:
        APP_CONTEXT.current_action.value.on_mouse_click(event, APP_CONTEXT, True)

def backSpacePressed(event):
    if len(APP_CONTEXT.selected_widgets) != 0:
        for widget in APP_CONTEXT.selected_widgets:
            APP_CONTEXT.canvas.delete(widget.id)
            APP_CONTEXT.widgets.remove(find_in_set(widget.id, APP_CONTEXT.widgets))
        APP_CONTEXT.selected_widgets = []

def mPressed(event):
    if len(APP_CONTEXT.selected_widgets) != 0:
        for widget in APP_CONTEXT.selected_widgets:
            mirror_line(widget, APP_CONTEXT)

def rPressed(event):
    if len(APP_CONTEXT.selected_widgets) != 0:
        for widget in APP_CONTEXT.selected_widgets:
            rotate_line(widget, APP_CONTEXT)

def plusPressed(event):
    if len(APP_CONTEXT.selected_widgets) != 0:
        for widget in APP_CONTEXT.selected_widgets:
            increase_line(widget, APP_CONTEXT)

def minusPressed(event):
    if len(APP_CONTEXT.selected_widgets) != 0:
        for widget in APP_CONTEXT.selected_widgets:
            decrease_line(widget, APP_CONTEXT)

def actvate_mode(current_action: ActionType, cursor_type: str):
    APP_CONTEXT.canvas.config(cursor = cursor_type)
    APP_CONTEXT.current_action = current_action

if __name__=="__main__":
    tk = Tk()
    tk.resizable(0,0)
    
    APP_CONTEXT.canvas = Canvas(tk, bg = 'white', cursor = 'arrow')
    APP_CONTEXT.status_bar = Label(text="X: , Y: ")

    pencil_img = PhotoImage(file = r"pencil.png")
    move_img = PhotoImage(file = r"move.png")
    change_img = PhotoImage(file = r"change.png")
    group_img = PhotoImage(file = r"regular.png")
    delete_img = PhotoImage(file = r"delete.png")
    focus_img = PhotoImage(file=r"focus.png")
    mirror_img = PhotoImage(file=r"mirror.png")

    button_select = Button(image=group_img, width=100, height=100, command=lambda:actvate_mode(ActionType.SELECT, "hand2"))
    button_create = Button(image=pencil_img, width=100, height=100, command=lambda:actvate_mode(ActionType.PENCIL, "pencil"))
    button_move = Button(image=move_img, width=100, height=100, command=lambda:actvate_mode(ActionType.MOVE, "fleur"))
    button_change = Button(image=change_img, width=100, height=100, command=lambda:actvate_mode(ActionType.CHANGE , "sizing"))
    button_delete = Button(image=delete_img, width=100, height=100, command=lambda:actvate_mode(ActionType.DELETE , "X_cursor"))
    button_focus = Button(image=focus_img, width=100, height=100, command=lambda:actvate_mode(ActionType.FOCUS , "question_arrow"))
    button_mirror = Button(image= mirror_img, width=100, height=100, command=lambda:actvate_mode(ActionType.MIRROR , "target"))

    APP_CONTEXT.canvas["width"] = 700
    APP_CONTEXT.canvas["height"] = 600

    # APP_CONTEXT.canvas.bind("<KeyPress>", keyPressHandler)
    APP_CONTEXT.canvas.bind("<Motion>", mouseMotionHandler)
    APP_CONTEXT.canvas.bind("<Button-1>", mouseButton1PressHandler)
    APP_CONTEXT.canvas.bind("<ButtonRelease>", mouseButton1ReleaseHandler)
    APP_CONTEXT.canvas.bind("<Shift-1>", shiftPressHandler)
    tk.bind("m", mPressed)
    tk.bind("r", rPressed)
    tk.bind("-", minusPressed)
    tk.bind("=", plusPressed)
    tk.bind("<BackSpace>", backSpacePressed)

    APP_CONTEXT.canvas.pack()
    APP_CONTEXT.status_bar.pack(side=BOTTOM)
    button_select.pack(side=LEFT)
    button_change.pack(side=LEFT)    
    button_create.pack(side=LEFT)
    button_move.pack(side=LEFT)
    button_delete.pack(side=LEFT)
    button_focus.pack(side=LEFT)
    button_mirror.pack(side=LEFT)
    
    tk.mainloop()
