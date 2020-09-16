## "Will Save World for Gold" Archiver

This simple command-line utility downloads the comic images to an archive directory
from www.willsaveworldforgold.com. 

### Installation

Installation takes advantage of the `pipx` [project](https://github.com/pipxproject/pipx). 

The following will install `git` and `pipx` for your system if not installed.

##### MacOS

If not installed, install [homebrew](https://brew.sh/).

```
$ brew install git pipx
$ pipx ensurepath
```

##### Arch Linux based distros

```
$ pacman -S git python-pipx
$ pipx ensurepath
```

_Note: you need to close and reopen your terminal after `pipx ensurepath`_

#### Install

The following command will install the utility.

```
$ pipx install git+https://github.com/amas0/wswfg_archiver.git
```


#### Usage

Installation will give you the command line tool `wswfg`:

```
$ wswfg -h

usage: wswfg [-h] [-s START_DATE] [-e END_DATE] [--download-all] [--overwrite] output

Downloads the web comic "Will Save World For Gold"

positional arguments:
  output                directory path to store the downloaded comics

optional arguments:
  -h, --help            show this help message and exit
  -s START_DATE, --start-date START_DATE
                        Format: YYYY-MM-DD. Comic date to start archiving, omitting this will pull comics from the past week
  -e END_DATE, --end-date END_DATE
                        Format: YYYY-MM-DD. Comic date to end archiving, omitting this will set today's date at the end
  --download-all        Enable this flag to download the full comic archive starting from 2011/09. This will override start and end date args. Use responsibly to avoid straining the server.
  --overwrite           Overwrite existing archived images.
```

Basic usage to download all comics from the past 7 days just requires specifying the directory you'd like to save them to:

```
$ wswfg archive_dir/

Downloading 6 images...done.
Saving 6 to archive_dir...done.
```

As seen in the help, you can specify the start and end dates to archive:

```
$ wswfg -s 2020-01-01 -e 2020-01-31 jan_archive/

Downloading 23 images...done.
Saving 23 to jan_archive...done.
```

For a full archive, you can use the `--download-all` flag:

```
$ wswfg --download_all full_archive/
```

By default, the tool looks in the provided `output` directory and checks for existing
archived images. If found, it will only update newer images than those already found. 
Passing the `--overwrite` flag will ignore this behavior.
