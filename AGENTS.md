# AGENTS.md

## Repository summary
This repository is a small Pygame + NumPy sliding-torus puzzle game. The “game logic” lives in `board.py`; the UI/game loop and solver entry points live in `sliding.py`; automated checks live in `test_board.py`.

## Commands
- Install dependencies:
  `python -m pip install -r requirements.txt`
- Run the game:
  `python sliding.py`
- Run the full test suite:
  `python -m unittest -v`
- Run a single test:
  `python -m unittest test_board.TestBoardMethods.test_moveboard_right`
- There is no repository-configured linter or formatter in this repo. Validation today is via the unittest suite.

## Architecture
- `board.py`
  - Defines `Direction` with `North`, `South`, `East`, `West`.
  - Implements `Board`, which wraps a NumPy 2D array and mutates it in place.
  - Core methods are `moveboard`, `rotationA`, `rotationB`, `rotationC`, `rotationD`, and `tw`.
  - The torus behavior is intentional: rows and columns wrap via NumPy roll operations, so movement is not bounded by the board edges.
- `sliding.py`
  - Defines `SlidingGame`, which wraps a `Board` instance.
  - Uses the board rotation helpers to animate moves and resolves the puzzle via a custom solver.
  - Takes the grid size from stdin at startup: `n = int(input("Enter Grid Size:"))`.
  - Handles Pygame rendering and keyboard/mouse interaction in the game loop.
- `test_board.py`
  - Uses `unittest` and `np.testing.assert_array_equal`.
  - Covers direct board movement and each corner-rotation variant; these are the most important regression checks for this project.

## Conventions
- Board coordinates follow `[row, col]` indexing.
- Directions are passed as `Direction.East`, `Direction.West`, etc., not raw strings.
- Movement and rotations mutate the underlying NumPy array in place rather than returning a detached board.
- The solver reuses the same board-rotation primitives as the interactive game, so gameplay and solver logic should stay aligned.
- When changing puzzle mechanics, prefer updating or extending `test_board.py` with a focused test over adding unrelated test scaffolding.

## Working style
- Keep puzzle-state mutations in `board.py` unless the change is specifically UI/rendering behavior.
- Avoid duplicating board-move logic in `sliding.py`; prefer reusing the `Board` methods.
- Treat the model as a deterministic state machine: each move should be reproducible and verifiable by a test.