from tkinter import *
from typing import *
from app_context import AppContext
from shapes import Line

def create_line(event, context: AppContext):
    line_id = context.canvas.create_line(event.x, event.y, event.x, event.y)
    line = Line(line_id, event.x, event.y, event.x, event.y)
    context.current_line = line

def on_line_drawing(event, context):
    if context.current_line:
        start_x = context.current_line.start_x
        start_y = context.current_line.start_y
        context.canvas.delete(context.current_line.id)
        line_id = context.canvas.create_line(start_x, start_y, event.x, event.y)
        line = Line(line_id, start_x, start_y, event.x, event.y)
        context.current_line = line

def line_drawing_complete(event, context):
    if context.current_line:
        context.widgets.append(context.current_line)
        context.current_line = None

def draw_morphed_line(line1: Line, line2:Line, context:AppContext):
    t = 0.5
    start_x = line1.start_x*(1-t) +line2.start_x*t
    start_y = line1.start_y*(1-t) +line2.start_y*t
    end_x = line1.end_x*(1-t) +line2.end_x*t
    end_y = line1.end_y*(1-t) +line2.end_y*t
    line_id = context.canvas.create_line(start_x, start_y, end_x, end_y)
    new_line = Line(line_id, start_x, start_y, end_x, end_y)
    context.widgets.append(new_line)