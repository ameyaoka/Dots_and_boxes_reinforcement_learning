
import numpy as np
import pickle
from collections import defaultdict

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = defaultdict(lambda: np.zeros(24))  # Q-table , dictionary that maps state and action 
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor , how much agent values future rewards as compared to immediate ones 
        self.epsilon = epsilon  # Exploration rate , probability that agent will explroe rather than exploit knowledge it already has
        self.last_state = None
        self.last_action = None

