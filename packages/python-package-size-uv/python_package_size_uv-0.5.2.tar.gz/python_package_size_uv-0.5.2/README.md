# Recursive Package Size

This is a fork of https://github.com/qertoip/python-package-size.  

The main difference to the original is that this fork uses [uv](https://github.com/astral-sh/uv) instead of pip for temporarily installing the packages, which boost performance by a lot.

Learn after-install weight of any Python package including its dependencies.

The tool will **loop over your project dependencies**, install each dependency in its own venv and report the actual size including dependency tree.

This is useful for optimizing dependencies of your large applications, libraries or containers.

This is **especially useful in machine learning** context, where dependencies easily explode into gigabytes.

## Installation

- pip: `pip install python-package-size-uv`
- pix: `pipx install python-package-size-uv`

## Usage

`python-package-size-uv -r pyproject.toml`

or

`python-package-size-uv -r requirements.txt`

## Example output

```
Determined package sizes:

        mypy:   43.7 MB
      awscli:   34.0 MB
       black:    6.7 MB
      pylint:    6.5 MB
      pytest:    2.5 MB
```

Additionally, the result is written in a csv file with default name `package_sizes.csv`.