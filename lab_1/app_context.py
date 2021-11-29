from tkinter import *
from typing import *
from action import Action
from shapes import *

class AppContext:
    def __init__(self):
        self.current_action: Action = None
        self.canvas: Canvas = None
        self.status_bar: Label = None
        self.plane_status_bar: Label = None
        self.widgets: List[Shape] = []
        self.selected_widgets = []

        self.widgets_XOY: List[Shape] = []
        self.unreachebale_widgets_XOY: List[Shape] = []

        self.widgets_XOZ: List[Shape] = []
        self.unreachebale_widgets_XOZ: List[Shape] = []

        self.current_line: Line = None
        self.path_start: Tuple[int, int] = None
        self.changing_start: bool = False
        self.changing_end: bool = False
        self.plane: str = "XOY"