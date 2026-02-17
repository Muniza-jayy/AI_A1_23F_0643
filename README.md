
# AI Pathfinder – Uninformed Search Visualization  
## GOOD PERFORMANCE TIME APP

This project implements and visualizes six **Uninformed Search Algorithms** in a grid-based environment.

The system shows how each algorithm explores a grid from a **Start (S)** node to a **Target (T)** node while avoiding **static obstacles (walls)**.  
The GUI animates the search step-by-step to clearly display the frontier, explored nodes, and final path.

---

##  Implemented Algorithms

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Uniform-Cost Search (UCS)** *(cost per action = 1)*
- **Depth-Limited Search (DLS)**
- **Iterative Deepening DFS (IDDFS)**
- **Bidirectional Search**

All algorithms:
- Follow the required strict clockwise movement order (including diagonals).
- Use path cost = **1 per move**.
- Animate exploration step-by-step.
- Show **expansion order numbering**.
- Highlight **frontier**, **explored**, and **final path** cells.

---

##  GUI Features

The visualization includes:

- Algorithm selection (radio buttons)
- Scenario selection: **Default / Best / Worst**
- Buttons: **Run / Reset / Exit**
- Frontier nodes (**yellow**)
- Explored nodes (**light gray**)
- Final path (**blue**)
- Start node (**green**) labeled **S**
- Target node (**blue**) labeled **T**
- Expansion order numbers shown inside visited cells  
  *(numbers do not overwrite S/T)*

Console output includes:
- Algorithm name
- Scenario name
- Path length
- Path sequence


##  Project Structure


AI_A1_23F-0643/
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



##  Requirements

- Python **3.8+**
- Libraries:
  - `matplotlib`
  - `numpy`


## 📦 Installation

Run this in terminal:

pip install matplotlib numpy

## ▶️ How to Run

1. Open terminal and go to the project folder:

cd AI_A1_23F-0643


2. Run the program:


python main.py


3. In the GUI:

* Select an algorithm
* Select a scenario (**Default / Best / Worst**)
* Click **Run**


##  Test Scenarios (Screenshots)

The project supports three scenarios:

* **Default**: original static wall layout
* **Best**: narrow corridor (minimal branching)
* **Worst**: mostly open grid (high branching)

You can select scenarios directly from the GUI (radio buttons) to take screenshots for the report.



## 📝 Notes

* Movement order follows a clockwise order with diagonals enabled.
* The project focuses on visualization and conceptual understanding of uninformed search strategies.

