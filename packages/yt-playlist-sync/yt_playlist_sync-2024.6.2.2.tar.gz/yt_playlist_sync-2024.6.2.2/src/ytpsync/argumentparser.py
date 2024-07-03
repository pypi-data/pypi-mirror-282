import os
import logging
from shutil import which
from argparse import ArgumentParser, Namespace
from typing import Tuple
from urllib.parse import urlparse, urlunparse
from pathlib import Path

def url_type(potential_url: str) -> str:
    '''Custom URL argparse type that will do URL parsing to validate
    a URL argument.

    :param potential_url: Potential URL.
    :type potential_url: str
    :raises ValueError: Error raised if URL is malformed.
    :return: The URL if valid.
    :rtype: str
    '''
    parsed_url = urlparse(potential_url)
    if not any((parsed_url.scheme, parsed_url.netloc)):
        raise ValueError(f"URL \"{potential_url}\" is malformed.")
    return urlunparse(parsed_url)

def directory_type(potential_dir: Path) -> Path:
    '''Custom directory argparse type.

    :param potential_dir: Potential directory_
    :type potential_dir: Path
    :raises ValueError: Error raised if path is not a directory.
    :return: The resolved potential directory.
    :rtype: Path
    '''

    if not isinstance(potential_dir, Path):
        potential_dir = Path(potential_dir)
    # Create path if it doesn't exist
    if not potential_dir.exists():
        potential_dir.mkdir(parents=True, exist_ok=True)
    if not potential_dir.is_dir():
        raise ValueError(f"Path {potential_dir} is not a directory.")
    return potential_dir.resolve()

def executable_type(executable_path: Path) -> Path:
    '''Custom executable argparse type.

    :param executable_path: The executable path.
    :type executable_path: Path
    :raises ValueError: Error raised if path is not an existing executable file.
    :return: The path resolved.
    :rtype: Path
    '''
    if not isinstance(executable_path, Path):
        executable_path = Path(executable_path)
    if not executable_path.exists():
        raise ValueError(f"Path {executable_path} does not exist.")
    if not executable_path.is_file():
        raise ValueError(f"Path {executable_path} is not a file.")
    if not os.access(executable_path, os.X_OK):
        raise ValueError(f"Path {executable_path} is not executable.")
    return executable_path.resolve()

def parse_args() -> (Namespace, Namespace):
    '''Create an argument parser and parse args.

    :return: The parsed arguments, and unparsed arguments.
    :rtype: Namespace
    '''
    # Create argument parser
    argparser: ArgumentParser = ArgumentParser(
                                    prog="yt-p-sync",
                                    description="Sync a YouTube playlist.",
                                    epilog="Any additional options will be "
                                           "passed directly to your yt-dlp "
                                           "executable."
                                )
    default_executable: str = which("yt-dlp")
    argparser.add_argument("--executable", type=executable_type, required=False,
                           help="Path to yt-dlp executable.", default=default_executable)
    argparser.add_argument("--logging", help="Logging level. Default 20 (INFO).", default=logging.INFO,
                           choices=(logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL))
    argparser.add_argument("playlist", type=url_type, help="URL of playlist to sync.")
    argparser.add_argument("directory", type=directory_type, help="Directory to sync playlist to.")

    # Parse arguments and return results
    args, unknown_args = argparser.parse_known_args()

    return (args, unknown_args)
