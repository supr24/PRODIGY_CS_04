# Keystroke Analytics Framework

An academic framework designed to safely capture, buffer, and log keyboard input events. This project demonstrates optimized I/O caching to mitigate performance overhead and introduces an architectural foundation for analyzing keystroke behaviors.

## Project Architecture
The project is built modularly to separate low-level input hooking from storage logic:
- `src/core/`: Intercepts system events and manages the volatile memory cache.
- `src/processing/`: Commits optimized chunks of data to disk.
- `tests/`: Holds unit tests to verify data integrity.

## Installation & Setup
1. Create a virtual environment: `python -m venv .venv`
2. Activate it and install dependencies: `pip install -r requirements.txt`
3. Execute the project framework: `python src/main.py`

## Supported Inputs
Refer to `keycodes.txt` for the baseline definitions mapped from the system's virtual key layout.