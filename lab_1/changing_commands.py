import logging
from os import curdir
from tkinter import *
from typing import *
from app_context import AppContext
from moving_commands import find_in_set
from shapes import Line
import math

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
    old_line = find_in_set(matched_line_id,context.widgets)
    context.canvas.delete(matched_line_id)

    line_id = context.canvas.create_line(old_line.start_x,old_line.start_y, old_line.end_x,old_line.end_y)
    line = Line(line_id, old_line.start_x,old_line.start_y, old_line.end_x,old_line.end_y)
    
    context.current_line = line

    diff_x_start = abs(old_line.start_x - event.x)
    diff_y_start = abs(old_line.start_y - event.y)
    diff_x_end = abs(old_line.end_x - event.x)
    diff_y_end = abs(old_line.end_y - event.y)

    if (diff_x_start < diff_x_end or diff_y_start < diff_y_end):
        context.changing_start = True
        context.changing_end = False
    else: 
        context.changing_end = True
        context.changing_start = False

    context.widgets.remove(old_line)

    
def on_line_changing(event, context: AppContext):
    if context.current_line:
        start_x = context.current_line.start_x
        start_y = context.current_line.start_y
        end_x = context.current_line.end_x
        end_y = context.current_line.end_y
        if (context.changing_end):
            context.canvas.delete(context.current_line.id)
            line_id = context.canvas.create_line(start_x, start_y, event.x, event.y)
            line = Line(line_id, start_x, start_y, event.x, event.y)
            context.current_line = line
        elif (context.changing_start):
            context.canvas.delete(context.current_line.id)
            line_id = context.canvas.create_line(event.x, event.y, end_x, end_y)
            line = Line(line_id, event.x, event.y, end_x, end_y)
            context.current_line = line

def line_changing_complete(event, context: AppContext):
    if context.current_line:
        context.widgets.append(context.current_line)
        context.current_line = None 

def rotate_line(line:Line, context: AppContext):
    tempX1 = (context.canvas.winfo_width() / 2) + (((line.start_x - (context.canvas.winfo_width() / 2)) * math.cos(0.175)) + (((line.start_y - (context.canvas.winfo_height() / 2)) * math.sin(0.175))))
    tempX2 = (context.canvas.winfo_width() / 2) + (((line.end_x - (context.canvas.winfo_width() / 2)) * math.cos(0.175)) + (((line.end_y - (context.canvas.winfo_height() / 2)) * math.sin(0.175))))
    tempY1 = (context.canvas.winfo_height() / 2) + (-((line.start_x - (context.canvas.winfo_width() / 2)) * math.sin(0.175)) + (((line.start_y - (context.canvas.winfo_height() / 2)) * math.cos(0.175))))
    tempY2 = (context.canvas.winfo_height()/ 2) + (-((line.end_x - (context.canvas.winfo_width() / 2)) * math.sin(0.175)) + (((line.end_y - (context.canvas.winfo_height() / 2)) * math.cos(0.175))))
    context.canvas.coords(line.id, tempX1, tempY1, tempX2, tempY2)
    line.update_points(tempX1, tempY1, tempX2, tempY2)
    
def increase_line(line:Line, context: AppContext):
    new_start_x = (line.start_x - context.canvas.winfo_width() / 2) * 1.1 + context.canvas.winfo_width() / 2
    new_start_y = (line.start_y - context.canvas.winfo_height() / 2) * 1.1 + context.canvas.winfo_height() / 2
    new_end_x = (line.end_x - context.canvas.winfo_width() / 2) * 1.1 + context.canvas.winfo_width() / 2
    new_end_y = (line.end_y - context.canvas.winfo_height() / 2) * 1.1 + context.canvas.winfo_height() / 2
    context.canvas.coords(line.id, new_start_x, new_start_y, new_end_x, new_end_y)
    line.update_points(new_start_x, new_start_y, new_end_x, new_end_y)

def decrease_line(line:Line, context: AppContext):
    new_start_x = (line.start_x - context.canvas.winfo_width() / 2) / 1.1 + context.canvas.winfo_width() / 2
    new_start_y = (line.start_y - context.canvas.winfo_height() / 2) / 1.1 + context.canvas.winfo_height() / 2
    new_end_x = (line.end_x - context.canvas.winfo_width() / 2) / 1.1 + context.canvas.winfo_width() / 2
    new_end_y = (line.end_y - context.canvas.winfo_height() / 2) / 1.1 + context.canvas.winfo_height() / 2
    context.canvas.coords(line.id, new_start_x, new_start_y, new_end_x, new_end_y)
    line.update_points(new_start_x, new_start_y, new_end_x, new_end_y)