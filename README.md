# AI Pathfinder – Uninformed Search Visualization
### GOOD PERFORMANCE TIME APP

This project implements and visualizes six fundamental **Uninformed Search Algorithms** in a grid-based environment.

The system demonstrates how each algorithm explores a grid from a **Start (S)** node to a **Target (T)** node while avoiding static obstacles (walls).  
The GUI visualizes the search process step-by-step to clearly show how each algorithm "thinks".

---

## Implemented Algorithms

The following search strategies are implemented:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform-Cost Search (UCS)
- Depth-Limited Search (DLS)
- Iterative Deepening DFS (IDDFS)
- Bidirectional Search

All algorithms:
- Follow the required strict clockwise movement order (including diagonals).
- Use cost per action = 1.
- Animate exploration step-by-step.
- Display expansion order numbers.
- Highlight frontier nodes, explored nodes, and final path.

---

## 🖥️ GUI Features

The visualization includes:

- Real-time step-by-step animation
- Frontier nodes (yellow)
- Explored nodes (light gray)
- Final path (blue)
- Start node (green)
- Target node (blue)
- Expansion order numbers displayed inside each visited cell
- GUI title: **GOOD PERFORMANCE TIME APP**

Console output includes:
- Algorithm name
- Path length
- Path sequence

---

## 📂 Project Structure

AI_A1_23F-0643
│
├── main.py
├── grid.py
├── visualisation.py
├── bfs.py
├── dfs.py
├── ucs.py
├── dls.py
├── iddfs.py
├── bidirectional.py
└── README.md

## ⚙️ Requirements

Make sure Python 3.8 or higher is installed.

### Install Required Dependencies

Run the following command in your terminal:

bash
pip install matplotlib numpy


### how to Run the project
 Navigate to the project directory in terminal:
cd AI_A1_23F-0643
Run:
python main.py

### Test Scenarios

The project includes:

Best-case grid scenario

Worst-case grid scenario

These can be selected from grid.py to generate required screenshots for the report.

