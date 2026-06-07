# Installation Guide

## Prerequisites

Before installing the GitHub Activity Generator, ensure you have:

- **Python 3.7 or higher** - [Download here](https://www.python.org/)
- **Git** - [Download here](https://git-scm.com/)
- **pip** - Usually comes with Python

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/raoviveksingh3-ai/git.git
cd git
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python contribute.py --help
```

You should see the help message with available options.

## Setup Git Credentials

For the script to push commits, ensure your Git credentials are configured:

```bash
# Configure git user
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# For SSH (recommended)
# Ensure SSH keys are set up in GitHub: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
```

## Troubleshooting

### "git: command not found"
- Ensure Git is installed and in your system PATH
- Try restarting your terminal after installing Git

### "Python command not found"
- Check your Python installation
- Use `python3` instead of `python` on some systems

### "Permission denied" on Unix/Linux
```bash
chmod +x contribute.py
./contribute.py --help
```

### SSL Certificate Errors
If you encounter SSL certificate errors:

```bash
# For HTTPS repositories
git config --global http.sslverify false  # (Not recommended for security reasons)

# Better: Use SSH keys instead
```

## Next Steps

See [USAGE.md](./USAGE.md) for detailed usage examples.
