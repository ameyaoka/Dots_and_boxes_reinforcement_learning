# Dots_and_boxes_reinforcement_learning
implementing dots and boxes game but using reinforcement learning 

1. This is currently a basic implementation of the game 
2. Train an AI agent to play the game using reinforcement learning (Q-learning)
3. We will design a better UI Afterward :)

## Reinforcement Learning 
-    Agent: The learner or decision-maker.
-    Environment: Everything the agent interacts with.
-    Action: What the agent can do.
-    State: Current situation returned by the environment.
-    Reward: Feedback from the environment after taking actions, guiding the learning process by indicating what's good or bad.
-    Policy: Strategy the agent uses to determine the next action based on the current state.


## Possible action in a 4×4 Grid

### Horizontal Moves (Row-wise)
- (0,0) → (0,1)
- (0,1) → (0,2)
- (0,2) → (0,3)

- (1,0) → (1,1)
- (1,1) → (1,2)
- (1,2) → (1,3)

- (2,0) → (2,1)
- (2,1) → (2,2)
- (2,2) → (2,3)

- (3,0) → (3,1)
- (3,1) → (3,2)
- (3,2) → (3,3)

### Vertical Moves (Column-wise)
- (0,0) → (1,0)
- (1,0) → (2,0)
- (2,0) → (3,0)

- (0,1) → (1,1)
- (1,1) → (2,1)
- (2,1) → (3,1)

- (0,2) → (1,2)
- (1,2) → (2,2)
- (2,2) → (3,2)

- (0,3) → (1,3)
- (1,3) → (2,3)
- (2,3) → (3,3)

**Total Moves: 24**



	
