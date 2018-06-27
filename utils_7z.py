from libarchive import public, constants
import argparse
from os import listdir
from os.path import isdir, join, abspath


def compress_7z(path, output):
    if isdir(path):
        to_compress = listdir(path)
        to_compress = [join(path,i) for i in to_compress]
        for i in public.create_file(
                output,
                constants.ARCHIVE_FORMAT_7ZIP,
                to_compress):
            print(i)
    else:
        for i in public.create_file(
                filename,
                constants.ARCHIVE_FORMAT_7ZIP,
                path):
            print(i)

def extract_7z(path):
    for entry in public.file_pour(path):
        print(entry)

def read_from_7z(path):
    with public.file_reader(path) as e:
        for entry in e:
            with open('/tmp/' + str(entry), 'wb') as f:
                for block in entry.get_blocks():
                    f.write(block)


parser = argparse.ArgumentParser(description="Tools to compress/extract 7z")
parser.add_argument(
    "-p",
    "--path",
    dest="path",
    help="This can be a file name or a path to the file")
parser.add_argument(
    "-o",
    "--output",
    dest="output",
    help="This is the output of compression and has to end with `.7z`")
parser.add_argument(
    "-e",
    "--extract",
    dest="extract",
    action="store_true",
    help="Set this to extract all files from [FILENAME].7z")
parser.add_argument(
    "-c",
    "--compress",
    dest="compress",
    action="store_true",
    help="Set this to compress file or folder and create [FILENAME].7z")


args = parser.parse_args()
path = args.path
output = args.output

if args.extract:
    if path:
        extract_7z(path)

if args.compress:
    if path:
        if output:
            compress_7z(path, output)
