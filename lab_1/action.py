from dataclasses import dataclass
from typing import *
from enum import Enum

@dataclass()
class Action:
    on_mouse_click: Callable
    on_mouse_move: Callable
    on_mouse_release: Callable