# AEON/Forge – Procedural Tectonic Simulation Engine

**Version**: Tactical Runtime Core `v0.2.4` (StratumGrid Prototype)  
**Author**: [@shawnalexhenry](https://github.com/shawnalexhenry)  
**Status**: Active Development | Modular | Tick-Based | Fully Loggable

---

## Overview

AEON/Forge is a simulation engine for tectonic uplift, stress dynamics, and terrain evolution over geological time.

- **Time Scale**: 1 tick = 100 years  
- **Grid Scale**: 512 x 512 (1 cell = 10 km²)  
- **Domains**: Heat, Stress, Terrain Deformation  
- **Output**: NumPy + Log-based, Shader-ready visual fields

---

## Architecture

- `engine/` – Core simulation loop: plates, uplift, pressure tick logic  
- `visualization/` – Field shader overlays (stress = yellow, heat = red, hybrid = purple)  
- `data/` – Plate seed data, evolution logs, runtime deltas  
- `logs/` – Tactical mutation logs and evolution summaries  

---

## Runtime Traits

- Tick-isolated mutation tracking  
- Overlay toggle system  
- Uplift dampening + heat smoothing (WIP)  
- Future: terrain export + 3D preview  

---

## Running the Engine

```bash
python run_engine.py
