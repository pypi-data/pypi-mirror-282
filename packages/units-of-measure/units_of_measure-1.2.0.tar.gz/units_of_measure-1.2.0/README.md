# Units of Measure

as defined in [Unit of Measurement](https://en.wikipedia.org/wiki/Unit_of_measurement).

- Python library: [`units-of-measure`](https://pypi.org/project/units-of-measure/)
- Python package: [`unitsofmeasure`](https://github.com/gerald-scharitzer/units-of-measure/tree/main/unitsofmeasure)

# Objectives

1. Relate units of measure to the [International System of Units (SI)](https://www.bipm.org/en/measurement-units/) to define their dimension and magnitude.
2. Relate objects to units without changing the objects.
3. Get the unit that an object is mapped to.
4. Give units human-readable symbols and names, and computable attributes.
5. Being mapped to a unit shall not keep an object from being garbage-collected.
6. Provide SI units and prefixes.

# Motivation

First, I used the library [`forallpeople`](https://github.com/connorferster/forallpeople),
but that ran into [issues with large scales](https://github.com/connorferster/forallpeople/issues/27) like megatonnes and gigatonnes.

Based on my [objectives](#objectives) I decided to create a new library that does exactly that and does not deal with quantities (yet).

# Limits

Some types of objects like `int` and `float` cannot be mapped to units, because that would create error-prone states.

Not all accepted SI units are implemented.

# Get Started

To start from the beginning, open the [Jupyter notebook](https://jupyter-notebook.readthedocs.io/en/latest/) [`start_here.ipynb`](start_here.ipynb).
This link is relative, so it might not work in all contexts.

There is no dependency to the package `jupyter`, neither at buildtime nor at runtime.
Consequently this library does not declare `jupyter` as dependency.
You can view the notebook on [GitHub](https://github.com/gerald-scharitzer/units-of-measure/blob/main/start_here.ipynb) or in [Visual Studio Code](https://code.visualstudio.com/).
Beyond that there are several alternatives to view notebooks.
If you want to run or edit it, then you need something like [package `jupyter`](https://pypi.org/project/jupyter/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Download and install the library with `python -m pip install units-of-measure`.

# Develop

1. Clone with `git clone https://github.com/gerald-scharitzer/units-of-measure.git`
2. Set up with `python -m pip install -r requirements.txt`
3. Test with `pytest`
4. Document with `pydoc -w unitsofmeasure`
5. Build with `python -m build`
6. Check with `python -m twine check dist/*`
7. Publish with `python -m twine upload dist/*`

# Release Notes

## Release 1.2

- [new decimal prefixes](https://www.bipm.org/en/cgpm-2022/resolution-3) defined in 2022

## Release 1.1

- totally ordered prefixes
- type and value checks in constructors
- dimension symbols and names
- `pyproject.toml` and `hatchling` instead of `setuptools`
