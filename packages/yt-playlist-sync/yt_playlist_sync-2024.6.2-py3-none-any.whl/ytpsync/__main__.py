import logging
from .argumentparser import parse_args
from .downloader import download_playlist

# 48273

def main():
    '''Main driver function.
    '''
    args, additional_args = parse_args()
    download_playlist(args.playlist, args.directory, executable=args.executable,
                      executable_args=additional_args)
    logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    main()
