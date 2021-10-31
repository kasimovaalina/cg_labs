import logging
from os import curdir
from tkinter import *
from typing import *
from app_context import AppContext
from moving_commands import find_in_set
from shapes import Line

LOGGER = logging.getLogger("changing_commands")

def find_in_set(id, lines):
    for line in lines:
        if line.id == id:
            return line

def match_with(target_x,target_y, x,y,radius=10):
    from_x = x - radius
    to_x = x + radius
    from_y = y - radius
    to_y = y + radius
    return in_range_closed(target_x, from_x, to_x) and in_range_closed(target_y, from_y, to_y)

def in_range_closed(n, start, end):
    return n >= start and n <= end

def start_change_line(event, context: AppContext):
    # probably will cause a problem when choosing a line among many others
    matched_line_id = context.canvas.find_closest(event.x, event.y)[0]
    coords = context.canvas.coords(matched_line_id)
    context.canvas.delete(matched_line_id)

    line_id = context.canvas.create_line(coords[0],coords[1], coords[2],coords[3])
    line = Line(line_id, coords[0],coords[1], coords[2],coords[2])
    context.current_line = line

    context.widgets.remove(find_in_set(matched_line_id, context.widgets))
    
def on_line_changing(event, context: AppContext):
    if context.current_line:
        start_x = context.current_line.start_x
        start_y = context.current_line.start_y
        context.canvas.delete(context.current_line.id)
        line_id = context.canvas.create_line(start_x, start_y, event.x, event.y)
        line = Line(line_id, start_x, start_y, event.x, event.y)
        context.current_line = line

def line_changing_complete(event, context: AppContext):
    if context.current_line:
        context.widgets.append(context.current_line)
        context.current_line = None 