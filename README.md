# Exercism

My solutions to [Exercism](https://exercism.org) exercises, solved locally with
a professional Python toolchain.

## Layout

```text
.
├── .editorconfig             # Basic formatting rules for any editor
├── .gitattributes            # Line-ending rules for Git
├── .gitignore                # Files Git must not track
├── .pre-commit-config.yaml   # Checks that run before every commit
├── .vscode/                  # VS Code settings for this workspace
└── python/
    ├── .venv/                # Virtual environment (not tracked)
    ├── pyproject.toml        # Tool configuration and dev dependencies
    └── <exercise>/           # One folder per exercise
        ├── README.md         # Instructions
        ├── <exercise>.py     # The solution: the only file to edit
        └── <exercise>_test.py
```

## Tools

| Tool       | Purpose                                         |
| ---------- | ----------------------------------------------- |
| exercism   | Downloads exercises and submits solutions       |
| pytest     | Runs the tests                                  |
| mypy       | Checks type annotations (strict mode)           |
| ruff       | Lints and formats the code (PEP 8)              |
| pre-commit | Runs ruff and mypy automatically on each commit |

## Setup

Only needed on a new machine or after deleting `python/.venv`:

```bash
cd python
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --group dev
pre-commit install
```

## Workflow

Run from the repository root with the virtual environment active
(`source python/.venv/bin/activate`):

```bash
# 1. Download the exercise
exercism download --track=python --exercise=<exercise>
cd python/<exercise>

# 2. Edit <exercise>.py, then check it until all three pass
pytest
mypy .
ruff check .

# 3. Submit the solution
exercism submit

# 4. Save it in the Git history
git add -A
git commit -m "Solve <exercise>"
```

## Conventions

- Code, comments and commit messages are written in English.
- Every function has type annotations.
- Style follows PEP 8, enforced by Ruff.
- Commit messages use the imperative mood, start with a capital letter, have
  no trailing period and stay under 50 characters: `Solve hello-world`.
- One commit per solved exercise.
