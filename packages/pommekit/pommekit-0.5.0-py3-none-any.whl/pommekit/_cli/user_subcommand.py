#  Copyright (C) 2024  Cypheriel
from pathlib import Path
from typing import Annotated

import typer

__ALIAS__ = "u"

from .._cli import CLIOptions
from .._cli.util.selection import get_selected_device, get_selected_user
from .._cli.util.user_utils import fetch_user
from .._util.aio import run_async
from ..ids import IDSUser
from .util.device_utils import fetch_device
from .util.rich_console import console

app = typer.Typer()


@app.command(name="list", help="List installed users.")
@app.command(name="ls", hidden=True)
def list_() -> None:
    if not CLIOptions.get_user_path().is_dir():
        typer.echo("No users found.", err=True)
        raise typer.Exit(1)

    found = False
    for user_path in CLIOptions.get_user_path().iterdir():
        if user_path.is_dir() and (user_path / "user_info.json").is_file():
            ids_user = fetch_user(user_path)

            if ids_user is None:
                continue

            auth_status = " ([blue]Authenticated[/])" if ids_user.is_fully_authenticated else ""
            registration_status = " ([green]Registered[/])" if ids_user.is_device_registered else ""

            console.print(f"{ids_user.apple_id} {auth_status} {registration_status}")
            found = True

    if not found:
        typer.echo("No users found.", err=True)


@app.command(help="Add a user.")
@run_async
async def add(
    apple_id: Annotated[
        str,
        typer.Option(
            prompt="Apple ID",
            help="The Apple ID of the user.",
        ),
    ],
    password: Annotated[
        str,
        typer.Option(
            prompt=True,
            hide_input=True,
            help="The password of the user.",
        ),
    ],
) -> None:
    if not CLIOptions.selected_device:
        typer.echo("No device selected.", err=True)
        raise typer.Exit(1)

    dev = fetch_device(CLIOptions.device_path, CLIOptions.selected_device)

    if dev.machine_data.requires_provisioning or dev.apns_credentials.requires_provisioning:
        typer.echo("Device is not fully provisioned.", err=True)
        raise typer.Abort

    ids_user = IDSUser(apple_id, dev.machine_data, dev.apns_credentials)

    ids_user.write(CLIOptions.get_user_path() / apple_id)

    await ids_user.start_authentication(password)

    if ids_user.requires_2fa:
        two_factor_code = typer.prompt("Enter the 2FA code: ")
        await ids_user.verify_2fa_code(two_factor_code)

    await ids_user.authenticate_device()

    ids_user.write(CLIOptions.get_user_path() / apple_id)

    await ids_user.register_device(dev.device_info, typer.prompt("Validation data"))

    ids_user.write(CLIOptions.get_user_path() / apple_id)


@app.callback(no_args_is_help=True)
def user(
    device_path: Annotated[
        Path,
        typer.Option(
            "--device-path",
            "-d",
            envvar="POMMEKIT_DEVICE_PATH",
            help="The path to save/load device data to.",
        ),
    ] = CLIOptions.device_path,
    device: Annotated[
        str,
        typer.Option(
            "--device",
            "-d",
            help="The serial number of the device to use.",
        ),
    ] = CLIOptions.selected_device,
) -> None:
    CLIOptions.device_path = device_path
    CLIOptions.selected_device = device or get_selected_device(CLIOptions.device_path)
    CLIOptions.selected_user = get_selected_user(CLIOptions.get_user_path())

    typer.echo(f"User path: {CLIOptions.get_user_path()}")
    typer.echo(f"Device path: {CLIOptions.device_path}")
