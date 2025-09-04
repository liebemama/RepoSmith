# ⚡ RepoSmith  

[![PyPI version](https://img.shields.io/pypi/v/reposmith-tol)](https://pypi.org/project/reposmith-tol/)  
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)  
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  
[![CI](https://github.com/liebemama/RepoSmith/actions/workflows/test-main.yml/badge.svg)](https://github.com/liebemama/RepoSmith/actions)  
[![Downloads](https://static.pepy.tech/personalized-badge/reposmith-tol?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads)](https://pepy.tech/project/reposmith-tol)  
[![Sponsor](https://img.shields.io/badge/Sponsor-💖-pink?style=for-the-badge)](https://github.com/sponsors/liebema)  

---

**RepoSmith** is a **lightweight & portable Python CLI tool** that helps you **bootstrap new projects instantly** 🚀.  
With a single command, you get a **ready-to-code environment** including:  

- 🧩 Virtualenv (`.venv`)  
- ⚙️ Config files  
- 📦 `requirements.txt`  
- 🖥️ VS Code setup (`.vscode/`)  
- 📜 `.gitignore`  
- 🛡️ License  

---

## ✨ Features
- 🚀 **Quick bootstrap**: create a full project with one command.  
- 🐍 **Python ≥ 3.12** support.  
- 📦 **Automatic virtual environment creation**.  
- 📂 **Essential files generated** out of the box:  
  - `setup-config.json`, `requirements.txt`, `app.py`  
  - `.vscode/` (settings + launch config)  
  - `.gitignore`, `LICENSE`  
- ⚙️ **Preconfigured GitHub Actions** workflow for CI.  
- 🛡️ **MIT License** template built-in.  

---

## 📦 Installation

From PyPI:
```bash
pip install reposmith-tol
```

From source:
```bash
git clone https://github.com/liebemama/RepoSmith.git
cd RepoSmith
pip install -e .
```

---

## ⚡ Usage

### CLI
```bash
# Create a new project structure in the current folder
reposmith --ci create --gitignore python --author "Tamer"
```

### Example
```bash
cd MyNewProject
reposmith --ci create --gitignore django --license MIT --author "Tamer"
```

### Quick Start (PowerShell)
```powershell
cd MyProject
py -m reposmith.main
```

---

## 🧩 Library API
```python
from reposmith.venv_utils import create_virtualenv, upgrade_pip, install_requirements

venv_dir = "./.venv"
req_file = "./requirements.txt"

create_virtualenv(venv_dir)
upgrade_pip(venv_dir)
install_requirements(venv_dir, req_file)
```

---

## 📂 Project Structure

```
MyProject/
├── app.py
├── requirements.txt
├── setup-config.json
├── .gitignore
├── .vscode/
│   └── settings.json
└── venv/
```

---

## 🧪 Development

Clone the repo and install in editable mode:

```bash
git clone https://github.com/liebemama/RepoSmith.git
cd RepoSmith
pip install -e .
```

Run tests and CI locally (or via GitHub Actions).  

---

## 🤝 Contributing

We welcome contributions 🎉  
- Open an **Issue** to discuss ideas.  
- Submit a **Pull Request** to improve features.  
- Check out [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.  

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).  
© 2025 TamerOnLine  

---

## 💖 Support & Sponsor

If you find RepoSmith useful, please consider supporting its development:  
👉 [GitHub Sponsors](https://github.com/sponsors/liebema)  

---
