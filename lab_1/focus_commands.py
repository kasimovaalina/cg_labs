import logging
from os import curdir
from tkinter import *
from typing import *
from app_context import AppContext
from moving_commands import find_in_set
from shapes import Line


LOGGER = logging.getLogger("focus_commands")

def focus_on_line(event, context: AppContext):
    matched_line_id = context.canvas.find_closest(event.x, event.y)[0]
    matched_line = find_in_set(matched_line_id, context.widgets)
    if matched_line:
        context.current_line = matched_line 
        a_coefficent = (matched_line.end_y - matched_line.start_y)
        b_coefficent = -(matched_line.end_x - matched_line.start_x)
        c_coefficent = - matched_line.end_x * (matched_line.end_y - matched_line.start_y) + (matched_line.end_x - matched_line.start_x)*matched_line.end_y 

        context.canvas.itemconfig(matched_line_id, fill="green")
        context.status_bar.config(text=f"{a_coefficent}x + ({b_coefficent})y + ({c_coefficent}) = 0")
    else:
        context.current_line = None

def on_focus(event, context: AppContext):
    if (context.current_line):
        matched_line = context.current_line
        a_coefficent = (matched_line.end_y - matched_line.start_y)
        b_coefficent = -(matched_line.end_x - matched_line.start_x)
        c_coefficent = - matched_line.end_x * (matched_line.end_y - matched_line.start_y) + (matched_line.end_x - matched_line.start_x)*matched_line.end_y 

        LOGGER.debug(f"a : {a_coefficent} b: {b_coefficent} c: {c_coefficent}")

        context.canvas.itemconfig(matched_line.id, fill="green")
        context.status_bar.config(text=f"{a_coefficent}x + ({b_coefficent})y + ({c_coefficent}) = 0")


def release_focus(event, context: AppContext):
    if context.current_line:
        context.canvas.itemconfig(context.current_line.id, fill="black")
        context.current_line = None
