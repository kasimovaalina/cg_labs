import logging
from os import curdir
from tkinter import *
from typing import *
from app_context import AppContext
from moving_commands import find_in_set
from shapes import Line

def delete_line(event, context: AppContext):
    matched_line_id = context.canvas.find_closest(event.x, event.y)[0]
    context.canvas.delete(matched_line_id)
    context.widgets.remove(find_in_set(matched_line_id, context.widgets))


