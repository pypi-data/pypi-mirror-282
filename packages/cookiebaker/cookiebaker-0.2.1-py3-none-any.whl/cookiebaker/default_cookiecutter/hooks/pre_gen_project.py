# A name that can follow "distributed under the terms of".
{% set license_name = {
    'MIT': 'the MIT License',
    'Unlicense': 'The Unlicense'
}.get(cookiecutter.license_spdx, '') %}

{% set is_open_source = cookiecutter.license_spdx != '' %}

{% if cookiecutter.versioning == 'semver' %}
{% set version = '0.1.0' %}
{% else %}
{% set version = cookiecutter.__year ~ '.' ~ cookiecutter.__month ~ '.0' %}
{% endif %}

{% set extra_values = {
    'license_name': license_name,
    'is_open_source': is_open_source,
    'version': version
} %}

"{{ cookiecutter.update(extra_values) }}"


