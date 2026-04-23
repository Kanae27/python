import argparse
import os
import sys


def read_text_file(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()


def main():
    parser = argparse.ArgumentParser(description='Read and display a document file.')
    parser.add_argument('path', help='Path to the document file')
    parser.add_argument('-n', '--lines', type=int, default=None, help='Show only the first N lines')
    args = parser.parse_args()

    path = args.path
    if not os.path.isfile(path):
        print(f'Error: file not found: {path}', file=sys.stderr)
        sys.exit(1)

    _, ext = os.path.splitext(path)
    ext = ext.lower()
    if ext not in {'.txt', '.md', '.csv', '.py', '.json', '.log'}:
        print(f'Error: unsupported file type: {ext}', file=sys.stderr)
        sys.exit(1)

    content = read_text_file(path)
    if args.lines is not None:
        lines = content.splitlines()
        content = '\n'.join(lines[: args.lines])

    print(content)


if __name__ == '__main__':
    main()
