# GitHub Activity Generator

A Python tool to generate GitHub commit activity for testing, visualization, and development purposes.

## Overview

This project provides utilities to programmatically create commits and contribute to a GitHub repository at specified intervals and frequencies. Useful for:
- Testing GitHub activity tracking
- Generating consistent contribution patterns
- Development and testing purposes
- Learning git workflows

## Features

- Configure custom commit frequencies
- Skip weekends option
- Batch commit generation
- Flexible repository targeting
- Customizable commit intervals

## Installation

1. Clone this repository:
```bash
git clone https://github.com/raoviveksingh3-ai/git.git
cd git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Examples

Generate commits with maximum count and frequency:
```bash
python contribute.py --max_commits=12 --frequency=60 --repository=git@github.com:user/repo.git
```

Generate commits excluding weekends:
```bash
python contribute.py --no_weekends
```

### Command-Line Options

- `--max_commits=N`: Maximum number of commits to generate (default: 10)
- `--frequency=N`: Time interval between commits in seconds (default: 60)
- `--repository=URL`: Git repository URL to target
- `--no_weekends`: Skip commit generation on weekends
- `--help`: Display help information

## Project Structure

```
.
├── README.md
├── .gitignore
├── requirements.txt
├── contribute.py          # Main script
├── docs/                  # Documentation
└── examples/              # Usage examples
```

## Requirements

- Python 3.7+
- Git
- Required Python packages (see requirements.txt)

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Author

Created by [raoviveksingh3-ai](https://github.com/raoviveksingh3-ai)

## Disclaimer

⚠️ This tool is intended for educational and development purposes. Use responsibly and in compliance with GitHub's Terms of Service.
