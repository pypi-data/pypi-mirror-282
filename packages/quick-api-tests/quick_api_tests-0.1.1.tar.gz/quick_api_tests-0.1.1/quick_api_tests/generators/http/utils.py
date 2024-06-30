from pathlib import Path
from subprocess import (
    PIPE,
    Popen,
    run,
)
from typing import (
    Optional,
    Tuple,
)
from urllib.parse import urlparse


def create_and_write_file(file_path: Path, text=None):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    if text:
        file_path.write_text(text)


def is_url(path):
    parsed = urlparse(path)
    return bool(parsed.scheme) and bool(parsed.netloc)


def run_command(command: str) -> Tuple[int, Optional[str]]:
    result = run(command, shell=True, stderr=PIPE, text=True)  # noqa: S602
    stderr = result.stderr
    return result.returncode, stderr
