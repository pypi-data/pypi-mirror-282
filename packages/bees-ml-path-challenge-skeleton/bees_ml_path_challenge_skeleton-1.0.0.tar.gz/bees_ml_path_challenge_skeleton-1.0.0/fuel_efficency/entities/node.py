from dataclasses import dataclass
from typing import Protocol

from fuel_efficency.entities.position import Position


@dataclass(slots=True, frozen=True)
class Node(Protocol):
    weight: float
    position: 'Position' = Position()

    def __eq__(self, other:'Node') -> bool:
        if not isinstance(other, self.__class__):
            raise NotImplementedError("Missing `position` or `weight` attribute")

        return hash(self) == hash(other)

    def __lt__(self, other:'Node') -> bool:
        if not hasattr(other, 'weight'):
            raise NotImplementedError("Missing `weight` attribute")

        return (self.weight < other.weight)
