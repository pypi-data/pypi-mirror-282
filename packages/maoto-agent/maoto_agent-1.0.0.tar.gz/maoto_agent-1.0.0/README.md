# Maoto Agent Module

## Build locally with pip
```bash
pip install pip setuptools wheel
python -m maoto-env maoto-env
source maoto-env/bin/activate
pip install -e .
```

## Publishing to PyPI
Create file in home directory `~/.pypirc` with:

```pypirc
[distutils]
index-servers =
    pypi

[pypi]
username = Maoto
password = <your-password>
```

Build the package
```bash
pip install build twine
python -m build
twine upload dist/*
```

## Publish to Homebrew

Add the formula to a tap or submit it to Homebrew core.


## Publish to Conda
```bash

```