# ---------------------------------------------------------
# Tama Prime System — Makefile
# ---------------------------------------------------------

# Python interpreter
PYTHON := python3

# Package name
PKG := tama_prime

# ---------------------------------------------------------
# Installation
# ---------------------------------------------------------

install:
    $(PYTHON) -m pip install -e .

dev:
    $(PYTHON) -m pip install -r requirements.txt

# ---------------------------------------------------------
# Tests
# ---------------------------------------------------------

test:
    $(PYTHON) -m pytest -q

# ---------------------------------------------------------
# CLI Commands
# ---------------------------------------------------------

compute:
    $(PYTHON) -m $(PKG).cli compute --formula $(FORMULA) --n $(N)

plot:
    $(PYTHON) -m $(PKG).cli plot --N $(N) --a0 $(A0) --a1 $(A1)

optimize:
    $(PYTHON) -m $(PKG).cli optimize --N $(N)

# Example:
#   make compute FORMULA=P_sub N=50
#   make plot N=200 A0=0 A1=0
#   make optimize N=300

# ---------------------------------------------------------
# Build & Packaging
# ---------------------------------------------------------

build:
    $(PYTHON) -m build

clean:
    rm -rf build dist *.egg-info

# ---------------------------------------------------------
# Publish to PyPI (optional)
# ---------------------------------------------------------

publish:
    $(PYTHON) -m twine upload dist/*

# ---------------------------------------------------------
# Formatting & Linting
# ---------------------------------------------------------

format:
    black $(PKG)

lint:
    flake8 $(PKG)

# ---------------------------------------------------------
# Convenience
# ---------------------------------------------------------

run:
    $(PYTHON) -m $(PKG).cli $(ARGS)

# Example:
#   make run ARGS="compute --formula T_prime --n 100"
