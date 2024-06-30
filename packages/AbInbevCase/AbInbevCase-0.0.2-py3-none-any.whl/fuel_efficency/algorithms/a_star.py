import heapq
from typing import List

from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


class AStarStrategy(PathfindingStrategy):

    allowed_directions = [Position(-1, 0), Position(0, -1), Position(0, 1), Position(1, 0)]

    def find_path(grid: List[List[Node]], start: Node, end: Node) -> List[Node]:
        open_set = []
        closed_set = []
        heapq.heappush(open_set, (0, start))
        
        g_score = {start: 0}
        f_score = {start: AStarStrategy.calculate_distance(start, end)}
        previous_nodes = {}

        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current == end:
                path = []
                current = end
                while start != current:
                    path.append(current)
                    current = previous_nodes[current]
                path.reverse()

                return path
            
            closed_set.append(current)

            for neighbor in AStarStrategy.get_neighbors(grid, current):
                if neighbor in closed_set or neighbor.weight == float('inf'):
                    continue

                tentative_g_score = g_score[current] + AStarStrategy.calculate_distance(current, neighbor)
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    previous_nodes[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + AStarStrategy.calculate_distance(neighbor, end)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return open_set

    def get_neighbors(grid: List[List[Node]], node: Node) -> List[Node]:
        neighbors = []
        
        for direction in AStarStrategy.allowed_directions:
            new_position = node.position + direction
            if 0 <= new_position.x < len(grid) and 0 <= new_position.y < len(grid[0]):
                neighbors.append(grid[new_position.x][new_position.y])

        return neighbors

    def calculate_distance(node1: Node, node2: Node) -> float:
        # Manhattan distance because we are only allowed to move in 4 directions
        return abs(node1.position.x - node2.position.x) + abs(node1.position.y - node2.position.y)
