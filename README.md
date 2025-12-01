# Scarper (PDF download)

A Python project for downloading PDF files using Selenium WebDriver with Chrome in headless mode.

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer
- Google Chrome browser installed

## Setup

1. **Install uv**:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Create a virtual environment and install dependencies**:

```bash
uv venv
source .venv/bin/activate
uv sync
```

## Usage

2. **Run the main script**:

```bash
uv run main.py
```

Or with the virtual environment activated:

```bash
python main.py
```

The script will download PDF files from specified URLs and save them to the `downloads` directory.

You can download other PDFs by modifying the following line `main.py`:

```python
download_file("your-pdf-url-here.pdf", driver)
```

## Project Structure

```
.
├── Classes/
│   └── Selenium.py          # Selenium WebDriver wrapper class
├── downloads/               # Downloaded files directory (auto-created)
├── main.py                  # Main script with download functionality
├── pyproject.toml          # Project dependencies and metadata
├── .python-version         # Python version specification
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Features

- **Headless Chrome**: Runs without a visible browser window
- **Custom Download Directory**: Saves files to the `downloads` folder
- **SSL Certificate Handling**: Ignores certificate errors for testing purposes
- **Auto-Retry**: Attempts downloads up to 4 times if needed

