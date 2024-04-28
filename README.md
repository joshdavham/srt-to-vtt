[![PyPi](https://img.shields.io/pypi/v/srt-to-vtt)](https://pypi.org/project/srt-to-vtt/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# srt-to-vtt

Python package to enable easy conversion of .srt files to .vtt files.

## Install

srt-to-vtt is available on [PyPI](https://pypi.org/project/srt-to-vtt/) and you can install the latest version with
```
pip install srt-to-vtt
```

## Basic usage

```python
from srt_to_vtt import srt_to_vtt

path_to_my_srt_file = "example.srt"
path_to_converted_vtt_file = "output.vtt"

# converts example.srt into output.vtt
srt_to_vtt(path_to_my_srt_file, path_to_converted_vtt_file)

```

## Develop

Clone this repo and then, at the root, install the package in ediable mode with
```
pip install -e .
```
You can now make changes to the package source code found in `srt-to-vtt/srt_to_vtt/` and see them reflected immediately.

## Format, build, test and distribute

Before doing anything else, make sure to bump the version number under `[project]` in `pyproject.toml`. Please use [semantic versioning](https://semver.org/).



Then, install the build requirements with
```
pip install -r build_requirements.txt
```

### Format

This project adheres to the [Black](https://github.com/psf/black) code style. You can automatically refomat your code to Black by executing the following in the root directory of this repo:
```
black .
```

### Build
Then, to build, run
```
python -m build
```

### Test

After building the package, install it with

```
pip install dist/srt_to_vtt-#.#.#-py3-none-any.whl
```

You may now run the tests by simply executing
```
pytest
```

### Distribute

Assuming that all the tests are passing, the package is now ready to be released on PyPI!

Open a pull request on the main branch and, if approved and merged, the package will be automatically updated on PyPI after the next Release is published on GitHub.