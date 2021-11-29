from dataclasses import dataclass
from typing import Tuple

@dataclass()
class Shape:
    id: str

@dataclass()
class Line(Shape):
    start_x: int
    start_y: int
    end_x: int
    end_y: int

    def left_top_boundary(self) -> Tuple[int, int]:
        left_x = min(self.start_x, self.end_x)
        top_y = min(self.start_y, self.end_y)
        return (left_x, top_y)
        
    def get_center(self) -> Tuple[int, int]:
        center_x = (self.start_x + self.end_x) // 2
        center_y = (self.start_y + self.end_y) // 2
        return (center_x, center_y)

    

    def update_points(self, s_x,s_y, e_x,e_y):
        self.start_x = s_x
        self.start_y = s_y
        self.end_x = e_x
        self.end_y = e_y

    
    def update_points_2(self, diff_x, diff_y):
        self.start_x -= diff_x
        self.start_y -= diff_y
        self.end_x -= diff_x
        self.end_y -= diff_y

@dataclass
class Unreachable_line(Shape):
    start_x: int
    start_y: int
    end_x: int
    end_y: int