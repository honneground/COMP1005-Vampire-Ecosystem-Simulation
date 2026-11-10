# Vampire and Human Population Simulation

- **Unit**: Fundamentals of Programming (`COMP1005` / `FOP1005`) — Assignment 2
- **Study Period**: 2022 Trimester 3A
- **Degree Programme**: Bachelor of Information Technology — Awarded with Distinction by Curtin University
- **Overall Unit Mark**: 92 (High Distinction)

> **README for Assignment Submission**: [README for Assignment Submission](ORIGINAL_README.md)

<table>
  <thead>
    <tr>
      <th colspan="6">Curtin University &bull; Bachelor of Information Technology</th>
    </tr>
  </thead>
  <tbody>
    <tr align="center" style="font-weight: bold; background-color: #f6f8fa;">
      <td>2022 T3A</td>
      <td>2023 T1A</td>
      <td>2023 T2A</td>
      <td>2023 T3A</td>
      <td>2024 T1A</td>
      <td>2024 T2A</td>
    </tr>
    <tr>
      <td valign="top" style="background-color: #f1f8ff; border: 2px solid #0969da;">
        <abbr title="Fundamentals of Programming (92 HD)"><b>COMP1005</b></abbr><br>
        &bull; <b>&#128073; Vampire Eco</b><br>        &bull; <a href="https://github.com/honneground/COMP1005-Vehicle-Emissions-Analyzer">Emissions</a><br>      </td>
      <td valign="top">
        <abbr title="Data Structures and Algorithms (89 HD)"><b>COMP1002</b></abbr><br>
        &bull; <a href="https://github.com/honneground/COMP1002-StudyHelp-Academic-Network">StudyHelp</a><br>        &bull; <a href="https://github.com/honneground/COMP1002-Advanced-Data-Structures-and-Visualizer">Visualizer</a><br>        <abbr title="Unix and C Programming (90 HD)"><b>COMP1000</b></abbr><br>
        &bull; <a href="https://github.com/honneground/COMP1000-Terminal-Maze-Survival-Game">Maze Survival</a><br>        &bull; <a href="https://github.com/honneground/COMP1000-Terminal-Maze-Darkness-Game">Maze Darkness</a><br>        &bull; <a href="https://github.com/honneground/COMP1000-Bookstore-Transaction-Simulator">Bookstore</a><br>        <abbr title="Introduction to Software Engineering (95 HD)"><b>ISAD1000</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ISAD1000-Software-Testing-and-Pocket-Beast-Game">Pocket Beast</a><br>      </td>
      <td valign="top">
        <abbr title="Unix Systems Programming (88 HD)"><b>COMP2002</b></abbr><br>
        &bull; <a href="https://github.com/honneground/COMP2002-Parallel-Directory-File-Calculator">Dir Calculator</a><br>        <abbr title="Operating Systems (80 HD)"><b>COMP2006</b></abbr><br>
        &bull; <a href="https://github.com/honneground/COMP2006-Customer-Queue-Concurrency-Simulation">Queue Sim</a><br>      </td>
      <td valign="top">
        <abbr title="Database Systems (80 HD)"><b>ISYS2014</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ISYS2014-Relational-Database-Management-System">FootyStats DB</a><br>        <abbr title="Quantitative Techniques for Business (87 HD)"><b>ECOM2001</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ECOM2001-Econometric-Statistical-Analysis-R">Econometric R</a><br>      </td>
      <td valign="top">
        <abbr title="Financial Decision Making (93 HD)"><b>ACCT1002</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ACCT1002-Financial-Decision-Calculators">Finance Tools</a><br>        <abbr title="Human Computer Interface (71 D)"><b>ICTE3002</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ICTE3002-Lumen-Interaction-Design">Lumen UI</a><br>        <abbr title="Engineering Management and Professional Practice (79 D)"><b>MGMT3000</b></abbr><br>
        &bull; <a href="https://github.com/honneground/MGMT3000-Phone-Router-Repurposing-Design">Phone Router</a><br>      </td>
      <td valign="top">
        <abbr title="Capstone Computing Project 1 (94 HD)"><b>ISAD3000</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ISAD3000-CurtinSG-App-Design">CurtinSG UI</a><br>        <abbr title="Capstone Computing Project 2 (95 HD)"><b>ISAD3001</b></abbr><br>
        &bull; <a href="https://github.com/honneground/ISAD3001-CurtinSG-Student-App">CurtinSG App</a><br>        <abbr title="Advanced Computer Communications (88 HD)"><b>CNCO3002</b></abbr><br>
        &bull; <a href="https://github.com/honneground/CNCO3002-Multi-Service-Socket-Server">Socket Server</a><br>      </td>
    </tr>
  </tbody>
</table>


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

---

## Portfolio note

This Git repository was created retrospectively from the original project code, with assistance from OpenAI Codex and Antigravity in curating the repository and writing this README for publication. The initial commit timestamp is backdated to the original coursework submission date, followed by the final release commit.


