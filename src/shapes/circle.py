from mymath import PI
from dataclasses import dataclass


@dataclass
class Circle:
    r: int

    def get_area(self):
        return (self.r ** 2) * PI
