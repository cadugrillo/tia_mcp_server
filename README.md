
# TIA MCP Server

    This project is a Python application managed with [uv](https://github.com/astral-sh/uv) and requires Python 3.13.

## Quick overview

    - Entry point: `main.py` (calls `mcp.run(...)` in `server.py`).
    - Dependency manager: `uv` with `pyproject.toml` and `uv.lock` present.

## Prerequisites

1. Install Python 3.13
    - Download from https://www.python.org/downloads/ and install. On Windows, check "Add Python to PATH" in the installer.

2. (Optional but recommended) Install Docker if you plan to run the Docker image. A `Dockerfile` is included.

## Setup — create and use a virtual environment

    It is recommended to create a virtual environment per-project. Examples below show PowerShell, Command Prompt (cmd.exe), and macOS/Linux shells.

    Windows (PowerShell)
    ```powershell
    # Create venv
    python -m venv .venv

    # If you get a script execution error when enabling the venv, run this once in the same session:
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

    # Activate the venv
    .\.venv\Scripts\Activate.ps1

    # Upgrade pip and install uv
    python -m pip install --upgrade pip
    pip install uv

    # Sync dependencies from uv.lock (preferred)
    uv sync

    # Alternatively, if your project provides a requirements file you can use:
    uv pip install -r requirements.txt
    ```

    Windows (Command Prompt)
    ```cmd
    python -m venv .venv
    .\.venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    pip install uv
    uv sync
    ```

    macOS / Linux
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    pip install uv
    uv sync
    ```

    Notes about `uv sync`:
    - `uv sync` reads your lockfile (`uv.lock`) and installs pinned versions into the active environment. This is the preferred way to reproduce a known-good environment.
    - If you change dependencies in `pyproject.toml`, update the lock with `uv lock` (or your normal `uv` workflow) and then run `uv sync` on other machines.

    ## Running the application

    With the virtual environment active you can run:

    ```bash
    uv python main.py
    # or, with the venv active, simply
    python main.py
    ```

    The server uses an MCP transport; `main.py` currently calls `mcp.run(transport="streamable-http")`. Adjust runtime flags or env vars as needed for your deployment.

    ## Docker (optional)

    A `Dockerfile` is provided for building a container image. Build and run (example):

    ```powershell
    # build (from repository root)
    docker build -t tia-mcp-server:latest .

    # run and map port 8000 (adjust if your app uses another port)
    docker run --rm -it -p 8000:8000 tia-mcp-server:latest
    ```

    ## Git housekeeping

    - Add `__pycache__/` to `.gitignore` to avoid committing compiled bytecode. If caches are already tracked, untrack them with your Git client or the PowerShell command provided in the repository's docs.

    ## Troubleshooting

    - If `uv sync` fails to install packages, ensure the virtual environment is activated and that you have a working internet connection. Check `uv.lock` is present and up to date.
    - On Windows PowerShell, if activation fails due to execution policy, run the `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` command shown above.

    ## Further reading

    - uv: https://github.com/astral-sh/uv
