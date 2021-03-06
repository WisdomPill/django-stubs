import os
from django.core.management.base import (
    BaseCommand as BaseCommand,
    CommandError as CommandError,
    CommandParser as CommandParser,
)
from django.core.management.utils import find_command as find_command, popen_wrapper as popen_wrapper
from typing import List, Tuple, Union

_PathType = Union[str, bytes, os.PathLike]

def has_bom(fn: _PathType) -> bool: ...
def is_writable(path: _PathType) -> bool: ...

class Command(BaseCommand):
    program: str = ...
    program_options: List[str] = ...
    verbosity: int = ...
    has_errors: bool = ...
    def compile_messages(self, locations: List[Tuple[_PathType, _PathType]]) -> None: ...
