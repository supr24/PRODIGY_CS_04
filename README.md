# keMem

keMem is a lightweight Python project for capturing keyboard input events, buffering them in memory, and writing them to a log file in batches. It is structured as a small modular framework for learning, experimentation, and basic keystroke event processing.

## Project Overview
This project demonstrates a simple architecture for:
- intercepting keyboard events using pynput
- collecting input in an in-memory buffer
- flushing buffered data to disk efficiently
- testing the buffer behavior with unit tests

## Features
- Modular design with separate components for monitoring, buffering, and storage
- Batch writing to reduce frequent disk I/O
- Simple test coverage for buffer logic
- Easy-to-run entry point via the main script

## Project Structure
- src/core/: keyboard monitoring and in-memory buffering logic
- src/processing/: file-writing/storage logic
- tests/: unit tests for the buffer implementation
- keycodes.txt: sample key mapping reference
- log.txt: output log file produced during runtime

## Installation
1. Create and activate a virtual environment:
   - python -m venv .venv
   - .venv\Scripts\activate
2. Install dependencies:
   - pip install -r requirements.txt
3. Run the project:
   - python src/main.py

## Usage
When the program starts, it listens for keyboard input and stores events in a buffer. Once the buffer reaches its configured size, the contents are appended to the log file.

## Testing
Run the unit tests with:
- python -m unittest discover -s tests

## Notes
This project is intended for educational and research-oriented use. Please use it responsibly and only on systems you own or are authorized to test.

## Short GitHub Description
A lightweight Python keystroke monitoring framework that buffers keyboard events in memory and writes them to a log file efficiently.
