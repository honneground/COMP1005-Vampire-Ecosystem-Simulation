# Vampire and Human Population Simulation

- **Unit**: Fundamentals of Programming (`COMP1005` / `FOP1005`) — Assignment 2
- **Study Period**: 2022 Trimester 3A
- **Degree Programme**: Bachelor of Information Technology — Awarded with Distinction by Curtin University
- **Overall Unit Mark**: 92 (High Distinction)

> **README for Assignment Submission**: [README for Assignment Submission](ORIGINAL_README.md)

## Assignment context

The assignment uses a fictional vampire takeover to explore simulation, object-oriented design, visualization and experimental comparison. Humans and vampires move through a two-dimensional world with food, water and garlic. The accompanying author report examines how different initial populations affect infection and survival; the user guide documents parameters and batch runs.

The submitted implementation models movement and nearby interactions over discrete timesteps, records events and prints the surviving human/vampire populations. The included parameter sweep and selected output support the report's comparisons.

## Model and implementation

- `Entities.py` defines common entity position/classification/display properties, ingestible resources and creatures with age, health and movement rules.
- Each timestep chooses a random valid displacement inside the world. Humans use a movement allowance of 4 and vampires 8; the final option chooses an exact or up-to allowance.
- Human health decreases with time. Food, water and garlic restore health when encountered.
- Nearby humans can help one another or transfer health. A vampire/human encounter can infect the human or eliminate the vampire; vampire/vampire interactions reduce health.
- `main.py` initializes entities, runs movement and interaction phases, counts events and optionally draws the world with Matplotlib.
- `vampireSweeps.sh` repeats runs over inclusive ranges of initial human and vampire counts, collecting each run's final population line into CSV.

The creatures use randomized movement. Resources are created during initialization and marked consumed by interactions.

## Run a simulation

Use Python 3 and Matplotlib. From this project directory:

```bash
python3 -m pip install matplotlib
python3 main.py
```

The optional positional arguments, in order, are:

```text
python3 main.py [humans] [vampires] [timesteps] [plot Y/N] [exact movement Y/N]
```

Defaults are 100 humans, 10 vampires, 50 timesteps, plotting enabled and exact movement enabled. For a smaller displayed run:

```bash
python3 main.py 20 2 10 Y Y
```

To skip frame plotting:

```bash
python3 main.py 20 2 10 N Y
```

Matplotlib is required in both modes. Configure the world dimensions through the constants in `main.py` (`XMAX = 75`, `YMAX = 125`).

## Parameter sweeps and outputs

The Bash script accepts:

```text
bash vampireSweeps.sh [lowest humans] [highest humans] [lowest vampires] [highest vampires] [timesteps] [plot Y/N]
```

For six non-plotting runs:

```bash
bash vampireSweeps.sh 10 12 1 2 10 N
```

With no arguments, the ranges are 10–40 humans and 1–5 vampires, with 50 timesteps and plotting enabled. Initial/final map figures are written to `Graphs/` when plotting is enabled. The sweep writes a range-named `simulation*.csv` with initial and final populations; the included `simulation10-40-1-5.csv` is a historical output example.
