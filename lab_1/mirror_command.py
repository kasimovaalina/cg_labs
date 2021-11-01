import logging
from os import curdir
from tkinter import *
from typing import *
from app_context import AppContext
from moving_commands import find_in_set
from shapes import Line


LOGGER = logging.getLogger("mirror_command")


def mirror_line(event, context: AppContext):
    matched_line_id = context.canvas.find_closest(event.x, event.y)[0]

    old_line = find_in_set(matched_line_id, context.widgets)
    LOGGER.debug(f"Line before change: {old_line}")

    context.canvas.delete(matched_line_id)
    line_id = context.canvas.create_line(old_line.end_x, old_line.start_y, old_line.start_x, old_line.end_y)
    LOGGER.debug(f"Line after change: {line_id}")
    context.widgets.append(Line(line_id, old_line.end_x, old_line.start_y, old_line.start_x, old_line.end_y))

    context.widgets.remove(old_line)


