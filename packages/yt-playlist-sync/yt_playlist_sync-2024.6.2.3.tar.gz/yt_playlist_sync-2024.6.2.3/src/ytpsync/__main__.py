import logging
from .argumentparser import parse_args
from .downloader import download_playlist

# 48273

def main():
    '''Main driver function.
    '''
    args, additional_args = parse_args()
    logging.basicConfig(level=args.logging)
    logging.info("Selected playlist: %s", args.playlist)
    logging.info("Selected directory: %s", args.directory)
    download_playlist(args.playlist, args.directory, executable=args.executable,
                      executable_args=additional_args)

if __name__ == "__main__":
    main()
