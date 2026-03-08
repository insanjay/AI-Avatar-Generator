# AI Avatar Generator

A Python project for generating AI-powered avatars with text-to-speech capabilities.

## Requirements

- Python 3.12+
- Dependencies:
  - `pyttsx3`: Text-to-speech synthesis library
  - `gTTS`: Google Text-to-Speech library

## Setup Instructions

Choose one of the following setup methods based on your preference:

### Option 1: Using `uv` (Recommended)

`uv` is a fast Python package installer and resolver. It's the recommended approach for this project.

1. **Install `uv`** (if not already installed):
   ```bash
   pip install uv
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

This command will read the `pyproject.toml` file and install all dependencies in a virtual environment.

### Option 2: Using `pip`

If you prefer the traditional pip approach:

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Dev Container Setup

For a containerized development environment using VS Code Dev Containers:

1. Install the "Dev Containers" extension in VS Code
2. Open the project folder in VS Code
3. Click on the green icon in the bottom-left corner and select "Reopen in Container"

The dev container automatically:
- Sets up Python 3.12
- Installs `uv` and runs `uv sync`
- Configures VS Code with Python and Pylance extensions

## Project Structure

- `pyproject.toml`: Project metadata and dependency definitions
- `requirements.txt`: Pinned dependencies for pip installation
- `.devcontainer/`: Dev container configuration
- `main.py`: Main application entry point

## Usage

```bash
python main.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

MIT License - See LICENSE file for details
