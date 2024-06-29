# venvpool
Run your Python scripts using an automated pool of virtual environments to satisfy their requirements

## Install
These are generic installation instructions.

### To use, permanently
The quickest way to get started is to install the current release from PyPI:
```
pip3 install --user venvpool
```

### To use, temporarily
If you prefer to keep .local clean, install to a virtualenv:
```
python3 -m venv venvname
venvname/bin/pip install -U pip
venvname/bin/pip install venvpool
. venvname/bin/activate
```

## Commands

### motivate
Create and maintain wrapper scripts in ~/.local/bin for all runnable modules in the given projects, or the current project if none given.

### motivate -S
Create/maintain wrappers for all console_scripts of the given requirement specifier.

### motivate -C
Compact the pool of venvs.
