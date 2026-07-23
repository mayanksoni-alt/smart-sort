# Smart Sort Project Handoff

## Vision

Build a personal desktop assistant called **Smart Sort**.

Goal: - Runs silently in the background. - Watches folders (starting
with Downloads). - Automatically organizes files into folders based on
rules. - Eventually uses AI to understand filenames and document
contents. - Learns from user corrections.

This is **not** a ChatGPT clone. It is an AI-powered file organization
assistant.

------------------------------------------------------------------------

# Development Philosophy

-   Build one small milestone at a time.
-   Understand every tool before writing code.
-   Do not copy tutorial code blindly.
-   Treat this like a real software project.

------------------------------------------------------------------------

# Long-Term Roadmap

Version 0.1 - Watch Downloads folder. - Detect new files. - Print
filename.

Version 0.2 - Move files by extension.

Version 0.3 - Read rules from JSON.

Version 0.4 - Background service.

Version 0.5 - Menu bar app.

Version 1.0 - AI classification. - PDF content understanding. - Learning
from corrections. - Natural-language search.

------------------------------------------------------------------------

# Planned Project Structure

smart-sort/ ├── src/ │ ├── main.py │ ├── watcher.py │ ├── sorter.py │
└── mover.py ├── config/ │ └── rules.json ├── logs/ ├── tests/ ├──
README.md ├── requirements.txt └── venv/

------------------------------------------------------------------------

# Technologies

Language - Python

Libraries - watchdog (folder monitoring) - pathlib (paths) - shutil
(move/copy files) - json (rules)

Later - SQLite - PySide6 - Gemini/OpenAI API

------------------------------------------------------------------------

# What Each Tool Does

Python - Main controller.

watchdog - Watches folders. - Receives file-created events.

pathlib - Reads filenames, extensions, paths.

shutil - Moves files.

JSON - Stores customizable sorting rules.

------------------------------------------------------------------------

# Architecture

File Created ↓ watchdog ↓ Python ↓ Classifier ↓ Destination Finder ↓
Mover ↓ Done

Later:

File Created ↓ watchdog ↓ Filename Analysis ↓ PDF Reader ↓ AI Classifier
↓ Move File ↓ Learning Database

------------------------------------------------------------------------

# Current Progress

Completed: - Created project folder. - Initialized Git repository. -
Learned why virtual environments exist. - Fixed Python environment
issues. - Removed Anaconda interference. - Created working virtual
environment. - Installed watchdog successfully.

Verified: - python points to project venv. - pip points to project venv.

No application code has been written yet.

------------------------------------------------------------------------

# Important Lessons Learned

-   Multiple Python installations can conflict.
-   Always verify:
    -   which python
    -   which pip
-   Virtual environments isolate dependencies.
-   watchdog uses OS file events instead of polling.

------------------------------------------------------------------------

# Next Milestone

Goal: Detect a newly downloaded file.

Expected output:

📄 New file detected: DSA Notes.pdf

No moving files yet.

------------------------------------------------------------------------

# Coding Rules

1.  One feature at a time.
2.  Every milestone should be testable.
3.  Commit after every milestone.
4.  Understand before coding.
5.  AI comes only after the rule-based sorter works.

------------------------------------------------------------------------

# Role of the Assistant

Act as a senior engineer: - Explain concepts. - Review architecture. -
Ask design questions. - Avoid giving full solutions immediately. - Help
the user understand every component.

This document is intended as a handoff so any AI or future chat can
continue the project with full context.
