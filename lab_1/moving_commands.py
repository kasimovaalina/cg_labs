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

def find_the_closest(event, context):
    for line in context.widgets:
        LOGGER.debug(f"LINE: {line.start_x} {line.start_y} {line.end_x} {line.end_y}")
        if matchWith(line.start_x, line.start_y, event.x, event.y) or  matchWith(line.end_x, line.end_y , event.x, event.y):
            return line           

def matchWith(target_x,target_y, x,y,radius=10):
    from_x = x - radius
    to_x = x + radius
    from_y = y - radius
    to_y = y + radius
    LOGGER.debug(f"Target x: {target_x}, From: {from_x}, To: {to_x}")
    LOGGER.debug(f"Target y: {target_y}, From: {from_y}, To: {to_y}")
    return in_range_closed(target_x, from_x, to_x) and in_range_closed(target_y, from_y, to_y)

def in_range_closed(n, start, end):
    return n >= start and n <= end

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