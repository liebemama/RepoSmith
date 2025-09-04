# 📦 Changelog

All notable changes to this project will be documented in this file.  
This project follows [Semantic Versioning](https://semver.org/).

---

## [0.2.0] - 2025-09-04
### Added
- Unified safe file-writing system (`write_file`) across all modules (atomic write + .bak + idempotent).
- CLI now prints state logs for each step (`[requirements]`, `[venv]`, `[pip]`, `[install]`, `[env-info]`, `[entry]`, `[ci]`).
- Fallback in VS Code settings: uses `python.exe`/`python3` if `.venv` not created.
- Config file generator (`setup-config.json`) with defaults.

### Changed
- `main.py` reorganized: no duplication, cleaner flow.
- Default entry file is now `main.py` instead of `app.py`.
- Logging standardized across all utilities.

### Fixed
- License handling: now `license = "MIT"` + `license-files = ["LICENSE"]` (PEP 639 compliant).
- PyPI build errors related to `license` and classifiers.

---

## [0.1.2] - 2025-09-04
### Added
- Auto-backup for GitHub Actions workflow files.

### Changed
- Updated `pyproject.toml` to use `setuptools>=77.0.0`.
- Minor refactoring for better CLI flexibility.

### Fixed
- Improved compatibility with modern `license-files` handling.

---

## [0.1.1] - 2025-09-03
### Added
- Initial packaging with `pyproject.toml`.
- PyPI publishing under the name `reposmith-tol`.
- CLI entry point: `reposmith = reposmith.main:main`.

---

## [0.1.0] - 2025-09-02
### Added
- First working version of **RepoSmith** 🎉.
- Automatic virtualenv creation.
- Generation of essential files:
  - `requirements.txt`, `app.py`
  - `.vscode/` (settings + launch)
  - `.gitignore`, `LICENSE`
- Basic GitHub Actions workflow generator.
