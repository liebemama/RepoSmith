# 📦 Changelog

All notable changes to this project will be documented in this file.  
This project follows [Semantic Versioning](https://semver.org/).

---

## [0.2.6] - 2025-09-05
### Added
- Auto-generate `setup-config.json` with sane defaults via `load_or_create_config` + unit tests.  
- Additional smoke tests to run `python -m reposmith.main` with explicit `PYTHONPATH` to prefer local code.

### Changed
- CI workflow generator now ensures CI imports local repo code and uninstalls any shadowing installed package.
- Updated matrix CI (`\.github/workflows/test-main.yml`) to test on 3.12/3.13 across OSes and build/upload artifacts.
- VS Code integration: more robust interpreter fallback when `.venv` is missing.

### Fixed
- Minor CLI/logging refinements and safer idempotent file writes across helpers.

---

## [0.2.5] - 2025-09-04
### Added
- Support for direct `python -m reposmith` execution (module entry).
- More informative console logs during initialization.

### Changed
- Improved `unittest` CI workflow to ensure consistent module discovery.
- Small refinements in CLI argument parsing and help messages.

### Fixed
- Resolved `ModuleNotFoundError: No module named 'reposmith'` in GitHub Actions by adjusting import paths.
- Minor fixes for editable installs on some environments.

---

## [0.2.4] - 2025-09-04
### Changed
- Updated `pyproject.toml` to version `0.2.4`.
- Minor refinements in metadata (`Support`, `Sponsor` links).
- Internal cleanup and docstrings improved.

---

## [0.2.3] - 2025-09-04
### Added
- Extra presets for `.gitignore` (Node, Django).
- Safer handling for `.gitignore` creation with clear console logs.

### Changed
- More robust `create_license` function (explicit messages for overwrite/backup).
- Improved VS Code integration with fallback interpreter detection.

---

## [0.2.2] - 2025-09-04
### Added
- `tests/test_fs.py` with unit tests for atomic file operations.
- Backup handling verification in tests.

### Changed
- Better logging output for each step of project initialization.

---

## [0.2.1] - 2025-09-04
### Fixed
- Adjusted `pyproject.toml` license metadata to be fully PEP 639 compliant.
- Fixed editable install issues with `pip install -e .`.

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

