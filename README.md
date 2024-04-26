# srt-to-vtt

Python package to enable easy conversion of .srt files to .vtt files.

## Install

srt-to-vtt is available at https://pypi.org/project/srt-to-vtt/ and you can install the latest version with
```
pip install srt-to-vtt
```

## Basic usage

```python
from srt_to_vtt import srt_to_vtt

path_to_my_srt_file = "example.srt"
path_to_converted_vtt_file = "output.vtt"

#converts example.srt into output.vtt
srt_to_vtt(path_to_my_srt_file, path_to_converted_vtt_file)
```

## Develop

Clone this repo and then, at the root, install the package in ediable mode with
```
pip install -e .
```
You can now make changes to the package source code found in `srt-to-vtt/srt_to_vtt/` and see them reflected immediately.

## Build, test and distribute

Before doing anything else, make sure to bump the version number under `[project]` in `pyproject.toml`. Please use [semantic versioning](https://semver.org/).


### Build
First, install the build requirements with
```
pip install -r build_requirements.txt
```

Then, to build, run
```
python -m build
```

### Test

After building the package, install it with

```
pip install dist/srt_to_vtt-#.#.#-py3-none-any.whl
```

You may now run any of the tests found in the `tests/` directory.

### Distribute

Assuming that all the tests are passing, the package is now ready to be released on PyPI.

First, ensure that the files to be uploaded are correct with
```
twine check dist/*
```

Then upload to PyPI with
```
twine upload dist/*
```