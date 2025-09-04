# ⚡ RepoSmith [![PyPI version](https://img.shields.io/pypi/v/reposmith-tol)](https://pypi.org/project/reposmith-tol/) [![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![Sponsor](https://img.shields.io/badge/Sponsor-💖-pink)](https://github.com/sponsors/liebemama)



**RepoSmith** is a portable Python library & CLI tool that helps you **bootstrap new projects instantly**.  
With one command, you get a ready-to-code environment including virtualenv, config files, VS Code setup, `.gitignore`, and license.

---

## ✨ Features

- 🚀 **Quick project setup** with a single command  
- 🐍 **Python ≥ 3.12** support  
- 📦 **Automatic virtual environment** creation (`.venv`)  
- 📄 Generates essential files:
  - `setup-config.json`
  - `requirements.txt`
  - `app.py`
  - `.vscode/` (settings + launch config)
  - `.gitignore`
  - `LICENSE` (MIT by default)
- 🤖 Preconfigured **GitHub Actions workflow**  
- 🛡️ Built-in license templates (MIT)  


---

## ⚡ Quick Start

The fastest way to bootstrap a new project:

```powershell
cd MyProject
py -m reposmith.main
```

This will:
- create `.venv/`
- add `requirements.txt`, `app.py`, `.gitignore`, `LICENSE`, `.vscode/`
- configure everything automatically with defaults.

👉 Optional flags:
- `--ci create` → add GitHub Actions workflow
- `--author "YourName"` → set your name in LICENSE

---

## 📦 Installation

### From source (local dev)
```bash
git clone https://github.com/TamerOnLine/RepoSmith.git
cd RepoSmith
pip install -e .
```

### From GitHub (direct)
```bash
pip install "git+https://github.com/TamerOnLine/RepoSmith.git@main"
```

---

## 🚀 Usage

### CLI
```bash
# Create new project structure in current folder
reposmith --ci create --gitignore python --author "Tamer"

# Or via module syntax (always works)
py -m reposmith.main --ci create --gitignore python --author "Tamer"
```

### Options
```
--ci {skip|create|force}    Configure GitHub Actions workflow
--ci-python VERSION         Python version for CI (default: 3.12)
--gitignore {python|node|django}
--license MIT  License type (only MIT supported for now)
--author NAME               Author name for LICENSE
--year YYYY                 Year in LICENSE header
--root PATH                 Target project root (absolute/relative)
```

---

### Example
```bash
cd MyNewProject
reposmith --ci create --gitignore django --license MIT --author "Tamer"
```

Generates:
```
MyNewProject/
├── .venv/
├── .vscode/
│   ├── settings.json
│   ├── launch.json
├── app.py
├── requirements.txt
├── setup-config.json
├── .gitignore
├── LICENSE
└── .github/workflows/test-main.yml
```

---

## 🧩 Library API

You can also use RepoSmith programmatically:

```python
from reposmith.venv_utils import create_virtualenv, upgrade_pip, install_requirements

venv_dir = "./.venv"
req_file = "./requirements.txt"

create_virtualenv(venv_dir)
upgrade_pip(venv_dir)
install_requirements(venv_dir, req_file)
```

---

## 🛡️ License
This project is licensed under the [MIT License](LICENSE).
© 2025 TamerOnLine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


---

## 💖 Support this project

If you find **RepoSmith** useful, consider supporting its development by becoming a sponsor.  
Your support helps us maintain infrastructure and continue building open-source tools.

👉 [Sponsor us on GitHub](https://github.com/sponsors/liebemama)
