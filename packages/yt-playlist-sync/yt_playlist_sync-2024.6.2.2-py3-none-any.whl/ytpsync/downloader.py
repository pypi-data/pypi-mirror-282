import subprocess
import logging
import os
from pathlib import Path
from typing import Dict, List

def kwargs_to_args(kwargs: Dict[str, str]) -> List[str]:
    '''Generate a list of arguments from keyword arguments.

    :param kwargs: Keyword arguments
    :type kwargs: Dict[str, str]
    :return: Arguments in order
    :rtype: List[str]
    '''
    args: list = []
    for key, arg in kwargs.items():
        if len(key) == 1:
            keyword = "-" + key
        else:
            keyword = "--" + key
        args.append(keyword)
        args.append(arg)
    return args

def download_playlist(playlist: str, output_directory: Path, executable: Path,
                      executable_args: list):
    '''Download playlist contents into a directory.

    :param playlist: Playlist URL.
    :type playlist: str
    :param output_directory: Output directory.
    :type output_directory: Path
    :param executable: Path to yt-dlp executable.
    :type executable: Path
    :param executable_args: Arguments to pass to executable
    :type executable_args: list
    '''
    # First, try to remove any options that could interfere with our script
    # from the executable args
    remove_slices: list = []
    invalid_options: list = ['-P', "--paths", '-a', '--batch-file', '-O', '--print',
                             '--newline', '--no-progress', '--progress', '--print-traffic',
                             '-v', '--verbose']
    for index, value in enumerate(executable_args):
        if(value in invalid_options):
            remove_slices.append((index, index+1))
    for remove_slice in reversed(remove_slices):
        del executable_args[remove_slice[0]:remove_slice[1]]
    
    # Then, append our own arguments
    additional_args: list = ['-P', str(output_directory), '--no-progress', '--print',
                             'after_move:filepath', '--', playlist]


    if not executable_args:
        executable_args = []
    for arg in additional_args:
        executable_args.append(arg)

    executable_args.insert(0, str(executable))
    
    logging.debug("Subprocess arguments: %s", executable_args)

    # Run the process and capture all filepaths
    logging.info("Beginning sync...")
    filepaths: list = None
    with subprocess.Popen(executable_args,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          text=True) as process:
        output, error = process.communicate()
        return_code: int = process.returncode
        logging.debug("yt-dlp return code: %s", return_code)
        if return_code != 0:
            logging.critical("There was error running yt-dlp. See below:")
            logging.error("yt-dlp error: %s", error)
            return False
        output_lines: list = output.splitlines()
        filepaths = [Path(filepath.strip()).resolve() for filepath in output_lines]

    logging.debug("Extracted video paths: %s", filepaths)

    for dirpath, _, filenames in os.walk(output_directory):
        for filename in filenames:
            filepath: Path = Path(dirpath) / Path(filename)
            resolved: Path = filepath.resolve()
            logging.debug("Walked over: %s", resolved)
            if not (resolved in filepaths):
                logging.debug("Found extra file in directory: %s", filepath)
                logging.info("Removing file: %s", filepath)
                os.remove(resolved)

    logging.info("Syncing complete.")
    return True
