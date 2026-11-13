# Dixon-Coles in Modern Football: A Contemporary Statistical Evaluation

## 1. Project Overview

Classical football score models provide a statistical framework for estimating
match outcome probabilities. This project investigates whether the approach of
Dixon and Coles (1997) remains effective in contemporary European football,
beginning with the Premier League and subsequently extending to other leagues.
The intended outputs are a reproducible statistical investigation and an academic
paper in English.

The study is a contemporary evaluation inspired by *Modelling Association Football
Scores and Inefficiencies in the Football Betting Market* (Dixon & Coles, 1997),
not an exact replication of the original paper's historical experiments.

## 2. Research Objectives

The investigation will address four questions:

- Does Dixon-Coles improve football score probability estimates compared with an independent Poisson model?
- Does temporal weighting improve predictive performance?
- How do model performance and assumptions vary across European leagues and seasons?
- Are the models well calibrated on unseen matches?

Comparisons with betting markets may form a secondary analysis; they are not the
primary research objective.

## 3. Dataset

The data source is [Football-Data.co.uk](https://www.football-data.co.uk/), which
provides historical football results and betting odds. Seven Excel files are
currently stored locally in `data/raw/`, covering seasons **2020/21–2026/27**.
The supplied data includes match dates, teams, final scores, and historical
betting odds. Field availability and data quality have not yet been audited.

The **2026/27 season is ongoing** and will be treated separately from completed
seasons. No dataset statistics or quality assessment are reported at this stage.

## 4. Methodology — Planned

The planned comparison comprises an independent Poisson model, a Dixon-Coles
model, and a temporally weighted Dixon-Coles model. Chronological validation will
be used to assess predictions on unseen matches. Planned evaluation includes
probability calibration, log loss, ranked probability score, and statistical
uncertainty around performance estimates and comparisons.

These methods have not yet been implemented or evaluated. Detailed modelling,
validation, and uncertainty estimation procedures remain to be established.

## 5. Technology Stack

The project uses Python 3.12 (initial environment: **3.12.12**) and Jupyter for
notebook-based research. pandas, NumPy, SciPy, and openpyxl support data handling
and numerical computation; penaltyblog and scikit-learn support modelling and
evaluation; matplotlib and seaborn support visualization; pytest supports testing.

Direct dependency versions are pinned in `pyproject.toml`. The exact installed
versions, including transitive dependencies and build tools, are recorded in
`requirements.lock.txt`.

## 6. Project Structure

The current structure is shown below, omitting Git internals, caches, and generated
package metadata. Local datasets and the PDF are shown for orientation and are
not intended for repository distribution.

```text
.
├── .venv/                         # Local Python environment
├── .vscode/
│   ├── extensions.json
│   └── settings.json
├── data/
│   ├── raw/
│   │   ├── .gitkeep
│   │   ├── all-euro-data-2020-2021.xlsx
│   │   ├── all-euro-data-2021-2022.xlsx
│   │   ├── all-euro-data-2022-2023.xlsx
│   │   ├── all-euro-data-2023-2024.xlsx
│   │   ├── all-euro-data-2024-2025.xlsx
│   │   ├── all-euro-data-2025-2026.xlsx
│   │   └── all-euro-data-2026-2027.xlsx
│   └── processed/
│       └── .gitkeep
├── docs/
│   ├── .gitkeep
│   └── Modelling Association Football Scores and Inefficiencies in the Football Betting Market.pdf
├── notebooks/
│   └── .gitkeep
├── paper/
│   └── .gitkeep
├── results/
│   ├── figures/
│   │   └── .gitkeep
│   └── tables/
│       └── .gitkeep
├── src/
│   └── dixon_coles_modern/
│       └── __init__.py
├── tests/
│   └── test_environment.py
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── requirements.lock.txt
```

## 7. Getting Started

Run commands from the project root on macOS/Linux. To use the existing environment:

```bash
source .venv/bin/activate
```

For a fresh checkout, first create the environment using Python 3.12.12:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install the recorded dependencies and the local package:

```bash
python -m pip install -r requirements.lock.txt
python -m pip install --no-deps --no-build-isolation -e .
```

In VS Code, open the project folder and install the recommended Python and Jupyter
extensions. Use **Python: Select Interpreter** to choose `.venv/bin/python`.
When opening a notebook, use its kernel picker to select **Python Environments**
and the same interpreter. No research notebooks have been created yet.

The existing environment also has a kernel named **Python (dixon-coles-modern)**.
To recreate this optional environment-local registration after rebuilding `.venv`:

```bash
python -m ipykernel install --sys-prefix --name dixon-coles-modern --display-name "Python (dixon-coles-modern)"
```

Run the minimal environment smoke tests:

```bash
python -m pytest
```

Alternatively, start JupyterLab with `python -m jupyterlab`. Use `deactivate` to
leave the environment. All installations should remain inside `.venv`.

## 8. Research Progress

- [x] Project initialization
- [x] Raw data collected
- [x] Original paper added to local documentation
- [ ] Data quality audit
- [ ] Exploratory data analysis
- [ ] Statistical modelling
- [ ] Model evaluation
- [ ] Robustness analysis
- [ ] Scientific manuscript

Collection indicates local file availability, not validated data quality or
complete coverage of the ongoing season. No scientific analysis is complete.

## 9. References

Dixon, M. J., & Coles, S. G. (1997). *Modelling Association Football Scores and
Inefficiencies in the Football Betting Market*. Journal of the Royal Statistical
Society: Series C (Applied Statistics), 46(2), 265–280.

Football-Data.co.uk. *Historical football results and betting odds*.
[Data source](https://www.football-data.co.uk/data.php).

## 10. Data Availability and Reproducibility

Raw Excel datasets in `data/raw/` and the original paper PDF in `docs/` are stored
locally and are not intended for redistribution through this repository. Obtain
source materials from their respective providers and place them in the documented
local directories. No licensing or redistribution permissions are asserted here.

The repository records the Python version, dependency versions, package structure,
and environment smoke tests. The dependency lock captures the initial environment;
other operating systems or architectures may require a different resolution.
Data provenance, preparation procedures, and analysis reproduction instructions
will be documented as those stages are developed. No complete analysis workflow
is available yet.
