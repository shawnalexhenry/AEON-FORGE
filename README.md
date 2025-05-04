PROJECT: Aeon/Forge – Procedural Tectonic Simulation Engine
VERSION: Tactical Runtime Core – v0.2.4 (StratumGrid Prototype)
OWNER: @shawn.alexhenry
DESCRIPTION:
  Aeon/Forge simulates tectonic uplift, stress dynamics, terrain evolution, and plate interactions over geological time.
  One tick = 100 years. Each grid cell = 10 km. Engine supports tactical field simulation across heat, pressure, and stress domains.
  Built for runtime integration, not just simulation snapshots.

CORE MODULES:
  /engine/         – Core simulation engine (plate logic, tick loop, field states)
  /visualization/  – Flat shader visualizer (stress = yellow, heat = red, hybrid = purple)
  /data/           – Plate definitions, seed terrain states, evolution logs
  /logs/           – Tactical state logs, simulation metadata

KEY CONFIGS:
  Grid: 512 x 512
  Tick granularity: 100 years/tick
  Units: km (space), years (time)
  Origin: Top-left (0,0)

RUNTIME TRAITS:
  - Tick logging enabled
  - Plate/terrain delta state inspector (logs every mutation)
  - Hybrid overlay toggles per-field
  - Defensive terrain smoothing and uplift dampening (WIP)

HANDOFF NOTES:
  - Engine is modularized and tick-isolated: extendable per-domain
  - No GPU needed; runs in flat NumPy logic
  - Visualization maps can be adapted to Blender or Godot runtime (see export pipeline)
  - Set `run_engine.py` to launch full tectonic evolution sequence
