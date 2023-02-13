"""This module provides the parsely CLI."""
# parsely/cli.py

from typing import Optional

import typer

from parsely import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        print(f"{__app_name__} v{__version__}")


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return