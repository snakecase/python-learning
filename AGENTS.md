# python-learning

A personal Python learning repo: exercises and practice code, not a product.

## Layout
- `automatetheboringstuff/`: practice scripts from *Automate the Boring Stuff with Python*, one folder per chapter.
- `exercism/python/<exercise>/`: Exercism Python track exercises, downloaded and submitted with the `exercism` CLI. `exercism/pytest.ini` registers the `task` marker the tests use.

## How to help here
- This repo is for learning. When asked to check code, review and explain: point out bugs and leftovers with the reason, and show the fix as a snippet. Don't edit or run the learner's files unless asked, and say whether you ran the code.
- Explain concepts briefly and concretely; assume a beginner.

## Running things
- Exercism tests: run pytest from `exercism/` (`cd exercism && pytest`) or as `pytest exercism`. From the repo root pytest doesn't find `exercism/pytest.ini` (it only searches upward), so every `@pytest.mark.task` gives an unknown-mark warning.
- Many Automate the Boring Stuff scripts use `input()`, so run them in a terminal, not VS Code's Debug Console (it can't take input).
- `.gitignore` covers `.exercism/` (local CLI metadata, recreated by `exercism download`), `__pycache__/`, `*.pyc`, `.pytest_cache/` and `*.code-workspace`.
