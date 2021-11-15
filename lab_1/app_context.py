from tkinter import *
from typing import *
from action import Action
from shapes import *

class AppContext:
    def __init__(self):
        self.current_action: Action = None
        self.canvas: Canvas = None
        self.status_bar: Label = None
        self.widgets: List[Shape] = []
        self.selected_widgets = []
        self.current_line: Line = None
        self.path_start: Tuple[int, int] = None
        self.changing_start: bool = False
        self.changing_end: bool = False