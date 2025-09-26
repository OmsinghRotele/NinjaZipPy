import argparse
from .core import zip_to_7z, unzip_7z, list_contents

def main():
    parser = argparse.ArgumentParser(prog='ninjazippy')
    sub = parser.add_subparsers(dest='cmd', required=True)

    pzip = sub.add_parser('zip', help='Compress file/dir to .7z')
    pzip.add_argument('input', help='file or directory to compress')
    pzip.add_argument('output', help='output .7z file')
    pzip.add_argument('-p', '--password', default=None)

    punzip = sub.add_parser('unzip', help='Extract .7z archive')
    punzip.add_argument('archive', help='archive.7z')
    punzip.add_argument('outdir', help='output folder')
    punzip.add_argument('-p', '--password', default=None)

    plist = sub.add_parser('list', help='List contents of archive')
    plist.add_argument('archive')

    args = parser.parse_args()
    if args.cmd == 'zip':
        zip_to_7z(args.input, args.output, args.password)
        print(f"Zipped {args.input} -> {args.output}")
    elif args.cmd == 'unzip':
        unzip_7z(args.archive, args.outdir, args.password)
        print(f"Unzipped {args.archive} -> {args.outdir}")
    elif args.cmd == 'list':
        for n in list_contents(args.archive):
            print(n)

if __name__ == "__main__":
    main()
