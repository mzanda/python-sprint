# Python Sprint

A scaffolded repository for an 8‑week Python sprint focused on writing **clean, tested, idiomatic Python**.
It includes a standard layout (`src/`, `tests/`, `notebooks/`), tooling (pytest, black, flake8, mypy),
and a GitHub Actions workflow to run tests on every push.

## Quickstart

```bash
# 1) (Recommended) Create a conda env
conda create -n py-sprint python=3.11 -y
conda activate py-sprint

# 2) Install package + dev tools
pip install -e ".[dev]"

# 3) Run tests
pytest -q

# 4) Format & lint
black .
flake8
mypy src
```

## Structure

```
.
├── src/                 # Your Python package code (importable)
│   └── __init__.py
├── tests/               # Pytest test files
│   └── test_smoke.py
├── notebooks/           # Jupyter notebooks (EDA, demos)
│   └── README.md
├── .github/
│   └── workflows/
│       └── python-tests.yml  # CI: runs pytest on push/PR
├── .gitignore
├── pyproject.toml       # Build system & dependencies
└── README.md
```

## Dev Conventions

- **Tests** live in `tests/` and mirror modules in `src/`.
- **Every function gets a test** (even simple ones).
- Use **black** for formatting and **flake8** for linting before commit.
- **Type hints** + **mypy** for stricter code quality.
- CI is set up to run `pytest` on push/PR; extend it as needed.

## Week Folders (optional)
If you prefer, create a folder per week under `src/` (e.g., `src/week1_text_utils/`) with a matching `tests/test_week1_text_utils.py` file.
Keep imports **package‑style**, not relative to scripts.

---

Happy coding! 🚀