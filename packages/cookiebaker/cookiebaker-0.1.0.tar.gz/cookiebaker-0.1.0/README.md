# `cookiebaker` - Use `cookiecutter` with existing code and git integration

`cookiebaker` is a simple wrapper for [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) which attempts to:

* Set `full_name` and `email` in the `cookiecutter` config from your Git config
* Use existing folders or files as the initial project source
* Initialize a Git repository in the newly created project folder

`src` layout is assumed, and the cookiecutter is expected **not** to contain a `src/` folder. An empty `src/` folder will be created in the template, and files and folders will be copied under that directory.

Because of the high probability that the project shares a name with a source folder, the cookiecutter is assembled in a local temporary directory first. Upon successful assembly, the original source is removed, the new project folder is moved out to the current level, and the temporary directory is removed.

A simple compatible cookiecutter is also included, and will be used by default. It assumes you are the sole author of the project, so it does not attempt to provide a code of conduct, contributor license agreement, guidelines for contributors etc. It assumes the project will be a pure Python project following modern packaging standards.

----

This project is open source software, licensed under the terms of The Unlicense.
Please see `LICENSE.txt` for details.
