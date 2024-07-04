import asyncio
import rich
import typer

from credio.cli.actions.gateway import API
from credio.util.type import Object


action = typer.Typer()


class Account(Object):
    email: str
    password: str


def ask(confirm_password: bool = False):
    email = typer.prompt("Your email")
    password = typer.prompt("Password", hide_input=True)
    if confirm_password:
        for _ in range(3):
            if password == typer.prompt("Confirm password", hide_input=True):
                break
            rich.print("[red]Password not match![/red]")
    return Account(
        {
            "email": email,
            "password": password,
        }
    )


@action.command(name="register", help="Register a Credio account.")
def register():
    account = ask(confirm_password=True)
    rich.print(
        asyncio.run(API().register(email=account.email, password=account.password))
    )


@action.command(name="login", help="Log in to Credio platform.")
def login():
    account = ask()
    rich.print(
        asyncio.run(API().authenticate(email=account.email, password=account.password))
    )


@action.command(name="show", help="Show your logged-in Credio account.")
def show():
    email = asyncio.run(API().info())
    rich.print("Hi, [green]%s[/green]!" % email)


@action.command(name="logout", help="No need to do that.")
def logout():
    confirm = typer.prompt("Sure? (yes/no)", default="no", show_default=True)
    if str(confirm).lower() in ["y", "yes"]:
        asyncio.run(API().logout())
        rich.print("Bye!")
