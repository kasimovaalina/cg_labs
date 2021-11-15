import logging
from os import curdir
from tkinter import *
from typing import *
from app_context import AppContext
from moving_commands import find_in_set
from shapes import Line


LOGGER = logging.getLogger("focus_commands")

def add_to_selection(event, context: AppContext, multi_select: bool = False):
    matched_line = _find_closest(event,context)
    if matched_line:
        shape = find_in_set(matched_line.id, context.widgets)
        if multi_select:
            if shape not in context.selected_widgets:
                context.selected_widgets.append(shape)
                set_fill_color(context, shape.id, "green")
        else:
           #reset color for old_selection
           for shape in context.selected_widgets:
                set_fill_color(context, shape.id, "black")  
        
           context.selected_widgets = [shape]
           set_fill_color(context, shape.id, "green")
    else:
        # if didn't find anything
        # reset color all selected widgets before
        for shape in context.selected_widgets:
            set_fill_color(context, shape.id, "black") 
        context.selected_widgets = []


def set_fill_color(context, shape_id, color):
    context.canvas.itemconfig(shape_id, fill=color)

def focus_on_line(event, context: AppContext):
    matched_line_id = context.canvas.find_closest(event.x, event.y)[0]
    matched_line = find_in_set(matched_line_id, context.widgets)
    if matched_line:
        context.current_line = matched_line 
        start_x = matched_line.start_x - context.canvas.winfo_width() / 2
        start_y = - (matched_line.start_y - context.canvas.winfo_height() / 2)
        end_x =  matched_line.end_x - context.canvas.winfo_width() / 2
        end_y = - (matched_line.end_y - context.canvas.winfo_height() / 2)

        a_coefficent = (end_y - start_y)
        b_coefficent = -(end_x - start_x)
        c_coefficent = - end_x * (end_y - start_y) + (end_x - start_x) * end_y 

        context.canvas.itemconfig(matched_line_id, fill="green")
        context.status_bar.config(text=f"{int(a_coefficent)}x + ({int(b_coefficent)})y + ({int(c_coefficent)}) = 0")
    else:
        context.current_line = None

def release_focus(event, context: AppContext):
    if context.current_line:
        context.canvas.itemconfig(context.current_line.id, fill="black")
        context.current_line = None


def _find_closest(event, context: AppContext):
    matched_line_id = context.canvas.find_closest(event.x, event.y)[0]
    line: Line = find_in_set(matched_line_id, context.widgets)
    if (abs(line.get_center()[0] - event.x) < 50 and abs(line.get_center()[1] - event.y) < 50):
        return line

