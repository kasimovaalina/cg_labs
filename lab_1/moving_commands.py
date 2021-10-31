import logging
from os import curdir
from tkinter import *
from typing import *
from app_context import AppContext
from shapes import Line

LOGGER = logging.getLogger("moving_commands")


def move_line(event, context: AppContext):
    LOGGER.debug(f"Set: {context.widgets}")
    matched_line_id = context.canvas.find_closest(event.x, event.y)[0]
    matched_line = find_in_set(matched_line_id, context.widgets)
    if matched_line:
        LOGGER.debug(f"There is the match: {matched_line}")
        context.current_line = matched_line 
        context.path_start = (event.x, event.y)  
    else:
        context.current_line = None

def find_in_set(id, lines):
    for line in lines:
        if line.id == id:
            return line

def on_line_moving(event, context):
    if context.current_line:
        line: Line = context.current_line
        LOGGER.debug(f"Line before change: {line}")
        left_x, top_y = line.left_top_boundary()
        s_x, s_y = context.path_start
        LOGGER.debug(f"s_x {s_x}, s_y {s_y}")
        diff_x, diff_y = s_x - event.x, s_y  - event.y
        LOGGER.debug(f"Event X:{event.x} Y:{event.y}")
        LOGGER.debug(f"dif_x {diff_x}, dif_y {diff_y}")
        context.canvas.moveto(line.id, left_x - diff_x, top_y - diff_y)
        
        coords = context.canvas.coords(line.id)
        LOGGER.debug(f"COORDS: {coords}")
        #line.update_points(*coords)
        line.update_points_2(diff_x, diff_y)
        LOGGER.debug(f"Line after change: {line}")
        context.path_start = (event.x, event.y)


def line_moving_complete(event, context: AppContext):
    if context.current_line:
        context.current_line = None
        context.path_start = None