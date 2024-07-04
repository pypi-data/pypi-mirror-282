import click
from rich.traceback import install
import typer

from credio.cli import actions


install(suppress=[click])

app = typer.Typer(
    rich_markup_mode="markdown",
    no_args_is_help=True,
    pretty_exceptions_show_locals=False,
    help="A command-line tool to build everything.",
)
app.add_typer(
    actions.config, name="config", help="All command-line tool configurations."
)
app.add_typer(
    actions.zkml,
    name="zkml",
    help="[WIP] Use ZKML functionalities (use ezkl tool actually).",
)
app.add_typer(
    actions.auth,
    name="me",
    help="You on Credio platform (normally show your registered email).",
)
app.add_typer(
    actions.artifact,
    name="artifact",
    help="Interact with artifacts (datasets, model submission, etc.)",
)
app.add_typer(
    typer.Typer(no_args_is_help=True),
    name="more",
    help="More features have been being built, available soon!",
)


def main():
    app()
