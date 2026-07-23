# Smart Sort

Smart Sort is a macOS desktop assistant that automatically organizes files in the Downloads folder.

## Current Features

- Watches Downloads in real time
- Sorts files using extension-based categories
- Creates category folders automatically
- Handles duplicate filenames safely
- Starts automatically with a macOS LaunchAgent
- Records successful file moves in SQLite

## Project Structure

```text
config/      Application configuration
database/    Local SQLite database files
src/         Application source code
logs/        Runtime logs
tests/       Automated tests


```

## Current Status

Smart Sort currently sorts by file extension and records successful moves in SQLite.

Next milestone: scan and organize files already present in Downloads when the app starts.

## Long-Term Goal

Learn each user’s personal organization habits and predict where their files belong.