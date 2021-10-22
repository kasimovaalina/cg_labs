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
    else:
        context.current_line = None

def find_in_set(id, lines):
    for line in lines:
        if line.id == id:
            return line

def on_line_moving(event, context):
    if context.current_line:
        line = context.current_line
        context.canvas.moveto(line.id, event.x, event.y)
        coords = context.canvas.coords(line.id)
        LOGGER.debug(f"COORDS: {coords}")
        LOGGER.debug(f"Line: {line}, {coords}")
        line.start_x = coords[0]
        line.start_y = coords[1]
        line.end_x = coords[2]
        line.end_y = coords[3]

def line_moving_complete(event, context: AppContext):
    if context.current_line:
        context.current_line = None