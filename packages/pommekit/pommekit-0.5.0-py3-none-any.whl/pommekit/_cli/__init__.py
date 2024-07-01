#  Copyright (C) 2024  Cypheriel
from pathlib import Path
from typing import ClassVar

from pommekit._cli.util.app_dirs import USER_DATA_DIR


class CLIOptions:
    save_path: ClassVar[Path] = USER_DATA_DIR
    device_path: ClassVar[Path] = save_path / "Devices"
    selected_device: ClassVar[str | None] = None
    selected_user: ClassVar[str | None] = None

    @staticmethod
    def get_user_path() -> Path:
        if not CLIOptions.selected_device:
            msg = "No device selected."
            raise ValueError(msg)

        if not CLIOptions.selected_device:
            msg = "No device selected."
            raise ValueError(msg)

        return CLIOptions.device_path / CLIOptions.selected_device / "Users"
