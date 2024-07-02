<div align="center">

[![PyPI](https://img.shields.io/pypi/v/inquirer3?&color=blue&logo=pypi&logoColor=%23FFFBEF)][pypi status]
[![Downloads](https://static.pepy.tech/badge/inquirer3?color=green)][pypi downloads]
[![Read the documentation at https://python-inquirer3.readthedocs.io/](https://img.shields.io/readthedocs/python-inquirer/latest.svg?label=docs)][read the docs]

[![Tests](https://github.com/guysalt/python-inquirer3/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/guysalt/python-inquirer3/branch/main/graph/badge.svg)][codecov]
[![Python Version](https://img.shields.io/pypi/pyversions/inquirer3.svg)][pypi status]
[![License](https://img.shields.io/pypi/l/inquirer3.svg)][license]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/inquirer3/
[pypi downloads]: https://pepy.tech/project/inquirer3
[read the docs]: https://python-inquirer3.readthedocs.io/
[tests]: https://github.com/guysalt/python-inquirer3/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/guysalt/python-inquirer3
[black]: https://github.com/psf/black

</div>

# python-inquirer3

This is a fork of [magmax/python-inquirer]. This one is hopefully more responsive (Issues/PRs/...).

Collection of common interactive command line user interfaces, based on [magmax/python-inquirer].

### Goal and Philosophy

**inquirer3** should ease the process of asking end user **questions**, **parsing**, **validating** answers, managing **hierarchical prompts** and providing **error feedback**.

## Platforms support

Python-inquirer supports mainly UNIX-based platforms (eq. Mac OS, Linux, etc.). Windows has experimental support, please let us know if there are any problems!

## Installation

Install the last released version using pip:

```sh
pip install inquirer3
```

Also, you can [download the python-inquirer code from GitHub] or [download the wheel from Pypi].

## Documentation

### Text

```python
import re

import inquirer3

questions = [
    inquirer3.Text('name', message="What's your name"),
    inquirer3.Text('surname', message="What's your surname"),
    inquirer3.Text('phone', message="What's your phone number",
                   validate=lambda _, x: re.match('\+?\d[\d ]+\d', x),
                   )
]
answers = inquirer3.prompt(questions)
```

### Editor

Like a Text question, but used for larger answers. It opens external text editor which is used to collect the answer.

The environment variables `$VISUAL` and `$EDITOR`, can be used to specify which editor should be used. If not present inquirer fallbacks to `vim -> emacs -> nano` in this order based on availability in the system.

External editor handling is done using great library [python-editor](https://github.com/fmoo/python-editor).

Example:

```python
import inquirer3

questions = [
    inquirer3.Editor('long_text', message="Provide long text")
]
answers = inquirer3.prompt(questions)
```

### List

Shows a list of choices, and allows the selection of one of them.

Example:

```python
import inquirer3

questions = [
    inquirer3.List('size',
                   message="What size do you need?",
                   choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
                   ),
]
answers = inquirer3.prompt(questions)
```

List questions can take one extra argument `carousel=False`. If set to true, the answers will rotate (back to first when pressing down on last choice, and down to last choice when pressing up on first choice)

### Checkbox

Shows a list of choices, with multiple selection.

Example:

```python
import inquirer3

questions = [
    inquirer3.Checkbox('interests',
                       message="What are you interested in?",
                       choices=['Computers', 'Books', 'Science', 'Nature', 'Fantasy', 'History'],
                       ),
]
answers = inquirer3.prompt(questions)
```

Checkbox questions can take extra argument `carousel=False`. If set to true, the answers will rotate (back to first when pressing down on last choice, and down to last choice when pressing up on first choice)

Another argument that can be used is `locked=<List>`. The given choices in the locked argument cannot be removed. This is useful if you want to make clear that a specific option out of the choices must be chosen.

### Path

Like Text question, but with builtin validations for working with paths.

Example:

```python
import inquirer3

questions = [
    inquirer3.Path('log_file',
                   message="Where logs should be located?",
                   path_type=inquirer3.Path.DIRECTORY,
                   ),
]
answers = inquirer3.prompt(questions)
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Copyright (c) 2014-2023 Miguel Ángel García

Distributed under the terms of the [MIT license][license].

<!-- github-only -->

[license]: https://github.com/guysalt/python-inquirer3/blob/main/LICENSE
[contributor guide]: CONTRIBUTING.md
[download the python-inquirer code from github]: https://github.com/guysalt/python-inquirer3
[download the wheel from pypi]: https://pypi.org/project/inquirer3/#files
[magmax/python-inquirer]: https://github.com/magmax/python-inquirer
