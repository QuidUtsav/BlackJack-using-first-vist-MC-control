# Blackjack Reinforcement Learning

A from-scratch implementation of a Blackjack environment and a tabular Reinforcement Learning agent using **First-Visit Monte Carlo Control**.

This project was built to develop a practical understanding of Reinforcement Learning fundamentals, particularly state representation, action-value estimation, exploration vs. exploitation, and policy evaluation.

Rather than relying on an existing RL environment, I implemented the game mechanics and learning agent independently in Python.

## Project Objectives

- Build a custom Blackjack environment.
- Model Blackjack as a Markov Decision Process.
- Implement a tabular Q-value representation.
- Understand and implement First-Visit Monte Carlo Control.
- Experiment with epsilon-greedy exploration.
- Compare a learned policy against a random policy.
- Understand the distinction between training and evaluation.

## Project Structure

```text
BlackJack/
├── Agent.py          # RL agent and Monte Carlo learning
├── Dealer.py         # Dealer logic
├── Deck.py           # Card deck and card generation
├── Environment.py    # Blackjack environment
├── Hand.py           # Hand management and score calculation
├── Player.py         # Player logic
├── main.py           # Training and evaluation
├── prac.py           # Experiments and practice
└── README.md
```

## Environment Design

The environment implements a simplified Blackjack game.

### State Space

The agent observes three features:

| Feature | Description |
|---|---|
| `player_sum` | Current value of the player's hand |
| `dealer_showing_card` | Dealer's visible card |
| `usable_ace` | Whether an Ace is currently counted as 11 |

The state is represented as:

\[
S=(player\_sum,\ dealer\_showing\_card,\ usable\_ace)
\]

### Action Space

| Action | Description |
|---|---|
| `0` | Stick — stop taking cards |
| `1` | Hit — draw another card |

### Reward Function

| Outcome | Reward |
|---|---:|
| Win | +1 |
| Loss | -1 |
| Draw | 0 |

The agent receives its terminal reward when an episode finishes.

## Learning Algorithm: First-Visit Monte Carlo Control

The agent learns using tabular Monte Carlo control.

It maintains a Q-table containing the estimated value of taking each action in a particular state:

\[
Q(s,a)=\mathbb{E}[G_t\mid S_t=s,A_t=a]
\]

Here, \(G_t\) represents the return observed after taking action \(a\) in state \(s\).

### First-Visit Updates

The implementation records state-action pairs throughout an episode and updates only their first occurrence after the episode terminates.

The Q-value is updated using an incremental sample average:

\[
Q(s,a)\leftarrow Q(s,a)+
\frac{G-Q(s,a)}{N(s,a)}
\]

Where:

- \(G\): Observed return.
- \(N(s,a)\): Number of episodes in which the pair has been updated.
- \(Q(s,a)\): Current action-value estimate.

Because the simplified environment uses terminal rewards and a discount factor of 1, the same final reward is used as the return for each timestep in an episode.

## Exploration Strategy: Epsilon-Greedy

The agent uses epsilon-greedy exploration.

- With probability \(\epsilon\), it selects a random action.
- Otherwise, it selects the action with the highest estimated Q-value.
- If both actions have equal Q-values, it randomly breaks the tie.

The initial experiment uses a fixed exploration probability:

\[
\epsilon=0.1
\]

This allows the agent to continue exploring while exploiting its current knowledge.

## Training and Evaluation

Training and evaluation are performed separately.

### Training

- Training episodes: **1,000,000**
- Exploration strategy: Fixed epsilon-greedy
- Exploration probability: 0.1
- Q-values updated after each completed episode.
- First-Visit Monte Carlo updates.

### Evaluation

After training, epsilon is set to zero.

The agent then plays 100,000 additional episodes without updating its Q-table or recording learning experiences.

This evaluates the learned greedy policy independently of the exploration performed during training.

## Experimental Results

### Training Performance

<text-placeholder/>

| Outcome | Episodes | Percentage |
|---|---:|---:|
| Wins | 405,913 | 40.59% |
| Losses | 510,022 | 51.00% |
| Draws | 84,065 | 8.41% |
| Total | 1,000,000 | 100% |

Average reward:

\[
\frac{405913-510022}{1000000}=-0.104109
\]

### Evaluation Performance

| Outcome | Episodes | Percentage |
|---|---:|---:|
| Wins | 42,430 | 42.43% |
| Losses | 48,505 | 48.51% |
| Draws | 9,065 | 9.07% |
| Total | 100,000 | 100% |

Average reward:

\[
\frac{42430-48505}{100000}=-0.06075
\]

### Random Policy Comparison

A random policy was also tested over 4 million episodes.

| Outcome | Approximate percentage |
|---|---:|
| Wins | 27.52% |
| Losses | 68.42% |
| Draws | 4.02% |

The learned policy substantially outperformed random action selection.

*Note: These are separate experimental runs, not a controlled statistical comparison using identical random seeds.*

## Key Takeaways

Through this project, I developed a better understanding of:

1. Modeling an environment using states, actions, and rewards.
2. Designing a state representation that captures relevant decision-making information.
3. Estimating action values from complete episodes.
4. Implementing First-Visit Monte Carlo updates.
5. Balancing exploration and exploitation using epsilon-greedy.
6. Separating policy training from policy evaluation.
7. Comparing learned behavior against simpler baselines.

One particularly important observation was that training performance does not necessarily represent the quality of the learned policy, because exploration introduces deliberately non-greedy actions.

## Running the Project

Clone the repository and run:

```bash
python main.py
```

No external RL framework is required for the core implementation.

## Conclusion

This project served as a practical introduction to Reinforcement Learning.

The primary goal was not to produce a perfect Blackjack-playing agent, but to understand how an agent can learn action values and improve its decision-making through interaction with an environment.

It also established a foundation for exploring more advanced algorithms, including Temporal Difference learning and Deep Reinforcement Learning.
