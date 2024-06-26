
from argparse import ArgumentParser
from xnb import XNBReader

def parse_args():
    parser = ArgumentParser(description='Convert XNB files to PNG')
    parser.add_argument('input', help='Input XNB file')
    parser.add_argument('output', help='Output PNG file')
    return parser.parse_args()

def main():
    args = parse_args()
    reader = XNBReader(args.input)
    reader.save(args.output)

if __name__ == '__main__':
    main()
