from dataclasses import dataclass

@dataclass()
class Shape:
    id: str

@dataclass()
class Line(Shape):
    start_x: int
    start_y: int
    end_x: int
    end_y: int