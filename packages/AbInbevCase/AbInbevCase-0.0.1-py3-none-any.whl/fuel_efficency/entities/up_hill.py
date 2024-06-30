from dataclasses import dataclass, field

from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


@dataclass(slots=True)
class UpHill:
    weight: float = float(2)
    position: 'Position' = field(default_factory=Position)

    def __hash__(self):
        return hash((self.weight, self.position.x, self.position.y))
    
    def __eq__(self, other):
        try:
            return (self.weight, self.position.x, self.position.y) == (other.weight, other.position.x, other.position.y)
        
        except AttributeError:
            raise NotImplementedError("Missing `position` or `weight` attribute")

    def __lt__(self, other):
        try:
            return self.weight < other.weight
        
        except AttributeError:
            raise NotImplementedError("Missing `weight` attribute")
 