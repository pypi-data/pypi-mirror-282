"""Return to the most recently used directory when starting the xonsh shell. """

from pathlib import Path
from xonsh import dirstack

_file = Path(__xonsh__.env.get('XDG_CACHE_HOME', '~/.cache')).expanduser() / 'xontrib-back2dir' / 'latest.path'

@events.on_post_init
def on_post_init(**_):
    if Path(__xonsh__.env["PWD"]) == Path(__xonsh__.env["HOME"]).resolve() and _file.exists():
        d = Path(_file.read_text().strip())
        nd = d
        ndp = d
        for _ in range(0, 1000):
            if not nd.exists():
                ndp = nd.parent
                if ndp == nd:
                    return
                nd = ndp
            else:
                __xonsh__.subproc_captured_stdout(['cd', str(nd)])
                return

@events.on_chdir
def _xontrib_back2dir(olddir, newdir, **kwargs):
    if not _file.parent.exists():
        _file.parent.mkdir(parents=True, exist_ok=True)
    with open(_file, 'w') as f:
        print(newdir, end='', file=f)
