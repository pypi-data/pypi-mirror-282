import heapq
import math
from typing import List

from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


class DijkstraStrategy(PathfindingStrategy):

    cardinal_directions = [Position(-1, -1), Position(-1, 0), Position(-1, 1), Position(0, -1), Position(0, 1), Position(1, -1), Position(1, 0), Position(1, 1)]
    
    @staticmethod
    def find_path(grid: List[List[Node]], start: Node, end: Node) -> List[Node]:

        distances = {node: float('inf') for row in grid for node in row}
        distances[start] = 0
        priority_queue = [(0, start)]
        previous_nodes = {start: None}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == end:
                break

            for neighbor in DijkstraStrategy.get_neighbors(grid, current_node):
                distance = current_distance + DijkstraStrategy.calculate_distance(current_node, neighbor)
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    previous_nodes[neighbor] = current_node

        path = []
        current = end
        while start != current:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()

        return path

    @staticmethod
    def get_neighbors(grid: List[List[Node]], node: Node) -> List[Node]:
        neighbors = []

        for direction in DijkstraStrategy.cardinal_directions:
            neighbor_position = node.position + direction
            
            if 0 <= neighbor_position.x < len(grid) and 0 <= neighbor_position.y < len(grid[0]):
                neighbors.append(grid[neighbor_position.x][neighbor_position.y])

        return neighbors

    @staticmethod
    def calculate_distance(node1: Node, node2: Node) -> float:
        # Euclidean distance because we can move in any direction
        return math.sqrt((node1.position.x - node2.position.x) ** 2 + (node1.position.y - node2.position.y) ** 2)
