from tkinter import *
from typing import *
from action import Action
from shapes import Line

class AppContext:
    def __init__(self):
        self.current_action: Action = None
        self.canvas: Canvas = None
        self.id_to_widget: Dict[any,any] = None
        self.current_line: Line = None