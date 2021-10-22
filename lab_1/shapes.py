from dataclasses import dataclass

@dataclass(frozen=True)
class Shape:
    id: str

@dataclass(frozen=True)
class Line(Shape):
    start_x: int
    start_y: int
    end_x: int
    end_y: int