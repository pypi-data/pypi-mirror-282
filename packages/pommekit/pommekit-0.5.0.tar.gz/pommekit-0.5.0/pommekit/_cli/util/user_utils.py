#  Copyright (C) 2024  Cypheriel
from pathlib import Path

from ...ids import IDSUser


def fetch_user(path: Path) -> IDSUser | None:
    if not path.is_dir():
        return None

    return IDSUser.read(path)
