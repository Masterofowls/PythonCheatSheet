
"""
COMPREHENSIVE PYTHON AI ALGORITHMS GUIDE
======================================
This guide covers fundamental AI concepts, algorithms, and implementations.
Each section demonstrates different aspects of AI and machine learning.
"""

import numpy as np
from typing import List, Tuple, Optional
import random
import math

# ===========================
# SECTION 1: NEURAL NETWORKS
# ===========================
"""
Simple neural network implementation with forward propagation.
"""
print("\n=== Neural Networks ===")

class NeuralNetwork:
    def __init__(self, layers: List[int]):
        self.layers = layers
        self.weights = []
        self.biases = []
        
        for i in range(len(layers) - 1):
            self.weights.append(np.random.randn(layers[i], layers[i + 1]))
            self.biases.append(np.random.randn(1, layers[i + 1]))
    
    def sigmoid(self, x: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-x))
    
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        activation = inputs
        for i in range(len(self.weights)):
            net = np.dot(activation, self.weights[i]) + self.biases[i]
            activation = self.sigmoid(net)
        return activation

# Example usage
nn = NeuralNetwork([2, 3, 1])
input_data = np.array([[0, 1]])
output = nn.forward(input_data)
print(f"Neural Network output: {output}")

# ===========================
# SECTION 2: GENETIC ALGORITHM
# ===========================
"""
Simple genetic algorithm implementation.
"""
print("\n=== Genetic Algorithm ===")

class GeneticAlgorithm:
    def __init__(self, population_size: int, gene_length: int):
        self.population_size = population_size
        self.gene_length = gene_length
        self.population = self._create_population()
    
    def _create_population(self) -> List[List[int]]:
        return [[random.randint(0, 1) for _ in range(self.gene_length)]
                for _ in range(self.population_size)]
    
    def fitness(self, individual: List[int]) -> int:
        return sum(individual)  # Simple fitness: count of 1s
    
    def crossover(self, parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
        point = random.randint(1, self.gene_length - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    
    def mutate(self, individual: List[int], mutation_rate: float = 0.01) -> List[int]:
        return [1 - gene if random.random() < mutation_rate else gene 
                for gene in individual]
    
    def evolve(self, generations: int = 100) -> List[int]:
        for _ in range(generations):
            # Sort population by fitness
            self.population.sort(key=self.fitness, reverse=True)
            
            # Create new population
            new_population = self.population[:2]  # Keep best 2
            
            while len(new_population) < self.population_size:
                parent1 = random.choice(self.population[:10])  # Top 10
                parent2 = random.choice(self.population[:10])
                child1, child2 = self.crossover(parent1, parent2)
                new_population.extend([self.mutate(child1), self.mutate(child2)])
            
            self.population = new_population[:self.population_size]
        
        return max(self.population, key=self.fitness)

# Example usage
ga = GeneticAlgorithm(population_size=50, gene_length=10)
best_solution = ga.evolve()
print(f"Best solution: {best_solution}")
print(f"Fitness: {ga.fitness(best_solution)}")

# ===========================
# SECTION 3: K-MEANS CLUSTERING
# ===========================
"""
K-means clustering implementation.
"""
print("\n=== K-Means Clustering ===")

class KMeans:
    def __init__(self, k: int, max_iters: int = 100):
        self.k = k
        self.max_iters = max_iters
    
    def fit(self, data: np.ndarray) -> Tuple[np.ndarray, List[int]]:
        # Initialize centroids randomly
        centroids = data[np.random.choice(len(data), self.k, replace=False)]
        
        for _ in range(self.max_iters):
            # Assign points to nearest centroid
            distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))
            labels = np.argmin(distances, axis=0)
            
            # Update centroids
            new_centroids = np.array([data[labels == i].mean(axis=0) 
                                    for i in range(self.k)])
            
            # Check convergence
            if np.all(centroids == new_centroids):
                break
                
            centroids = new_centroids
        
        return centroids, labels.tolist()

# Example usage
data = np.random.randn(100, 2)  # 100 points in 2D
kmeans = KMeans(k=3)
centroids, labels = kmeans.fit(data)
print(f"Centroids:\n{centroids}")

# ===========================
# SECTION 4: A* PATHFINDING
# ===========================
"""
A* pathfinding algorithm implementation.
"""
print("\n=== A* Pathfinding ===")

class Node:
    def __init__(self, position: Tuple[int, int], parent: Optional['Node'] = None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Estimated cost from current node to end
        self.f = 0  # Total cost (g + h)

class AStar:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
    
    def heuristic(self, pos: Tuple[int, int], goal: Tuple[int, int]) -> float:
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    
    def get_neighbors(self, node: Node) -> List[Tuple[int, int]]:
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4-directional
            new_pos = (node.position[0] + dx, node.position[1] + dy)
            if (0 <= new_pos[0] < self.rows and 
                0 <= new_pos[1] < self.cols and 
                self.grid[new_pos[0]][new_pos[1]] == 0):
                neighbors.append(new_pos)
        return neighbors
    
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        start_node = Node(start)
        goal_node = Node(goal)
        
        open_list = [start_node]
        closed_list = []
        
        while open_list:
            current_node = min(open_list, key=lambda x: x.f)
            open_list.remove(current_node)
            closed_list.append(current_node)
            
            if current_node.position == goal_node.position:
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                return path[::-1]
            
            for neighbor_pos in self.get_neighbors(current_node):
                neighbor = Node(neighbor_pos, current_node)
                
                if neighbor in closed_list:
                    continue
                
                neighbor.g = current_node.g + 1
                neighbor.h = self.heuristic(neighbor_pos, goal)
                neighbor.f = neighbor.g + neighbor.h
                
                if neighbor not in open_list:
                    open_list.append(neighbor)
        
        return []  # No path found

# Example usage
grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
astar = AStar(grid)
path = astar.find_path((0, 0), (4, 4))
print(f"A* Path: {path}")

# ===========================
# SECTION 5: MINIMAX ALGORITHM
# ===========================
"""
Minimax algorithm implementation for game AI.
"""
print("\n=== Minimax Algorithm ===")

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'
    
    def available_moves(self) -> List[int]:
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def make_move(self, position: int, player: str) -> None:
        self.board[position] = player
    
    def undo_move(self, position: int) -> None:
        self.board[position] = ' '
    
    def check_winner(self, player: str) -> bool:
        # Check rows, columns and diagonals
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.board[i] == player for i in combo) 
                  for combo in win_combinations)
    
    def minimax(self, depth: int, is_maximizing: bool) -> int:
        if self.check_winner(self.ai):
            return 1
        if self.check_winner(self.human):
            return -1
        if not self.available_moves():
            return 0
        
        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves():
                self.make_move(move, self.ai)
                score = self.minimax(depth + 1, False)
                self.undo_move(move)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves():
                self.make_move(move, self.human)
                score = self.minimax(depth + 1, True)
                self.undo_move(move)
                best_score = min(score, best_score)
            return best_score
    
    def get_best_move(self) -> int:
        best_score = -math.inf
        best_move = None
        
        for move in self.available_moves():
            self.make_move(move, self.ai)
            score = self.minimax(0, False)
            self.undo_move(move)
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move

# Example usage
game = TicTacToe()
game.make_move(0, 'X')  # Human moves
best_ai_move = game.get_best_move()
print(f"Best AI move: {best_ai_move}")
