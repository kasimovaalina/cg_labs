from tkinter import *
from typing import *
from action import Action
from shapes import *

class AppContext:
    def __init__(self):
        self.current_action: Action = None
        self.canvas: Canvas = None
        self.widgets: set[Shape] = set()
        self.current_line: Line = None