# Modular Input Event Analytics Framework

> **Academic Software Engineering Project**
>
> A modular framework that demonstrates efficient **system input event processing**, **in-memory buffering**, and **asynchronous storage architecture** for endpoint telemetry research. The project emphasizes clean software design and performance optimization rather than simple scripting.

---

# Overview

This project demonstrates how continuous system-generated input events can be processed efficiently by separating:

- Event monitoring
- Memory buffering
- Storage operations

Instead of writing every captured event directly to disk, the framework temporarily stores processed data in **volatile memory (RAM)** and performs **batched file operations**, significantly reducing disk I/O overhead.

The implementation follows a modular architecture that promotes:

- Separation of concerns
- Maintainability
- Testability
- Extensibility

---

# Architecture

```text
               Hardware / Operating System
                        Input Events
                              │
                              ▼
┌────────────────────────────────────────────────────┐
│                src/core/monitor.py                 │
│----------------------------------------------------│
│ • Registers native input event hooks               │
│ • Normalizes virtual key definitions               │
│ • Produces sanitized event tokens                  │
└──────────────────────────┬─────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────┐
│                 src/core/buffer.py                 │
│----------------------------------------------------│
│ • Stores processed events in RAM                   │
│ • Monitors configurable buffer thresholds          │
│ • Prevents excessive disk writes                   │
└──────────────────────────┬─────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────┐
│            src/processing/storage.py               │
│----------------------------------------------------│
│ • Flushes buffered data                            │
│ • Performs UTF-8 encoded file operations           │
│ • Uses atomic write strategies                     │
└────────────────────────────────────────────────────┘
```

---

# Key Features

## Modular Architecture

The framework is divided into independent layers, allowing each component to perform a single responsibility.

- Event Monitoring Layer
- Buffer Management Layer
- Storage Layer
- Automated Testing Layer

---

## In-Memory Buffering

Instead of writing every event immediately to disk:

- Events are accumulated in RAM.
- Data is written only after the buffer reaches a predefined threshold.
- Reduces disk I/O operations.
- Improves runtime efficiency.
- Demonstrates caching strategies commonly used in high-performance systems.

---

## Virtual Key Normalization

Special keyboard keys are translated into readable representations.

Examples include:

- Space
- Enter
- Tab
- Backspace
- Modifier keys

This improves the readability of stored event data.

---

## Graceful Shutdown Handling

Before program termination:

- Remaining buffered data is flushed safely.
- Prevents accidental data loss.
- Demonstrates proper cleanup procedures.

---

## Automated Testing

The project includes isolated unit tests for validating:

- Buffer capacity
- Flush triggers
- Memory consistency
- Boundary conditions

---

# Project Structure

```text
keystroke_analytics/
│
├── .gitignore
├── README.md
├── requirements.txt
├── keycodes.txt
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── monitor.py
│   │   └── buffer.py
│   │
│   └── processing/
│       ├── __init__.py
│       └── storage.py
│
└── tests/
    ├── __init__.py
    └── test_buffer.py
```

---

# Module Responsibilities

## `monitor.py`

Responsible for:

- Registering operating-system input hooks
- Capturing input events
- Translating raw virtual key codes
- Producing normalized event tokens

---

## `buffer.py`

Responsible for:

- Managing volatile RAM storage
- Maintaining configurable buffer sizes
- Triggering flush operations
- Preventing excessive disk writes

---

## `storage.py`

Responsible for:

- Writing buffered data to persistent storage
- UTF-8 encoding support
- Atomic file write operations
- Storage consistency

---

# Installation

## Prerequisites

- Python **3.10+**
- Required operating system permissions for global input event monitoring
  - Windows
  - Linux
  - macOS (Accessibility permissions)

---

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

Execute the automated validation suite:

```bash
python -m unittest discover tests
```

---

# Running the Application

Start the framework using:

```bash
python src/main.py
```

---

# Performance Design

The project demonstrates an optimized data-processing pipeline.

Traditional approach:

```
Input Event
      ↓
Immediate Disk Write
      ↓
High Disk I/O
```

Framework approach:

```
Input Event
      ↓
Memory Buffer
      ↓
Threshold Reached
      ↓
Single Batch Write
```

### Benefits

- Lower disk activity
- Reduced CPU overhead
- Better scalability
- Improved maintainability
- Cleaner architecture

---

# Testing Coverage

The included unit tests validate:

- Buffer initialization
- Cache threshold behavior
- Flush consistency
- Empty buffer handling
- Boundary conditions
- Memory integrity

---

# Future Enhancements

The architecture is intentionally modular and can be extended with additional capabilities such as:

- Keystroke biometric analysis
- Typing rhythm (flight and dwell time) measurements
- Data Loss Prevention (DLP) pattern scanning
- Event encryption before storage
- Database-backed storage
- Multi-threaded processing
- Cross-platform abstraction layers
- Performance benchmarking
- Logging and monitoring dashboards

---

# Educational Purpose

This project is intended solely for:

- Software engineering education
- Performance optimization research
- Modular architecture demonstrations
- Operating system event-processing concepts
- Endpoint telemetry research

It is designed to illustrate architectural patterns, buffering techniques, and clean software design in a controlled academic environment.

---

# Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- File I/O
- Memory Buffering
- Unit Testing
- Modular Software Architecture

---

# License

This repository is intended for educational and academic purposes only. Users are responsible for ensuring that any experimentation complies with applicable laws, organizational policies, and ethical guidelines.
