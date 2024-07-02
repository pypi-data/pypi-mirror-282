from cookiecutter.main import cookiecutter
from datetime import datetime
from pathlib import Path
import shutil, sys, tempfile

_default_cookiecutter = str(Path(__file__).parent / 'default_cookiecutter')
assert ':' not in _default_cookiecutter, "please use a path without colons"


def create(name, *sources):
    now = datetime.now()
    context = {
        '__project_name': name,
        '__pypi_slug': name.lower().replace(' ', '_').replace('-', '_'),
        '__rtd_slug': name.lower().replace(' ', '-').replace('_', '-'),
        '__full_name': 'A User',
        '__email': 'a@user.com',
        '__year': now.year,
        '__month': now.month
    }
    tmp = tempfile.mkdtemp(dir='.')
    cookiecutter(_default_cookiecutter, output_dir=tmp, extra_context=context)
    tmp = Path(tmp)
    # The temporary directory should only contain the single directory
    # that was created by `cookiecutter`.
    contents = tmp.iterdir()
    created = next(contents)
    src = created / 'src'
    assert not list(contents)
    src.mkdir()
    for source in sources:
        shutil.move(source, src / source)
    shutil.move(created, '.')
    tmp.rmdir()


def cli():
    return create(*sys.argv[1:])


if __name__ == '__main__':
    sys.exit(cli())
