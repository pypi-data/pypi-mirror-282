# {{ cookiecutter.__project_name }} - {{ cookiecutter.project_short_description }}

{% if cookiecutter.is_open_source -%}
[![](https://img.shields.io/pypi/v/{{ cookiecutter.__pypi_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.__pypi_slug }})
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.__rtd_slug }}/badge/?version=latest)](https://{{ cookiecutter.__rtd_slug }}.readthedocs.io/en/latest/?version=latest)

{% endif -%}
## Installation

`pip install {{ cookiecutter.__pypi_slug }}`

## Documentation

See full documentation at https://{{ cookiecutter.__rtd_slug }}.readthedocs.io.

----

Copyright &copy; {{ cookiecutter.__year }} {{ cookiecutter.__full_name }}
{%- if cookiecutter.is_open_source %}

This project is open source software, distributed under the terms of {{ cookiecutter.license_name }}.
Please see `LICENSE.txt` for details.
{%- endif -%}
