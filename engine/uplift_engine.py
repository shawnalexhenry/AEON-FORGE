# uplift_engine.py
import numpy as np
import os

class UpliftEngine:
    def __init__(self, grid_size=(512, 512), out_dir="data/"):
        self.grid = np.zeros(grid_size)
        self.out_dir = out_dir

    def apply_uplift(self, magnitude):
        self.grid += magnitude
        return self.grid

    def save_grid(self, tick, fmt="npy"):
        os.makedirs(self.out_dir, exist_ok=True)
        path = os.path.join(self.out_dir, f"uplift_field_tick{tick:03d}.{fmt}")
        if fmt == "npy":
            np.save(path, self.grid)
        elif fmt == "csv":
            np.savetxt(path, self.grid, delimiter=",")
