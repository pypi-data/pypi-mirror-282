from cookiecutter.main import cookiecutter
from datetime import datetime
from pathlib import Path
import shutil, subprocess, sys, tempfile

_default_cookiecutter = str(Path(__file__).parent / 'default_cookiecutter')
assert ':' not in _default_cookiecutter, "please use a path without colons"


def git_config(key):
    git_args = ['git', 'config', '--get', key]
    return subprocess.check_output(git_args, text=True).strip()


def git_init(where):
    subprocess.call(['git', 'init', where])


def git_commit(where):
    subprocess.call(['git', '-C', where, 'add', '.'])
    subprocess.call(['git', '-C', where, 'commit', '-m', 'Initial commit'])


def create(name, *sources):
    now = datetime.now()
    context = {
        '__project_name': name,
        '__pypi_slug': name.lower().replace(' ', '_').replace('-', '_'),
        '__rtd_slug': name.lower().replace(' ', '-').replace('_', '-'),
        '__full_name': git_config('user.name'),
        '__email': git_config('user.email'),
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
    assert not list(contents)
    git_init(created)
    src = created / 'src'
    src.mkdir()
    for source in sources:
        shutil.move(source, src / source)
    git_commit(created)
    shutil.move(created, '.')
    tmp.rmdir()


def cli():
    return create(*sys.argv[1:])


if __name__ == '__main__':
    sys.exit(cli())
