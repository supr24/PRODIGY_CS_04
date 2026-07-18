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
