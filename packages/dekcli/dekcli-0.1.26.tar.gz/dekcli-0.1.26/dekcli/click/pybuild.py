import os
import typing
import typer
from typing_extensions import Annotated
from dektools.typer import multi_options_to_dict
from ..core.pyinstaller.core import build_target as pyinstaller_build_target
from ..core.nuitka.core import build_target as nuitka_build_target

app = typer.Typer(add_completion=False)


@app.command()
def pyinstaller(
        path: Annotated[str, typer.Argument()] = '',
        kw: typing.Optional[typing.List[str]] = typer.Option(None)
):
    if not path:
        path = os.getcwd()
    kwargs = multi_options_to_dict(kw)
    pyinstaller_build_target(path, kwargs)


@app.command()
def nuitka(path: Annotated[str, typer.Argument()] = ''):
    if not path:
        path = os.getcwd()
    nuitka_build_target(path)
