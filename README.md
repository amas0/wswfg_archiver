## "Will Save World for Gold" Archiver

This simple command-line utility downloads the comic images to an archive directory
from www.willsaveworldforgold.com. 

#### Installation

##### Linux

Assuming `git` and `pip` (`python >= 3.6`):

```bash
git clone https://github.com/amas0/wswfg_archiver.git 
pip install ./wswfg_archiver
```

#### Usage

Installing the utility via `pip` will give you the command line tool, `wswfg`:

```bash
$ wswfg -h

usage: wswfg [-h] [-s START_DATE] [-e END_DATE] [--download-all] output

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
