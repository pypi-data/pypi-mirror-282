# yt-playlist-sync
Sync a YouTube playlist to a directory on your system using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Getting Started

### Requirements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp).
- Python 3.10+
- (Strongly recommended) [ffmpeg](https://www.ffmpeg.org/)
- [Python Modules](requirements.txt)*

\* These should be installed by running the install scripts.

### Installation

Copy the directory to your machine, and run `pip install -U .` in the newly created directory.

## Usage

### CLI

The command-line interface has the following syntax:

```
usage: yt-p-sync [-h] [--executable EXECUTABLE] [--logging {10,20,30,40,50}]
                 playlist directory

Sync a YouTube playlist.

positional arguments:
  playlist              URL of playlist to sync.
  directory             Directory to sync playlist to.

options:
  -h, --help            show this help message and exit
  --executable EXECUTABLE
                        Path to yt-dlp executable.
  --logging {10,20,30,40,50}
                        Logging level. Default 20 (INFO).

Any additional options will be passed directly to your yt-dlp executable.
```


## Authors

- Willow Ciesialka

## License

This project is licensed under GNU General Public License v3.0. See [LICENSE](LICENSE) for more details.