import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons

from grid import create_grid, create_grid_best, create_grid_worst
from visualisation import draw_grid, set_ui_ax  

from bfs import bfs
from dfs import dfs
from ucs import ucs
from dls import dls
from iddfs import iddfs
from bidirectional import bidirectional


class App:
    def __init__(self):
        self.current_algo_name = "BFS"
        self.stop_requested = False

        # Scenario selection
        self.current_scenario = "Default"

        # Create UI
        self.fig = plt.figure(figsize=(12, 7))
        self.ax_grid = self.fig.add_axes([0.05, 0.08, 0.62, 0.85])  # BIG grid area

        # Tell visualisation.py to ALWAYS draw here (prevents tiny grid bug)
        set_ui_ax(self.ax_grid)

        # --- Algorithm selector ---
        algo_names = ["BFS", "DFS", "UCS", "DLS (L=10)", "IDDFS (max=20)", "Bidirectional"]
        ax_radio_algo = self.fig.add_axes([0.72, 0.58, 0.25, 0.32])
        self.radio_algo = RadioButtons(ax_radio_algo, algo_names, active=0)
        self.radio_algo.on_clicked(self.on_algo_change)

        # --- Scenario selector ---
        scenario_names = ["Default", "Best", "Worst"]
        ax_radio_scene = self.fig.add_axes([0.72, 0.44, 0.25, 0.12])
        self.radio_scene = RadioButtons(ax_radio_scene, scenario_names, active=0)
        self.radio_scene.on_clicked(self.on_scenario_change)

        # --- Buttons ---
        ax_run = self.fig.add_axes([0.72, 0.32, 0.25, 0.07])
        self.btn_run = Button(ax_run, "Run")
        self.btn_run.on_clicked(self.on_run)

        ax_reset = self.fig.add_axes([0.72, 0.23, 0.25, 0.07])
        self.btn_reset = Button(ax_reset, "Reset")
        self.btn_reset.on_clicked(self.on_reset)

        ax_exit = self.fig.add_axes([0.72, 0.14, 0.25, 0.07])
        self.btn_exit = Button(ax_exit, "Exit")
        self.btn_exit.on_clicked(self.on_exit)

        # Keyboard shortcuts
        self.fig.canvas.mpl_connect("key_press_event", self.on_key)

        # Initial draw
        self.grid = self.make_grid()
        draw_grid(self.grid, algo="")

    # ---------- helpers ----------
    def make_grid(self):
        if self.current_scenario == "Best":
            return create_grid_best()
        elif self.current_scenario == "Worst":
            return create_grid_worst()
        return create_grid()

    def should_stop(self):
        # Allows exit/reset to interrupt running algorithms
        return self.stop_requested

    def run_algo(self):
        # Run selected algorithm with stop support
        if self.current_algo_name == "BFS":
            return bfs(self.grid, should_stop=self.should_stop)
        if self.current_algo_name == "DFS":
            return dfs(self.grid, should_stop=self.should_stop)
        if self.current_algo_name == "UCS":
            return ucs(self.grid, should_stop=self.should_stop)
        if self.current_algo_name == "DLS (L=10)":
            return dls(self.grid, 40, should_stop=self.should_stop)
        if self.current_algo_name == "IDDFS (max=20)":
            return iddfs(self.grid, 20, should_stop=self.should_stop)[0]
        if self.current_algo_name == "Bidirectional":
            return bidirectional(self.grid, should_stop=self.should_stop)
        return []

    # ---------- callbacks ----------
    def on_algo_change(self, label):
        self.current_algo_name = label

    def on_scenario_change(self, label):
        self.current_scenario = label
        # update grid preview when scenario changes
        self.grid = self.make_grid()
        draw_grid(self.grid, algo=f"{self.current_scenario} Scenario")

    def on_run(self, event=None):
        self.stop_requested = False

        print("\n==============================")
        print(f"Running Algorithm: {self.current_algo_name}")
        print(f"Scenario: {self.current_scenario}")
        print("==============================")

        # Reset grid for fresh run
        self.grid = self.make_grid()

        # Draw clean first frame
        draw_grid(self.grid, algo=self.current_algo_name)

        path = self.run_algo()

        # If stopped early, path may be empty
        print("Path length:", len(path))
        print("Path:", path)

    def on_reset(self, event=None):
        # stop any running algorithm loop
        self.stop_requested = True

        print("\nResetting view...")
        self.grid = self.make_grid()
        draw_grid(self.grid, algo=f"{self.current_scenario} Scenario")

    def on_exit(self, event=None):
        # stop any running algorithm loop then close
        self.stop_requested = True
        print("\nExiting...")
        plt.close(self.fig)

    def on_key(self, event):
        if event.key == "r":
            self.on_run()
        elif event.key == "c":
            self.on_reset()
        elif event.key == "q":
            self.on_exit()


if __name__ == "__main__":
    app = App()
    plt.show()
