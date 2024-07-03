# `cookiebaker` - Use `cookiecutter` with existing code and git integration

[![](https://img.shields.io/pypi/v/cookiebaker.svg)](https://pypi.org/project/cookiebaker)
<!-- [![Documentation Status](https://readthedocs.org/projects/cookiebaker/badge/?version=latest)](https://cookiebaker.readthedocs.io/en/latest/?version=latest) -->

`cookiebaker` is a simple wrapper for [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) which attempts to:

* Set `full_name` and `email` in the `cookiecutter` config from your Git config
* Use existing folders or files as the initial project source
* Initialize a Git repository in the newly created project folder
* Commit the initial set of files to the Git repository

`src` layout is assumed, and the cookiecutter is expected **not** to contain a `src/` folder. An empty `src/` folder will be created in the template, and files and folders will be copied under that directory.

Because of the high probability that the project shares a name with a source folder, the cookiecutter is assembled in a local temporary directory first. Upon successful assembly, the original source is removed, the new project folder is moved out to the current level, and the temporary directory is removed.

A simple compatible cookiecutter is also included, and will be used by default. It assumes you are the sole author of the project, so it does not attempt to provide a code of conduct, contributor license agreement, guidelines for contributors etc. It does, however, attempt to adapt the project contents to your choice of license, and assumes the project will be a pure Python project following modern packaging standards.

## Installation

### With `pipx` (recommended)

If you already have `cookiecutter` installed via `pipx`:
```
pipx inject --include-apps cookiecutter cookiebaker
```
This will add `cookiebaker` to your existing `cookiecutter` installation, so you don't need a second copy of `cookiecutter` as a dependency.

If you don't have `cookiecutter`, but you have `pipx`:
```
pipx install --include-deps cookiebaker
```
This will download and install `cookiecutter` as a dependency of `cookiebaker`, and make its command-line tools available as well.

If you don't have `pipx`, [get it first](https://pipx.pypa.io/stable/installation/).

### With `pip`

If you don't want to use `pipx`, you can install `cookiebaker` with `pip` instead. Please keep in mind that `cookiebaker` is an application, and does not provide any meaningful API or library. No particular guidance is provided here, as users who have a good reason to do it this way should know what they're doing already.

## Documentation

Run the program with `new-project`, specifying a name for the new project and then the files and/or folders to use as the initial project source.

For example, from a single file:
```
new-project "My Awesome Project" example.py
```
The new project will be created in `my_awesome_project`, and `example.py` will be moved directly under `src`.

To choose a license for the project, specify its SPDX id when prompted.

Currently these licenses are supported:

* the MIT license (MIT)
* The Unlicense (Unlicense)

<!-- See full documentation at https://cookiebaker.readthedocs.io. -->

----

Copyright &copy; 2024 Karl Knechtel

This project is open source software, distributed under the terms of The Unlicense.
Please see `LICENSE.txt` for details.
