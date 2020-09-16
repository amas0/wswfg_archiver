import argparse
from datetime import date, timedelta
from pathlib import Path
from typing import List, Tuple

from wswfg_archiver import download_images, save_image


def to_date(text: str) -> date:
    year, month, day = text.split('-')
    return date(year=int(year), month=int(month), day=int(day))


def validate_output_directory(out_dir: str) -> Path:
    p = Path(out_dir)
    if p.exists() and p.is_file():
        raise FileExistsError('Output is an existing file')
    if p.exists() and p.is_dir():
        return p
    else:
        p.mkdir()
        return p


def get_existing_image_dates(out_dir: Path) -> List[date]:
    all_pngs = out_dir.glob('*png')
    files = [file.stem for file in all_pngs]
    dates = []
    for file in files:
        try:
            dates.append(to_date(file))
        except ValueError:
            pass
    return dates


def evaluate_args():
    parser = argparse.ArgumentParser(description='Downloads the web comic "Will Save World For Gold"')
    parser.add_argument('output', help='directory path to store the downloaded comics')
    parser.add_argument('-s', '--start-date', dest='start_date', action='store',
                        help='Format: YYYY-MM-DD. Comic date to start archiving, omitting this will '
                             'pull comics from the past week')
    parser.add_argument('-e', '--end-date', dest='end_date', action='store',
                        help='Format: YYYY-MM-DD. Comic date to end archiving, omitting this will set '
                             'today\'s date at the end')
    parser.add_argument('--download-all', dest='download_all', action='store_const', const=True,
                        help='Enable this flag to download the full comic archive starting from '
                             '2011/09. This will override start and end date args. Use responsibly '
                             'to avoid straining the server.')
    parser.add_argument('--overwrite', dest='overwrite', action='store_const', const=True,
                        help='Overwrite existing archived images.')
    args = parser.parse_args()
    return args


def resolve_dates(start_date: str, end_date: str, existing_dates: List[date],
                  overwrite: bool) -> Tuple[date, date]:
    start_date = to_date(start_date) if start_date else date.today() - timedelta(days=7)
    end_date = to_date(end_date) if end_date else date.today()
    if not overwrite and existing_dates:  # If not overwriting, start on the day after the latest comic
        next_comic_date = max(existing_dates) + timedelta(days=1)
        # If specified start date is later than the latest archive date, use that
        start_date = max((next_comic_date, start_date))

    if start_date > date.today():
        print(f'Archive up to date. Exiting.')
        exit()
    if start_date > end_date:
        print(f'Specified start date after end date. Check your input.')
        exit()

    return start_date, end_date


def archiver(start_date: str, end_date: str, output: str, overwrite: bool):
    output_dir = validate_output_directory(output)
    existing_dates = get_existing_image_dates(output_dir)

    start_date, end_date = resolve_dates(start_date, end_date, existing_dates, overwrite)

    print(f'Downloading images from {start_date} to {end_date}')
    images = download_images(start_date, end_date)
    print(f'Saving {len(images)} to {output_dir}...', end='')
    for image in images:
        save_image(image, output_dir)
    print('done.')


def main():
    args = evaluate_args()
    if args.download_all:
        start_date, end_date = '2011-09-12', None
    else:
        start_date, end_date = args.start_date, args.end_date
    overwrite = bool(args.overwrite)
    archiver(start_date, end_date, args.output, overwrite)
