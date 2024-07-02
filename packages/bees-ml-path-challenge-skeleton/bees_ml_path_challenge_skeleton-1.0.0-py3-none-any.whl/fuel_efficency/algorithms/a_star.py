import heapq
import math
from typing import List

from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


class AStarStrategy(PathfindingStrategy):

    allowed_directions: list[Position] = [Position(-1, 0), Position(0, -1), Position(0, 1), Position(1, 0)]

    def find_path(grid:List[List[Node]], start:Node, end:Node) -> List[Node]:
        min_heap = [(0, start)]
        shortest_distance = { start: 0 }
        previous_node = {}

        while min_heap:
            distance_1, node_1 = heapq.heappop(min_heap)

            if node_1 == end:
                return AStarStrategy._path(previous_node, end)

            for node_2 in AStarStrategy.get_neighbors(grid, node_1):
                distance_2 = distance_1 + AStarStrategy.calculate_distance(node_1, node_2)

                if distance_2 < shortest_distance.get(node_2, math.inf):
                    shortest_distance[node_2] = distance_2
                    previous_node[node_2] = node_1
                    heuristic_distance_to_end = AStarStrategy.calculate_distance(node_2, end)
                    heapq.heappush(min_heap, (distance_2 + heuristic_distance_to_end, node_2))

        raise ValueError("Unable to find path")


    def get_neighbors(grid:List[List[Node]], node:Node) -> List[Node]:
        all_positions = [allowed_direction + node.position for allowed_direction in AStarStrategy.allowed_directions]

        possible_positions = [position for position in all_positions if 0 <= position.x < len(grid) and 0 <= position.y < len(grid[0])]

        return [grid[position.x][position.y] for position in possible_positions]

    def calculate_distance(node1:Node, node2:Node) -> float:
        return abs(node1.position.x - node2.position.x) + abs(node1.position.y - node2.position.y)

    def _path(previous_node: dict[Node, Node], end: Node) -> List[Node]:
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_node.get(current, None)
        path.reverse()
        path.pop(0)
        return path
