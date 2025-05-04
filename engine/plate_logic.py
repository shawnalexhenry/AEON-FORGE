# plate_logic.py
import numpy as np
import os

class PlateSimulator:
    def __init__(self, config):
        self.ticks = 0
        self.autosave = config.get("autosave", True)
        self.out_dir = config.get("export_folder", "data/")
        self.out_fmt = config.get("output_format", "npy")

    def simulate_step(self):
        self.ticks += 1
        result = {"tick": self.ticks}
        data = np.full((512, 512), self.ticks, dtype=np.float32)
        if self.autosave:
            os.makedirs(self.out_dir, exist_ok=True)
            path = os.path.join(self.out_dir, f"uplift_field_tick{self.ticks:03d}.{self.out_fmt}")
            if self.out_fmt == "npy":
                np.save(path, data)
            elif self.out_fmt == "csv":
                np.savetxt(path, data, delimiter=",")
        return result
