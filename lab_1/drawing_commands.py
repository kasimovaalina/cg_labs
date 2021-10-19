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
    context.current_line = None 