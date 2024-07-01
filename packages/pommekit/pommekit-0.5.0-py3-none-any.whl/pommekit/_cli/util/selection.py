#  Copyright (C) 2024  Cypheriel
from pathlib import Path

import typer


def get_selected_device(path: Path) -> str | None:
    selected_file = path / ".selected_device"

    if selected_file.is_file() and (selected_device := selected_file.read_text()):
        typer.echo(f"{selected_device = }")
        return selected_device
    return None


def set_selected_device(path: Path, serial: str) -> None:
    if path.is_dir() and serial in (device.name for device in path.iterdir()):
        selected_file = path / ".selected_device"
        selected_file.write_text(serial)

    else:
        msg = "Failed to select device. Device not found."
        raise ValueError(msg)


def get_selected_user(path: Path) -> str | None:
    selected_file = path / ".selected_user"

    if selected_file.is_file() and (selected_user := selected_file.read_text()):
        return selected_user
    return None


def set_selected_user(path: Path, username: str) -> None:
    if path.is_dir() and username in (user.name for user in path.iterdir()):
        selected_file = path / ".selected_user"
        selected_file.write_text(username)

    else:
        msg = "Failed to select user. User not found."
        raise ValueError(msg)
