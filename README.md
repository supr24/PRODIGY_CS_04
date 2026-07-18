# Modular Keystroke Analytics Framework

An academic software engineering framework designed to demonstrate optimized system input event handling, volatile memory caching pipelines, and structural patterns for endpoint data analytics. 

This project shifts the focus away from basic script utilities toward a production-grade, modular architecture designed to solve performance bottleneck problems (High Disk I/O) associated with continuous telemetry capture.

---

## ─── Core Architecture ───

The framework is decoupled into distinct processing layers to achieve separation of concerns, ensuring that the critical path of input interception is completely isolated from slower input/output (I/O) file system operations.

```text
               [ Hardware / OS Level Input Events ]
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                  src/core/monitor.py                         │
│  - Establishes native operating system event hooks           │
│  - Sanitizes input streams & maps virtual key definitions     │
└──────────────────────────────┬───────────────────────────────┘
                               │ (Sanitized String Token)
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                  src/core/buffer.py                          │
│  - Manages an in-memory (RAM) volatile data cache           │
│  - Evaluates cache limits to prevent memory leaks            │
└──────────────────────────────┬───────────────────────────────┘
                               │ (Thread-Safe Buffer Flush)
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                src/processing/storage.py                     │
│  - Commits aggregated text blocks asynchronously             │
│  - Enforces atomic file writes using UTF-8 streaming         │
└──────────────────────────────────────────────────────────────┘

─── Feature Set ───
Modular Subsystems: Clean breakdown into core abstraction models, processing pipelines, and validation test suites.

Volatile Memory Caching: Implements an in-memory buffer constraint model that holds data in RAM, executing file writes only when the programmatic threshold is reached. This drastically reduces CPU overhead and hard drive degradation.

Virtual Key Code Normalization: Maps structural keys (e.g., Key.space, Key.enter) cleanly using static lookups to ensure legible text logging.

Graceful Signal Interception: Implements keyboard interrupt handlers to automatically flush remaining data out of volatile RAM cache onto the disk prior to process termination.

Automated Testing Suite: Includes isolated unit test models executing data boundary checks, cache capacity triggers, and flush consistency checks.

─── Directory Layout ───
Plaintext
keystroke_analytics/
│
├── .gitignore               # Excludes runtime metrics, dependencies, and data logs from VC
├── README.md                # Engineering documentation and framework layout
├── requirements.txt         # Defined package dependencies
├── keycodes.txt             # Target OS Virtual Key Code mapping reference documentation
│
├── src/                     # Core application source root
│   ├── __init__.py
│   ├── main.py              # Operational runtime execution entrypoint
│   │
│   ├── core/                # Core Event Capturing Engine
│   │   ├── __init__.py
│   │   ├── monitor.py       # Intercepts native API callbacks and translates layouts
│   │   └── buffer.py        # Validates and holds memory queues dynamically
│   │
│   └── processing/          # Storage Operations Engine
│       ├── __init__.py
│       └── storage.py       # Manages file streaming, encoding, and disk structures
│
└── tests/                   # Independent Validation Suite
    ├── __init__.py
    └── test_buffer.py       # Validates volatile buffer behavior and edge cases
─── Verification & Setup ───
Prerequisites
Python 3.10 or higher

Operating system-level permissions allowing global input hooking events (e.g., root access on Linux distributions, or IDE accessibility clearance on macOS).

1. Initialization and Environment Isolation
From the root project directory, spin up a secure virtual python workspace:

Bash
# Create the virtual directory environment
python -m venv .venv

# Activate the workspace environment (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate the workspace environment (Linux / macOS)
source .venv/bin/activate
2. Dependency Resolution
Install the required platform abstraction libraries compiled in the specification manifest:

Bash
pip install -r requirements.txt
3. Executing Automated Test Suites
Run the isolated automated test cases to evaluate core processing layers before runtime operations:

Bash
python -m unittest discover tests
4. Running the Framework Application
Launch the main application deployment module:

Bash
python src/main.py
─── Cybersecurity Context & Extension ───
This software architecture has been created exclusively for academic research. In modern endpoint protection contexts, unmanaged global hooking metrics represent a significant vulnerability.

Future Academic Extensions
For advanced thesis completion, this framework is structured to easily support the integration of:

Keystroke Biometric Verification: Upgrading monitor.py to calculate typing flight/dwell times for identity analysis.

Data Loss Prevention (DLP) Scanners: Intercepting the buffer.py queue to scan for regular expression structural anomalies like unexpected credit card formats before logging.
